import hashlib
import uuid
from datetime import datetime
from database import execute_query, execute_one

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(name, dob, email, phone, password, travel_preferences={}):
    # Check duplicate email
    existing_email = execute_one(
        "SELECT user_id FROM users WHERE email = %s", (email,)
    )
    if existing_email:
        return {'success': False, 'error': 'Email already registered'}

    # Check duplicate phone
    existing_phone = execute_one(
        "SELECT user_id FROM users WHERE phone = %s", (phone,)
    )
    if existing_phone:
        return {'success': False, 'error': 'Phone number already registered'}

    user_id = str(uuid.uuid4())[:8]
    token   = str(uuid.uuid4())

    # Insert user
    execute_query("""
        INSERT INTO users (user_id, name, email, phone, dob, password, token, created_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (user_id, name, email, phone, dob,
          hash_password(password), token,
          datetime.now()))

    # Insert preferences
    budget        = travel_preferences.get('budget', 'medium')
    trip_duration = travel_preferences.get('trip_duration', 7)
    execute_query("""
        INSERT INTO user_preferences (user_id, budget, trip_duration)
        VALUES (%s, %s, %s)
    """, (user_id, budget, trip_duration))

    # Insert travel styles
    for style in travel_preferences.get('travel_styles', []):
        execute_query("""
            INSERT INTO user_travel_styles (user_id, style)
            VALUES (%s, %s)
        """, (user_id, style))

    # Insert fav destinations
    for dest in travel_preferences.get('fav_destinations', []):
        execute_query("""
            INSERT INTO user_fav_destinations (user_id, destination)
            VALUES (%s, %s)
        """, (user_id, dest))

    return {
        'success':  True,
        'user_id':  user_id,
        'name':     name,
        'dob':      dob,
        'email':    email,
        'phone':    phone,
        'token':    token,
        'travel_preferences': {
            'budget':           budget,
            'trip_duration':    trip_duration,
            'travel_styles':    travel_preferences.get('travel_styles', []),
            'fav_destinations': travel_preferences.get('fav_destinations', [])
        }
    }

def login_user(email, password):
    user = execute_one(
        "SELECT * FROM users WHERE email = %s AND password = %s",
        (email, hash_password(password))
    )
    if not user:
        return {'success': False, 'error': 'Invalid email or password'}

    # Refresh token
    new_token = str(uuid.uuid4())
    execute_query(
        "UPDATE users SET token = %s WHERE user_id = %s",
        (new_token, user['user_id'])
    )

    # Get preferences
    prefs  = execute_one(
        "SELECT * FROM user_preferences WHERE user_id = %s",
        (user['user_id'],)
    )
    styles = execute_query(
        "SELECT style FROM user_travel_styles WHERE user_id = %s",
        (user['user_id'],), fetch=True
    )
    dests  = execute_query(
        "SELECT destination FROM user_fav_destinations WHERE user_id = %s",
        (user['user_id'],), fetch=True
    )

    # Get groups
    groups = execute_query("""
        SELECT gm.group_id, gt.name as group_name, gm.joined_at
        FROM group_members gm
        JOIN groups_table gt ON gm.group_id = gt.group_id
        WHERE gm.member_name = %s
    """, (user['name'],), fetch=True) or []

    return {
        'success': True,
        'user_id': user['user_id'],
        'name':    user['name'],
        'dob':     user['dob'],
        'email':   user['email'],
        'phone':   user['phone'],
        'token':   new_token,
        'groups':  [{'group_id': g['group_id'], 'group_name': g['group_name'], 'joined_at': str(g['joined_at'])} for g in groups],
        'travel_preferences': {
            'budget':           prefs['budget']        if prefs else 'medium',
            'trip_duration':    prefs['trip_duration'] if prefs else 7,
            'travel_styles':    [s['style']       for s in (styles or [])],
            'fav_destinations': [d['destination'] for d in (dests  or [])]
        }
    }

def get_user(user_id):
    user = execute_one(
        "SELECT * FROM users WHERE user_id = %s", (user_id,)
    )
    if not user:
        return None

    prefs  = execute_one(
        "SELECT * FROM user_preferences WHERE user_id = %s", (user_id,)
    )
    styles = execute_query(
        "SELECT style FROM user_travel_styles WHERE user_id = %s",
        (user_id,), fetch=True
    )
    dests  = execute_query(
        "SELECT destination FROM user_fav_destinations WHERE user_id = %s",
        (user_id,), fetch=True
    )
    groups = execute_query("""
        SELECT gm.group_id, gt.name as group_name, gm.joined_at
        FROM group_members gm
        JOIN groups_table gt ON gm.group_id = gt.group_id
        WHERE gm.member_name = %s
    """, (user['name'],), fetch=True) or []

    return {
        'user_id': user_id,
        'name':    user['name'],
        'dob':     user['dob'],
        'email':   user['email'],
        'phone':   user['phone'],
        'groups':  [{'group_id': g['group_id'], 'group_name': g['group_name'], 'joined_at': str(g['joined_at'])} for g in groups],
        'travel_preferences': {
            'budget':           prefs['budget']        if prefs else 'medium',
            'trip_duration':    prefs['trip_duration'] if prefs else 7,
            'travel_styles':    [s['style']       for s in (styles or [])],
            'fav_destinations': [d['destination'] for d in (dests  or [])]
        }
    }

def update_preferences(user_id, travel_preferences):
    user = execute_one("SELECT user_id FROM users WHERE user_id = %s", (user_id,))
    if not user:
        return {'success': False, 'error': 'User not found'}

    # Update preferences
    execute_query("""
        INSERT INTO user_preferences (user_id, budget, trip_duration)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
        budget = VALUES(budget),
        trip_duration = VALUES(trip_duration)
    """, (user_id,
          travel_preferences.get('budget', 'medium'),
          travel_preferences.get('trip_duration', 7)))

    # Replace travel styles
    execute_query(
        "DELETE FROM user_travel_styles WHERE user_id = %s", (user_id,)
    )
    for style in travel_preferences.get('travel_styles', []):
        execute_query(
            "INSERT INTO user_travel_styles (user_id, style) VALUES (%s, %s)",
            (user_id, style)
        )

    # Replace fav destinations
    execute_query(
        "DELETE FROM user_fav_destinations WHERE user_id = %s", (user_id,)
    )
    for dest in travel_preferences.get('fav_destinations', []):
        execute_query(
            "INSERT INTO user_fav_destinations (user_id, destination) VALUES (%s, %s)",
            (user_id, dest)
        )

    return {'success': True}

def add_group_to_user(user_id, group_id, group_name):
    # Groups are linked via group_members table
    # This is now handled in voting.py when creating groups
    pass