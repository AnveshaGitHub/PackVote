import json
from datetime import datetime
from database import execute_query, execute_one


def add_task(group_id, title, description, category,
             assigned_to, priority, due_date=''):
    task_id = f"task_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"

    execute_query("""
        INSERT INTO tasks
            (task_id, group_id, title, description, category,
             assigned_to, priority, due_date, completed, created_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        task_id, group_id, title, description or '', category,
        assigned_to, priority,
        due_date if due_date else None,
        False,
        datetime.now()
    ))

    return {
        'success': True,
        'task': {
            'id':          task_id,
            'title':       title,
            'description': description or '',
            'category':    category,
            'assigned_to': assigned_to,
            'priority':    priority,
            'due_date':    due_date or '',
            'completed':   False,
            'created_at':  str(datetime.now())
        }
    }


def get_tasks(group_id):
    rows = execute_query(
        "SELECT * FROM tasks WHERE group_id = %s ORDER BY created_at ASC",
        (group_id,), fetch=True
    ) or []

    tasks = []
    for row in rows:
        tasks.append({
            'id':           row['task_id'],
            'title':        row['title'],
            'description':  row['description'] or '',
            'category':     row['category'],
            'assigned_to':  row['assigned_to'],
            'priority':     row['priority'],
            'due_date':     str(row['due_date']) if row['due_date'] else '',
            'completed':    bool(row['completed']),
            'completed_at': str(row['completed_at']) if row['completed_at'] else None,
            'created_at':   str(row['created_at'])
        })

    return {
        'tasks': tasks,
        'stats': calculate_stats(tasks)
    }


def toggle_task(group_id, task_id):
    task = execute_one(
        "SELECT * FROM tasks WHERE task_id = %s AND group_id = %s",
        (task_id, group_id)
    )
    if not task:
        return {'success': False, 'error': 'Task not found'}

    new_completed    = not bool(task['completed'])
    completed_at_val = datetime.now() if new_completed else None

    execute_query("""
        UPDATE tasks
        SET completed = %s, completed_at = %s
        WHERE task_id = %s AND group_id = %s
    """, (new_completed, completed_at_val, task_id, group_id))

    return {'success': True, 'completed': new_completed}


def delete_task(group_id, task_id):
    task = execute_one(
        "SELECT task_id FROM tasks WHERE task_id = %s AND group_id = %s",
        (task_id, group_id)
    )
    if not task:
        return {'success': False, 'error': 'Task not found'}

    execute_query(
        "DELETE FROM tasks WHERE task_id = %s AND group_id = %s",
        (task_id, group_id)
    )
    return {'success': True}


def update_task(group_id, task_id, updates):
    task = execute_one(
        "SELECT task_id FROM tasks WHERE task_id = %s AND group_id = %s",
        (task_id, group_id)
    )
    if not task:
        return {'success': False, 'error': 'Task not found'}

    allowed = ['title', 'description', 'category',
               'assigned_to', 'priority', 'due_date']
    sets    = []
    values  = []

    for key, val in updates.items():
        if key in allowed:
            sets.append(f"{key} = %s")
            values.append(val)

    if not sets:
        return {'success': False, 'error': 'No valid fields to update'}

    values += [task_id, group_id]
    execute_query(
        f"UPDATE tasks SET {', '.join(sets)} WHERE task_id = %s AND group_id = %s",
        tuple(values)
    )
    return {'success': True}


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
        if cat not in by_cat:
            by_cat[cat] = {'total': 0, 'completed': 0}
        by_cat[cat]['total']     += 1
        by_cat[cat]['completed'] += 1 if task['completed'] else 0

        person = task.get('assigned_to', 'Unassigned')
        if person not in by_person:
            by_person[person] = {'total': 0, 'completed': 0}
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
    default_tasks = [
        # Documents
        {'title': 'Collect Aadhaar/ID copies',   'description': 'Scan and share with group',       'category': 'documents',  'priority': 'high'},
        {'title': 'Apply for travel insurance',   'description': f'Coverage for {duration} days',   'category': 'documents',  'priority': 'medium'},
        {'title': 'Check passport validity',      'description': 'Must be valid for 6 months',      'category': 'documents',  'priority': 'high'},
        # Bookings
        {'title': f'Book flights to {destination}',  'description': 'Compare prices on MakeMyTrip', 'category': 'bookings',   'priority': 'high'},
        {'title': f'Book hotel in {destination}',    'description': f'{duration} nights stay',       'category': 'bookings',   'priority': 'high'},
        {'title': 'Book airport transfers',           'description': 'Cab/shuttle to airport',        'category': 'bookings',   'priority': 'medium'},
        {'title': 'Reserve activities/experiences',   'description': 'Book popular spots in advance', 'category': 'bookings',   'priority': 'medium'},
        # Packing
        {'title': 'Pack clothes',       'description': f'Pack for {duration} days',    'category': 'packing',    'priority': 'medium'},
        {'title': 'Pack medications',   'description': 'First aid kit and personal meds', 'category': 'packing', 'priority': 'high'},
        {'title': 'Charge all devices', 'description': 'Phone, camera, power bank',    'category': 'packing',    'priority': 'low'},
        {'title': 'Pack adapters',      'description': 'Universal travel adapter',      'category': 'packing',    'priority': 'low'},
        # Activities
        {'title': f'Research top spots in {destination}', 'description': 'Make a list of must-visits', 'category': 'activities', 'priority': 'medium'},
        {'title': 'Plan day-by-day itinerary',             'description': 'Use PackVote AI itinerary',  'category': 'activities', 'priority': 'medium'},
        {'title': 'Find local food recommendations',       'description': 'Best restaurants and street food', 'category': 'activities', 'priority': 'low'},
    ]

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