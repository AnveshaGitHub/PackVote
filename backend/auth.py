import json
import os
import hashlib
import uuid
from datetime import datetime

USERS_FILE = os.path.join(os.path.dirname(__file__), 'data', 'users.json')

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {'users': {}}

def save_users(data):
    os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
    with open(USERS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(name, dob, email, phone, password, travel_preferences={}):
    users = load_users()

    # Check duplicate email
    for uid, user in users['users'].items():
        if user['email'] == email:
            return {'success': False, 'error': 'Email already registered'}

    # Check duplicate phone
    for uid, user in users['users'].items():
        if user.get('phone') == phone:
            return {'success': False, 'error': 'Phone number already registered'}

    user_id = str(uuid.uuid4())[:8]
    token   = str(uuid.uuid4())

    users['users'][user_id] = {
        'user_id':    user_id,
        'name':       name,
        'dob':        dob,
        'email':      email,
        'phone':      phone,
        'password':   hash_password(password),
        'token':      token,
        'travel_preferences': {
            'budget':        travel_preferences.get('budget', 'medium'),
            'travel_styles': travel_preferences.get('travel_styles', []),
            'fav_destinations': travel_preferences.get('fav_destinations', []),
            'trip_duration': travel_preferences.get('trip_duration', 7)
        },
        'groups':     [],
        'created_at': datetime.now().isoformat()
    }
    save_users(users)

    return {
        'success':  True,
        'user_id':  user_id,
        'name':     name,
        'dob':      dob,
        'email':    email,
        'phone':    phone,
        'token':    token,
        'travel_preferences': users['users'][user_id]['travel_preferences']
    }

def login_user(email, password):
    users = load_users()

    for uid, user in users['users'].items():
        if user['email'] == email and user['password'] == hash_password(password):
            new_token = str(uuid.uuid4())
            user['token'] = new_token
            save_users(users)
            return {
                'success': True,
                'user_id': uid,
                'name':    user['name'],
                'dob':     user.get('dob', ''),
                'email':   user['email'],
                'phone':   user.get('phone', ''),
                'token':   new_token,
                'groups':  user.get('groups', []),
                'travel_preferences': user.get('travel_preferences', {})
            }

    return {'success': False, 'error': 'Invalid email or password'}

def get_user(user_id):
    users = load_users()
    user  = users['users'].get(user_id)
    if not user:
        return None
    return {
        'user_id': user_id,
        'name':    user['name'],
        'dob':     user.get('dob', ''),
        'email':   user['email'],
        'phone':   user.get('phone', ''),
        'groups':  user.get('groups', []),
        'travel_preferences': user.get('travel_preferences', {})
    }

def update_preferences(user_id, travel_preferences):
    users = load_users()
    if user_id not in users['users']:
        return {'success': False, 'error': 'User not found'}

    users['users'][user_id]['travel_preferences'] = {
        'budget':           travel_preferences.get('budget', 'medium'),
        'travel_styles':    travel_preferences.get('travel_styles', []),
        'fav_destinations': travel_preferences.get('fav_destinations', []),
        'trip_duration':    travel_preferences.get('trip_duration', 7)
    }
    save_users(users)
    return {'success': True}

def add_group_to_user(user_id, group_id, group_name):
    users = load_users()
    if user_id in users['users']:
        if 'groups' not in users['users'][user_id]:
            users['users'][user_id]['groups'] = []
        users['users'][user_id]['groups'].append({
            'group_id':   group_id,
            'group_name': group_name,
            'joined_at':  datetime.now().isoformat()
        })
        save_users(users)

def get_all_users_summary():
    users = load_users()
    return [
        {
            'user_id': uid,
            'name':    u['name'],
            'email':   u['email'],
            'groups':  len(u.get('groups', [])),
            'joined':  u['created_at'][:10]
        }
        for uid, u in users['users'].items()
    ]