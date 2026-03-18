import json
import os
from datetime import datetime

PLANNER_FILE = os.path.join(os.path.dirname(__file__), 'data', 'planner.json')

def load_planner():
    if os.path.exists(PLANNER_FILE):
        with open(PLANNER_FILE, 'r') as f:
            return json.load(f)
    return {'groups': {}}

def save_planner(data):
    os.makedirs(os.path.dirname(PLANNER_FILE), exist_ok=True)
    with open(PLANNER_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_task(group_id, title, description, category,
             assigned_to, priority, due_date=''):
    data = load_planner()
    if group_id not in data['groups']:
        data['groups'][group_id] = {'tasks': []}

    task = {
        'id':          f"task_{datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        'title':       title,
        'description': description,
        'category':    category,
        'assigned_to': assigned_to,
        'priority':    priority,
        'due_date':    due_date,
        'completed':   False,
        'created_at':  datetime.now().isoformat(),
        'completed_at': None
    }

    data['groups'][group_id]['tasks'].append(task)
    save_planner(data)
    return {'success': True, 'task': task}

def get_tasks(group_id):
    data  = load_planner()
    if group_id not in data['groups']:
        return {'tasks': [], 'stats': get_empty_stats()}
    tasks = data['groups'][group_id]['tasks']
    return {'tasks': tasks, 'stats': calculate_stats(tasks)}

def toggle_task(group_id, task_id):
    data = load_planner()
    if group_id not in data['groups']:
        return {'success': False, 'error': 'Group not found'}

    for task in data['groups'][group_id]['tasks']:
        if task['id'] == task_id:
            task['completed']    = not task['completed']
            task['completed_at'] = datetime.now().isoformat() if task['completed'] else None
            save_planner(data)
            return {'success': True, 'completed': task['completed']}

    return {'success': False, 'error': 'Task not found'}

def delete_task(group_id, task_id):
    data = load_planner()
    if group_id not in data['groups']:
        return {'success': False, 'error': 'Group not found'}

    tasks = data['groups'][group_id]['tasks']
    data['groups'][group_id]['tasks'] = [
        t for t in tasks if t['id'] != task_id
    ]
    save_planner(data)
    return {'success': True}

def update_task(group_id, task_id, updates):
    data = load_planner()
    if group_id not in data['groups']:
        return {'success': False, 'error': 'Group not found'}

    for task in data['groups'][group_id]['tasks']:
        if task['id'] == task_id:
            for key, val in updates.items():
                if key in task:
                    task[key] = val
            save_planner(data)
            return {'success': True, 'task': task}

    return {'success': False, 'error': 'Task not found'}

def calculate_stats(tasks):
    if not tasks:
        return get_empty_stats()

    total     = len(tasks)
    completed = sum(1 for t in tasks if t['completed'])
    by_cat    = {}
    by_person = {}
    by_priority = {'high': 0, 'medium': 0, 'low': 0}

    for task in tasks:
        cat = task.get('category', 'other')
        by_cat[cat] = by_cat.get(cat, {'total': 0, 'completed': 0})
        by_cat[cat]['total']     += 1
        by_cat[cat]['completed'] += 1 if task['completed'] else 0

        person = task.get('assigned_to', 'Unassigned')
        by_person[person] = by_person.get(person, {'total': 0, 'completed': 0})
        by_person[person]['total']     += 1
        by_person[person]['completed'] += 1 if task['completed'] else 0

        priority = task.get('priority', 'medium')
        if priority in by_priority:
            by_priority[priority] += 1

    return {
        'total':       total,
        'completed':   completed,
        'pending':     total - completed,
        'percentage':  round((completed / total) * 100) if total > 0 else 0,
        'by_category': by_cat,
        'by_person':   by_person,
        'by_priority': by_priority
    }

def get_empty_stats():
    return {
        'total': 0, 'completed': 0, 'pending': 0,
        'percentage': 0, 'by_category': {},
        'by_person': {}, 'by_priority': {}
    }

def generate_default_tasks(group_id, destination, duration, members):
    """Auto-generate a starter task list based on trip details."""
    default_tasks = [
        # Documents
        {'title': 'Collect Aadhaar/ID copies', 'description': 'Scan and share with group', 'category': 'documents', 'priority': 'high'},
        {'title': 'Apply for travel insurance', 'description': f'Coverage for {duration} days', 'category': 'documents', 'priority': 'medium'},
        {'title': 'Check passport validity',    'description': 'Must be valid for 6 months', 'category': 'documents', 'priority': 'high'},

        # Bookings
        {'title': f'Book flights to {destination}',  'description': 'Compare prices on MakeMyTrip', 'category': 'bookings', 'priority': 'high'},
        {'title': f'Book hotel in {destination}',    'description': f'{duration} nights accommodation', 'category': 'bookings', 'priority': 'high'},
        {'title': 'Book airport transfers',          'description': 'Cab/shuttle to airport', 'category': 'bookings', 'priority': 'medium'},
        {'title': 'Reserve activities/experiences',  'description': 'Book popular spots in advance', 'category': 'bookings', 'priority': 'medium'},

        # Packing
        {'title': 'Pack clothes',      'description': f'Pack for {duration} days', 'category': 'packing', 'priority': 'medium'},
        {'title': 'Pack medications',  'description': 'First aid kit and personal meds', 'category': 'packing', 'priority': 'high'},
        {'title': 'Charge all devices','description': 'Phone, camera, power bank', 'category': 'packing', 'priority': 'low'},
        {'title': 'Pack adapters',     'description': 'Universal travel adapter', 'category': 'packing', 'priority': 'low'},

        # Activities
        {'title': f'Research top spots in {destination}', 'description': 'Make a list of must-visits', 'category': 'activities', 'priority': 'medium'},
        {'title': 'Plan day-by-day itinerary',            'description': 'Use PackVote AI itinerary', 'category': 'activities', 'priority': 'medium'},
        {'title': 'Find local food recommendations',       'description': 'Best restaurants and street food', 'category': 'activities', 'priority': 'low'},
    ]

    # Assign tasks round-robin to members
    for i, task in enumerate(default_tasks):
        assigned = members[i % len(members)] if members else 'Unassigned'
        add_task(
            group_id    = group_id,
            title       = task['title'],
            description = task['description'],
            category    = task['category'],
            assigned_to = assigned,
            priority    = task['priority']
        )

    return get_tasks(group_id)