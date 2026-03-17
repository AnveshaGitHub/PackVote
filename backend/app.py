from expenses import add_expense, get_expenses, delete_expense, get_expense_stats
from planner import add_task, get_tasks, toggle_task, delete_task, update_task, generate_default_tasks
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime

from voting import VotingEngine
from recommender import RecommendationEngine
from apis import TravelAPI
from auth import (register_user, login_user, get_user,
                  add_group_to_user, update_preferences)

app = Flask(__name__)
CORS(app)

# ── paths ───────────────────────────────────────────────

BASE_DIR      = os.path.dirname(__file__)
DATA_DIR      = os.path.join(BASE_DIR, 'data')
FRONTEND_DIR  = os.path.join(BASE_DIR, '..', 'frontend')

VOTES_FILE       = os.path.join(DATA_DIR, 'votes.json')
ITINERARIES_FILE = os.path.join(DATA_DIR, 'itineraries.json')

voting_engine = VotingEngine()
recommender   = RecommendationEngine()
travel_api    = TravelAPI()

# ── helpers ─────────────────────────────────────────────

def load_json(filepath, default):
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return default

def save_json(filepath, data):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

# ── frontend routes (SERVE HTML) ───────────────────────

@app.route('/')
def home():
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route('/login')
def login_page():
    return send_from_directory(FRONTEND_DIR, 'login.html')

@app.route('/register')
def register_page():
    return send_from_directory(FRONTEND_DIR, 'register.html')

@app.route('/dashboard')
def dashboard_page():
    return send_from_directory(FRONTEND_DIR, 'dashboard.html')

@app.route('/vote')
def vote_page():
    return send_from_directory(FRONTEND_DIR, 'vote.html')

@app.route('/results')
def results_page():
    return send_from_directory(FRONTEND_DIR, 'results.html')

# ── status ─────────────────────────────────────────────

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({'status': 'Triply backend running!', 'version': '2.0'})

# ═══════════════════════════════════════════════════════
# AUTH ROUTES
# ═══════════════════════════════════════════════════════

@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.json

    name     = data.get('name', '').strip()
    dob      = data.get('dob', '')
    email    = data.get('email', '').strip().lower()
    phone    = data.get('phone', '').strip()
    password = data.get('password', '')
    travel_preferences = data.get('travel_preferences', {})

    if not name:
        return jsonify({'success': False, 'error': 'Name is required'}), 400

    if not dob:
        return jsonify({'success': False, 'error': 'Date of birth required'}), 400

    if not email or '@' not in email:
        return jsonify({'success': False, 'error': 'Valid email required'}), 400

    if not phone or len(phone) < 10:
        return jsonify({'success': False, 'error': 'Valid phone required'}), 400

    if not password or len(password) < 6:
        return jsonify({'success': False, 'error': 'Password must be 6+ chars'}), 400

    result = register_user(name, dob, email, phone, password, travel_preferences)

    if result['success']:
        return jsonify(result), 201

    return jsonify(result), 400


@app.route('/api/auth/login', methods=['POST'])
def login():
    data     = request.json
    email    = data.get('email', '').strip().lower()
    password = data.get('password', '')

    if not email or not password:
        return jsonify({'success': False, 'error': 'Email and password required'}), 400

    result = login_user(email, password)

    if result['success']:
        return jsonify(result)

    return jsonify(result), 401


@app.route('/api/auth/user/<user_id>', methods=['GET'])
def get_user_profile(user_id):

    user = get_user(user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(user)


@app.route('/api/auth/preferences/<user_id>', methods=['PUT'])
def update_user_preferences(user_id):

    data = request.json
    result = update_preferences(user_id, data.get('travel_preferences', {}))

    return jsonify(result)

# ═══════════════════════════════════════════════════════
# GROUP ROUTES
# ═══════════════════════════════════════════════════════

@app.route('/api/group/create', methods=['POST'])
def create_group():

    data = request.json

    group_name = data.get('group_name', 'My Travel Group')
    members    = data.get('members', [])
    user_id    = data.get('user_id', '')

    groups   = load_json(VOTES_FILE, {'groups': {}})
    group_id = f"group_{datetime.now().strftime('%Y%m%d%H%M%S')}"

    groups['groups'][group_id] = {
        'name': group_name,
        'members': members,
        'created_by': user_id,
        'votes': {},
        'created_at': datetime.now().isoformat()
    }

    save_json(VOTES_FILE, groups)

    if user_id:
        add_group_to_user(user_id, group_id, group_name)

    return jsonify({
        'success': True,
        'group_id': group_id,
        'group_name': group_name
    })


@app.route('/api/group/<group_id>', methods=['GET'])
def get_group(group_id):

    groups = load_json(VOTES_FILE, {'groups': {}})

    if group_id not in groups['groups']:
        return jsonify({'error': 'Group not found'}), 404

    group = groups['groups'][group_id]

    return jsonify({
        'group_id': group_id,
        'name': group['name'],
        'members': group['members'],
        'total_votes': len(group.get('votes', {})),
        'created_at': group['created_at']
    })

# ═══════════════════════════════════════════════════════
# VOTE ROUTES
# ═══════════════════════════════════════════════════════

@app.route('/api/vote/submit', methods=['POST'])
def submit_vote():

    data = request.json

    group_id    = data.get('group_id')
    user_name   = data.get('user_name')
    preferences = data.get('preferences', {})

    groups = load_json(VOTES_FILE, {'groups': {}})

    if group_id not in groups['groups']:
        return jsonify({'error': 'Group not found'}), 404

    groups['groups'][group_id]['votes'][user_name] = {
        'preferences': preferences,
        'submitted_at': datetime.now().isoformat()
    }

    save_json(VOTES_FILE, groups)

    return jsonify({
        'success': True,
        'message': f'Vote recorded for {user_name}'
    })


@app.route('/api/vote/results/<group_id>', methods=['GET'])
def get_results(group_id):

    groups = load_json(VOTES_FILE, {'groups': {}})

    if group_id not in groups['groups']:
        return jsonify({'error': 'Group not found'}), 404

    group = groups['groups'][group_id]
    votes = group.get('votes', {})

    if not votes:
        return jsonify({'error': 'No votes yet'}), 400

    consensus       = voting_engine.calculate_consensus(votes)
    recommendations = recommender.get_recommendations(consensus)

    return jsonify({
        'group_id': group_id,
        'group_name': group['name'],
        'total_votes': len(votes),
        'consensus': consensus,
        'recommendations': recommendations
    })

# ═══════════════════════════════════════════════════════
# ITINERARY ROUTES
# ═══════════════════════════════════════════════════════

@app.route('/api/itinerary/generate', methods=['POST'])
def generate_itinerary():

    data = request.json

    destination  = data.get('destination')
    duration     = data.get('duration', 7)
    budget       = data.get('budget', 'medium')
    travel_style = data.get('travel_style', ['culture'])
    month        = data.get('month', 'December')

    weather       = travel_api.get_weather(destination)
    places        = travel_api.get_places(destination, travel_style)
    cost_estimate = travel_api.estimate_cost(destination, duration, budget)

    itinerary = {
        'destination': destination,
        'duration': duration,
        'budget': budget,
        'month': month,
        'weather': weather,
        'estimated_cost': cost_estimate,
        'days': build_day_plan(places, duration),
        'generated_at': datetime.now().isoformat()
    }

    itineraries = load_json(ITINERARIES_FILE, {'itineraries': []})
    itineraries['itineraries'].append(itinerary)

    save_json(ITINERARIES_FILE, itineraries)

    return jsonify({
        'success': True,
        'itinerary': itinerary
    })


@app.route('/api/itinerary/user/<user_id>', methods=['GET'])
def get_user_itineraries(user_id):

    itineraries = load_json(ITINERARIES_FILE, {'itineraries': []})

    user_its = [
        i for i in itineraries['itineraries']
        if i.get('user_id') == user_id
    ]

    return jsonify({'itineraries': user_its})

# ── helpers ───────────────────────────────────────────

def build_day_plan(places, duration):

    days = []

    place_index = 0
    all_places = places.get('attractions', []) + places.get('restaurants', [])

    for day_num in range(1, duration + 1):

        day_places = []

        for _ in range(3):
            if place_index < len(all_places):
                day_places.append(all_places[place_index])
                place_index += 1

        days.append({
            'day': day_num,
            'title': f'Day {day_num}',
            'activities': day_places
        })

    return days

# ── run ───────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════
# EXPENSE ROUTES
# ══════════════════════════════════════════════════════════════════════════

@app.route('/api/expenses/<group_id>', methods=['GET'])
def get_group_expenses(group_id):
    return jsonify(get_expenses(group_id))

@app.route('/api/expenses/add', methods=['POST'])
def add_group_expense():
    data        = request.json
    group_id    = data.get('group_id')
    paid_by     = data.get('paid_by')
    amount      = data.get('amount')
    description = data.get('description')
    category    = data.get('category', 'other')
    split_among = data.get('split_among', [])
    split_type  = data.get('split_type', 'equal')

    if not all([group_id, paid_by, amount, description, split_among]):
        return jsonify({'success': False, 'error': 'Missing required fields'}), 400

    result = add_expense(group_id, paid_by, amount, description, category, split_among, split_type)
    return jsonify(result)

@app.route('/api/expenses/delete/<group_id>/<expense_id>', methods=['DELETE'])
def delete_group_expense(group_id, expense_id):
    return jsonify(delete_expense(group_id, expense_id))

@app.route('/api/expenses/stats/<group_id>', methods=['GET'])
def expense_stats(group_id):
    return jsonify(get_expense_stats(group_id))

# ══════════════════════════════════════════════════════════════════════════
# PLANNER ROUTES
# ══════════════════════════════════════════════════════════════════════════

@app.route('/api/planner/<group_id>', methods=['GET'])
def get_group_tasks(group_id):
    return jsonify(get_tasks(group_id))

@app.route('/api/planner/add', methods=['POST'])
def add_group_task():
    data     = request.json
    group_id = data.get('group_id')
    title    = data.get('title', '').strip()
    if not group_id or not title:
        return jsonify({'success': False, 'error': 'Group ID and title required'}), 400
    result = add_task(
        group_id    = group_id,
        title       = title,
        description = data.get('description', ''),
        category    = data.get('category', 'other'),
        assigned_to = data.get('assigned_to', 'Unassigned'),
        priority    = data.get('priority', 'medium'),
        due_date    = data.get('due_date', '')
    )
    return jsonify(result)

@app.route('/api/planner/toggle/<group_id>/<task_id>', methods=['PUT'])
def toggle_group_task(group_id, task_id):
    return jsonify(toggle_task(group_id, task_id))

@app.route('/api/planner/delete/<group_id>/<task_id>', methods=['DELETE'])
def delete_group_task(group_id, task_id):
    return jsonify(delete_task(group_id, task_id))

@app.route('/api/planner/generate', methods=['POST'])
def generate_tasks():
    data        = request.json
    group_id    = data.get('group_id')
    destination = data.get('destination', 'your destination')
    duration    = data.get('duration', 7)
    members     = data.get('members', [])
    if not group_id:
        return jsonify({'success': False, 'error': 'Group ID required'}), 400
    result = generate_default_tasks(group_id, destination, duration, members)
    return jsonify(result)

if __name__ == '__main__':

    print("🌍 Triply backend starting...")
    print("📍 Running at: http://127.0.0.1:5000")

    app.run(debug=True, port=5000)

