from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

from database import init_db
from voting import VotingEngine, create_group, get_group, submit_vote, get_results
from recommender import RecommendationEngine
from apis import TravelAPI
from auth import register_user, login_user, get_user, update_preferences
from expenses import add_expense, get_expenses, delete_expense, get_expense_stats
from planner import add_task, get_tasks, toggle_task, delete_task, update_task, generate_default_tasks

app = Flask(__name__)
CORS(app)

recommender = RecommendationEngine()
travel_api  = TravelAPI()

# ── Init database on startup ──────────────────────────────────────────────
init_db()

# ── Status ────────────────────────────────────────────────────────────────
@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({
        'status':   'PackVote backend running!',
        'version':  '3.0',
        'database': 'Railway MySQL'
    })

# ══════════════════════════════════════════════════════════════════════════
# AUTH ROUTES
# ══════════════════════════════════════════════════════════════════════════

@app.route('/api/auth/register', methods=['POST'])
def register():
    data     = request.json
    name     = data.get('name',     '').strip()
    dob      = data.get('dob',      '')
    email    = data.get('email',    '').strip().lower()
    phone    = data.get('phone',    '').strip()
    password = data.get('password', '')
    travel_preferences = data.get('travel_preferences', {})

    if not name:
        return jsonify({'success': False, 'error': 'Name is required'}), 400
    if not dob:
        return jsonify({'success': False, 'error': 'Date of birth is required'}), 400
    if not email or '@' not in email:
        return jsonify({'success': False, 'error': 'Valid email is required'}), 400
    if not phone or len(phone) < 10:
        return jsonify({'success': False, 'error': 'Valid phone number is required'}), 400
    if not password or len(password) < 6:
        return jsonify({'success': False, 'error': 'Password must be at least 6 characters'}), 400

    result = register_user(name, dob, email, phone, password, travel_preferences)
    if result['success']:
        return jsonify(result), 201
    return jsonify(result), 400


@app.route('/api/auth/login', methods=['POST'])
def login():
    data     = request.json
    email    = data.get('email',    '').strip().lower()
    password = data.get('password', '')

    if not email or not password:
        return jsonify({'success': False, 'error': 'Email and password required'}), 400

    result = login_user(email, password)
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 401


@app.route('/api/auth/user/<user_id>', methods=['GET'])
def get_user_profile(user_id):
    user = get_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)


@app.route('/api/auth/preferences/<user_id>', methods=['PUT'])
def update_user_preferences(user_id):
    data   = request.json
    result = update_preferences(user_id, data.get('travel_preferences', {}))
    return jsonify(result)

# ══════════════════════════════════════════════════════════════════════════
# GROUP ROUTES
# ══════════════════════════════════════════════════════════════════════════

@app.route('/api/group/create', methods=['POST'])
def create_group_route():
    data       = request.json
    group_name = data.get('group_name', 'My Travel Group')
    members    = data.get('members', [])
    user_id    = data.get('user_id', '')

    result = create_group(group_name, members, user_id)
    return jsonify(result)


@app.route('/api/group/<group_id>', methods=['GET'])
def get_group_route(group_id):
    group = get_group(group_id)
    if not group:
        return jsonify({'error': 'Group not found'}), 404
    return jsonify(group)

# ══════════════════════════════════════════════════════════════════════════
# VOTE ROUTES
# ══════════════════════════════════════════════════════════════════════════

@app.route('/api/vote/submit', methods=['POST'])
def submit_vote_route():
    data        = request.json
    group_id    = data.get('group_id')
    user_name   = data.get('user_name')
    preferences = data.get('preferences', {})

    if not group_id or not user_name:
        return jsonify({'error': 'Group ID and user name required'}), 400

    result = submit_vote(group_id, user_name, preferences)
    return jsonify(result)


@app.route('/api/vote/results/<group_id>', methods=['GET'])
def get_results_route(group_id):
    data = get_results(group_id)
    if 'error' in data:
        return jsonify(data), 400

    # Add recommendations
    recommendations = recommender.get_recommendations(data['consensus'])
    data['recommendations'] = recommendations

    return jsonify(data)

# ══════════════════════════════════════════════════════════════════════════
# ITINERARY ROUTES
# ══════════════════════════════════════════════════════════════════════════

@app.route('/api/itinerary/generate', methods=['POST'])
def generate_itinerary():
    data         = request.json
    destination  = data.get('destination')
    duration     = data.get('duration', 7)
    budget       = data.get('budget', 'medium')
    travel_style = data.get('travel_style', ['culture'])
    month        = data.get('month', 'December')
    group_id     = data.get('group_id', '')

    weather       = travel_api.get_weather(destination)
    places        = travel_api.get_places(destination, travel_style)
    cost_estimate = travel_api.estimate_cost(destination, duration, budget)

    itinerary = {
        'destination':    destination,
        'duration':       duration,
        'budget':         budget,
        'month':          month,
        'weather':        weather,
        'estimated_cost': cost_estimate,
        'days':           build_day_plan(places, duration),
        'generated_at':   datetime.now().isoformat()
    }

    return jsonify({'success': True, 'itinerary': itinerary})


@app.route('/api/places/search', methods=['GET'])
def search_places():
    query   = request.args.get('q', '')
    results = travel_api.search_destination(query)
    return jsonify({'results': results})


@app.route('/api/weather/<destination>', methods=['GET'])
def get_weather(destination):
    weather = travel_api.get_weather(destination)
    return jsonify(weather)

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

    result = add_expense(group_id, paid_by, amount,
                         description, category,
                         split_among, split_type)
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
        category    = data.get('category',    'other'),
        assigned_to = data.get('assigned_to', 'Unassigned'),
        priority    = data.get('priority',    'medium'),
        due_date    = data.get('due_date',    '')
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

# ── Helpers ───────────────────────────────────────────────────────────────

def build_day_plan(places, duration):
    days        = []
    place_index = 0
    all_places  = places.get('attractions', []) + places.get('restaurants', [])

    for day_num in range(1, duration + 1):
        day_places = []
        for _ in range(3):
            if place_index < len(all_places):
                day_places.append(all_places[place_index])
                place_index += 1
        days.append({
            'day':        day_num,
            'title':      f'Day {day_num}',
            'activities': day_places
        })
    return days

# ── Run ───────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("🌍 PackVote backend starting...")
    print("📍 Running at: http://127.0.0.1:5000")
    print("🗄️  Database: Railway MySQL")
    app.run(debug=True, port=5000)