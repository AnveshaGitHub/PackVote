from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime

from database import init_db, get_connection
from voting import VotingEngine
from recommender import RecommendationEngine
from apis import TravelAPI
from auth import register_user, login_user, get_user, update_preferences, add_group_to_user
from expenses import add_expense, get_expenses, delete_expense, get_expense_stats
from planner import add_task, get_tasks, toggle_task, delete_task, update_task, generate_default_tasks
from email_service import send_join_confirmation, send_voting_open, send_results_ready

app = Flask(__name__)
CORS(app)

BASE_DIR         = os.path.dirname(__file__)
DATA_DIR         = os.path.join(BASE_DIR, 'data')
FRONTEND_DIR     = os.path.join(BASE_DIR, '..', 'frontend')
ITINERARIES_FILE = os.path.join(DATA_DIR, 'itineraries.json')

voting_engine = VotingEngine()
recommender   = RecommendationEngine()
travel_api    = TravelAPI()

init_db()

# ── helpers ──────────────────────────────────────────────────────────────

def load_json(filepath, default):
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return default

def save_json(filepath, data):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

# ── frontend routes ───────────────────────────────────────────────────────

@app.route('/frontend/<path:filename>')
def serve_static(filename):
    return send_from_directory(FRONTEND_DIR, filename)

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

# ── status ────────────────────────────────────────────────────────────────

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({'status': 'PackVote backend running!', 'version': '2.0'})

# ══════════════════════════════════════════════════════════════════════════
# AUTH ROUTES
# ══════════════════════════════════════════════════════════════════════════

@app.route('/api/auth/register', methods=['POST'])
def register():
    data               = request.json
    name               = data.get('name', '').strip()
    dob                = data.get('dob', '')
    email              = data.get('email', '').strip().lower()
    phone              = data.get('phone', '').strip()
    password           = data.get('password', '')
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
        return jsonify({'success': False, 'error': 'Password must be at least 6 characters'}), 400

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


# ✅ FIXED: removed COUNT(DISTINCT m2.id) and COUNT(DISTINCT v.id)
@app.route('/api/auth/user/<user_id>/groups', methods=['GET'])
def get_user_groups(user_id):
    try:
        conn = get_connection()
        with conn.cursor(dictionary=True) as cur:
            cur.execute("SELECT name FROM users WHERE user_id = %s", (user_id,))
            user_row = cur.fetchone()
            if not user_row:
                return jsonify({'groups': []}), 404
            user_name = user_row['name']

            cur.execute("""
                SELECT g.group_id, g.name as group_name, g.created_at
                FROM members m
                JOIN groups_table g ON g.group_id = m.group_id
                WHERE m.name = %s
                ORDER BY g.created_at DESC
            """, (user_name,))
            rows = cur.fetchall() or []
        conn.close()

        groups = [{
            'group_id':   r['group_id'],
            'group_name': r['group_name'],
            'created_at': str(r['created_at']),
        } for r in rows]

        return jsonify({'groups': groups})

    except Exception as e:
        print(f"get_user_groups error: {e}")
        return jsonify({'groups': [], 'error': str(e)}), 500


@app.route('/api/auth/preferences/<user_id>', methods=['PUT'])
def update_user_preferences(user_id):
    data   = request.json
    result = update_preferences(user_id, data.get('travel_preferences', {}))
    return jsonify(result)

# ══════════════════════════════════════════════════════════════════════════
# GROUP ROUTES
# ══════════════════════════════════════════════════════════════════════════

@app.route('/api/group/create', methods=['POST'])
def create_group():
    data       = request.json
    group_name = data.get('group_name', 'My Travel Group')
    members    = data.get('members', [])
    user_id    = data.get('user_id', '')
    group_id   = f"group_{datetime.now().strftime('%Y%m%d%H%M%S')}"

    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO groups_table (group_id, name, created_by) VALUES (%s, %s, %s)",
                (group_id, group_name, user_id or None)
            )
            for member in members:
                cur.execute(
                    "INSERT INTO members (group_id, name) VALUES (%s, %s)",
                    (group_id, member)
                )
        conn.commit()
        conn.close()

        if user_id:
            add_group_to_user(user_id, group_id, group_name)

        return jsonify({'success': True, 'group_id': group_id, 'group_name': group_name})

    except Exception as e:
        print(f"create_group error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/group/join', methods=['POST'])
def join_group():
    data     = request.json
    group_id = data.get('group_id', '').strip()
    member   = data.get('member_name', '').strip()
    email    = data.get('email', '').strip()

    if not group_id or not member:
        return jsonify({'success': False, 'error': 'Group ID and name required'}), 400

    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM groups_table WHERE group_id = %s", (group_id,))
            group = cur.fetchone()
            if not group:
                return jsonify({'success': False, 'error': 'Group not found'}), 404

            cur.execute(
                "SELECT id FROM members WHERE group_id = %s AND name = %s",
                (group_id, member)
            )
            if cur.fetchone():
                return jsonify({'success': False, 'error': 'You are already in this group'}), 400

            cur.execute(
                "INSERT INTO members (group_id, name, email) VALUES (%s, %s, %s)",
                (group_id, member, email)
            )
        conn.commit()
        conn.close()

        try:
            send_join_confirmation(email, member, group['name'], group_id)
        except Exception as mail_err:
            print(f"Email error (non-fatal): {mail_err}")

        return jsonify({
            'success':    True,
            'group_id':   group_id,
            'group_name': group['name'],
            'message':    f'Welcome to {group["name"]}!'
        })

    except Exception as e:
        print(f"join_group error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/group/<group_id>', methods=['GET'])
def get_group(group_id):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM groups_table WHERE group_id = %s", (group_id,))
            group = cur.fetchone()
            if not group:
                return jsonify({'error': 'Group not found'}), 404

            cur.execute("SELECT name FROM members WHERE group_id = %s", (group_id,))
            members = [r['name'] for r in cur.fetchall()]

            cur.execute("SELECT DISTINCT user_name FROM votes WHERE group_id = %s", (group_id,))
            voters = [r['user_name'] for r in cur.fetchall()]

            cur.execute("SELECT COUNT(*) as cnt FROM votes WHERE group_id = %s", (group_id,))
            vote_count = cur.fetchone()['cnt']

        conn.close()
        return jsonify({
            'group_id':    group_id,
            'name':        group['name'],
            'created_by':  group.get('created_by', ''),
            'members':     members,
            'voters':      voters,
            'total_votes': vote_count,
            'created_at':  str(group['created_at'])
        })
    except Exception as e:
        print(f"get_group error: {e}")
        return jsonify({'error': str(e)}), 500

# ══════════════════════════════════════════════════════════════════════════
# DESTINATION ROUTES
# ══════════════════════════════════════════════════════════════════════════

@app.route('/api/group/<group_id>/destinations', methods=['GET'])
def get_destinations(group_id):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM destinations WHERE group_id = %s ORDER BY created_at ASC", (group_id,))
            rows = cur.fetchall()
        conn.close()
        return jsonify({'destinations': rows})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/group/<group_id>/destinations/add', methods=['POST'])
def add_destination(group_id):
    data     = request.json
    name     = data.get('name', '').strip()
    added_by = data.get('added_by', '')
    if not name:
        return jsonify({'success': False, 'error': 'Destination name required'}), 400
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM destinations WHERE group_id = %s AND LOWER(name) = LOWER(%s)", (group_id, name))
            if cur.fetchone():
                return jsonify({'success': False, 'error': 'Already added'}), 400
            cur.execute("INSERT INTO destinations (group_id, name, added_by) VALUES (%s, %s, %s)", (group_id, name, added_by))
            cur.execute("SELECT * FROM destinations WHERE group_id = %s ORDER BY created_at ASC", (group_id,))
            destinations = cur.fetchall()
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'destinations': destinations})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/group/<group_id>/destinations/remove', methods=['POST'])
def remove_destination(group_id):
    name = request.json.get('name', '').strip()
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM destinations WHERE group_id = %s AND name = %s", (group_id, name))
            cur.execute("SELECT * FROM destinations WHERE group_id = %s ORDER BY created_at ASC", (group_id,))
            destinations = cur.fetchall()
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'destinations': destinations})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/group/<group_id>/open-voting', methods=['POST'])
def open_voting(group_id):
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("UPDATE groups_table SET voting_open = TRUE WHERE group_id = %s", (group_id,))
            cur.execute("SELECT name FROM destinations WHERE group_id = %s", (group_id,))
            dest_names = [r['name'] for r in cur.fetchall()]
            cur.execute("SELECT name, email FROM members WHERE group_id = %s AND email IS NOT NULL AND email != ''", (group_id,))
            members = cur.fetchall()
            cur.execute("SELECT name FROM groups_table WHERE group_id = %s", (group_id,))
            group = cur.fetchone()
        conn.commit()
        conn.close()
        if group:
            for m in members:
                try:
                    send_voting_open(m['email'], m['name'], group['name'], dest_names)
                except Exception as mail_err:
                    print(f"Email error (non-fatal): {mail_err}")
        return jsonify({'success': True, 'message': 'Voting opened'})
    except Exception as e:
        print(f"open_voting error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

# ══════════════════════════════════════════════════════════════════════════
# VOTE ROUTES
# ══════════════════════════════════════════════════════════════════════════

@app.route('/api/vote/submit', methods=['POST'])
def submit_vote():
    import json as json_lib
    data        = request.json
    group_id    = data.get('group_id')
    user_name   = data.get('user_name')
    preferences = data.get('preferences', {})

    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT group_id FROM groups_table WHERE group_id = %s", (group_id,))
            if not cur.fetchone():
                return jsonify({'error': 'Group not found'}), 404
            cur.execute(
                """INSERT INTO votes (group_id, user_name, preferences)
                   VALUES (%s, %s, %s)
                   ON DUPLICATE KEY UPDATE
                   preferences = VALUES(preferences),
                   submitted_at = CURRENT_TIMESTAMP""",
                (group_id, user_name, json_lib.dumps(preferences))
            )
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'message': f'Vote recorded for {user_name}'})
    except Exception as e:
        print(f"submit_vote error: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/vote/results/<group_id>', methods=['GET'])
def get_results(group_id):
    import json as json_lib
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM groups_table WHERE group_id = %s", (group_id,))
            group = cur.fetchone()
            if not group:
                return jsonify({'error': 'Group not found'}), 404
            cur.execute("SELECT user_name, preferences FROM votes WHERE group_id = %s", (group_id,))
            rows = cur.fetchall()
            cur.execute("SELECT COUNT(*) as cnt FROM members WHERE group_id = %s", (group_id,))
            member_count = cur.fetchone()['cnt']
            cur.execute("SELECT name, email FROM members WHERE group_id = %s AND email IS NOT NULL AND email != ''", (group_id,))
            members_with_email = cur.fetchall()
        conn.close()

        if not rows:
            return jsonify({'error': 'No votes yet'}), 400

        votes = {}
        for row in rows:
            prefs = row['preferences']
            if isinstance(prefs, str):
                prefs = json_lib.loads(prefs)
            votes[row['user_name']] = {'preferences': prefs}

        consensus       = voting_engine.calculate_consensus(votes)
        recommendations = recommender.get_recommendations(consensus)
        winner          = consensus.get('winner', '')

        if winner and len(rows) >= member_count and member_count > 0:
            for m in members_with_email:
                try:
                    send_results_ready(m['email'], m['name'], group['name'], winner, len(rows))
                except Exception as mail_err:
                    print(f"Email error (non-fatal): {mail_err}")

        return jsonify({
            'group_id':        group_id,
            'group_name':      group['name'],
            'total_votes':     len(votes),
            'consensus':       consensus,
            'recommendations': recommendations
        })
    except Exception as e:
        print(f"get_results error: {e}")
        return jsonify({'error': str(e)}), 500

# ══════════════════════════════════════════════════════════════════════════
# WEATHER ROUTE
# ══════════════════════════════════════════════════════════════════════════

@app.route('/api/weather/<destination>', methods=['GET'])
def get_weather(destination):
    data = travel_api.get_weather(destination)
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

    itineraries = load_json(ITINERARIES_FILE, {'itineraries': []})
    itineraries['itineraries'].append(itinerary)
    save_json(ITINERARIES_FILE, itineraries)

    return jsonify({'success': True, 'itinerary': itinerary})


@app.route('/api/itinerary/user/<user_id>', methods=['GET'])
def get_user_itineraries(user_id):
    itineraries = load_json(ITINERARIES_FILE, {'itineraries': []})
    user_its    = [i for i in itineraries['itineraries'] if i.get('user_id') == user_id]
    return jsonify({'itineraries': user_its})


def build_day_plan(places, duration):
    days        = []
    place_index = 0
    all_places  = places.get('attractions', []) + places.get('restaurants', [])
    themes = [
        'Arrival & Exploration', 'Main Attractions', 'Culture & Heritage',
        'Adventure Day', 'Food & Markets', 'Leisure & Local Life', 'Departure Day'
    ]
    for day_num in range(1, duration + 1):
        day_places = []
        for _ in range(3):
            if place_index < len(all_places):
                day_places.append(all_places[place_index])
                place_index += 1
        title = themes[(day_num - 1) % len(themes)]
        days.append({'day': day_num, 'title': f'Day {day_num} — {title}', 'activities': day_places})
    return days

# ══════════════════════════════════════════════════════════════════════════
# DEEP LINKS ROUTE
# ══════════════════════════════════════════════════════════════════════════

@app.route('/api/deeplinks', methods=['POST'])
def get_deeplinks():
    data        = request.json
    destination = data.get('destination', '')
    duration    = data.get('duration', 7)
    budget      = data.get('budget', 'medium')
    if not destination:
        return jsonify({'error': 'Destination required'}), 400
    try:
        links = travel_api.get_deeplinks(destination, duration, budget)
        return jsonify({'success': True, 'links': links, 'destination': destination})
    except Exception as e:
        print(f"deeplinks error: {e}")
        return jsonify({'error': str(e)}), 500

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

# ── run ───────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("🌍 PackVote backend starting...")
    print("📍 Running at: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)