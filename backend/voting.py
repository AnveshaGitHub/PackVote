import json
from collections import defaultdict
from datetime import datetime
from database import execute_query, execute_one

class VotingEngine:

    def calculate_consensus(self, votes_list):
        destination_scores = defaultdict(float)
        budget_votes       = defaultdict(int)
        style_votes        = defaultdict(int)
        duration_votes     = []
        month_votes        = defaultdict(int)

        total_voters = len(votes_list)

        for vote in votes_list:
            try:
                destinations = json.loads(vote.get('destinations') or '[]')
                travel_style = json.loads(vote.get('travel_style') or '[]')
            except:
                destinations = []
                travel_style = []

            budget   = vote.get('budget', 'medium')
            duration = vote.get('duration', 7)
            month    = vote.get('month', 'December')

            # Borda count
            n = len(destinations)
            for rank, dest in enumerate(destinations):
                destination_scores[dest] += (n - rank)

            budget_votes[budget] += 1

            for style in travel_style:
                style_votes[style] += 1

            duration_votes.append(duration)
            month_votes[month] += 1

        # Top destinations
        sorted_dests = sorted(
            destination_scores.items(),
            key=lambda x: x[1], reverse=True
        )

        max_score = max(destination_scores.values()) if destination_scores else 1
        top_destinations = [
            {
                'destination': d,
                'score':       s,
                'percentage':  round(s / max_score * 100)
            }
            for d, s in sorted_dests[:5]
        ]

        consensus_budget   = max(budget_votes, key=budget_votes.get) if budget_votes else 'medium'
        sorted_styles      = sorted(style_votes.items(), key=lambda x: x[1], reverse=True)
        top_styles         = [s for s, _ in sorted_styles[:3]]
        avg_duration       = round(sum(duration_votes) / len(duration_votes)) if duration_votes else 7
        consensus_month    = max(month_votes, key=month_votes.get) if month_votes else 'December'
        conflicts          = self.detect_conflicts(votes_list, consensus_budget, avg_duration)

        return {
            'top_destinations':  top_destinations,
            'winner':            top_destinations[0]['destination'] if top_destinations else None,
            'consensus_budget':  consensus_budget,
            'top_styles':        top_styles,
            'avg_duration':      avg_duration,
            'consensus_month':   consensus_month,
            'total_voters':      total_voters,
            'conflicts':         conflicts,
            'score_breakdown':   dict(destination_scores)
        }

    def detect_conflicts(self, votes_list, consensus_budget, avg_duration):
        conflicts   = []
        budget_map  = {'low': 1, 'medium': 2, 'high': 3, 'luxury': 4}
        cons_level  = budget_map.get(consensus_budget, 2)

        for vote in votes_list:
            user_name   = vote.get('user_name', 'Someone')
            user_budget = vote.get('budget', 'medium')
            user_level  = budget_map.get(user_budget, 2)
            if abs(user_level - cons_level) >= 2:
                conflicts.append({
                    'type':     'budget',
                    'message':  f'{user_name} prefers {user_budget} vs group consensus {consensus_budget}',
                    'severity': 'high'
                })

            user_dur = vote.get('duration', 7)
            if abs(user_dur - avg_duration) > 3:
                conflicts.append({
                    'type':     'duration',
                    'message':  f'{user_name} wants {user_dur} days vs group average {avg_duration} days',
                    'severity': 'medium'
                })

        return conflicts


# ── Group functions ───────────────────────────────────────────────────────

def create_group(group_name, members, user_id=''):
    group_id = f"group_{datetime.now().strftime('%Y%m%d%H%M%S')}"

    # Insert group
    execute_query("""
        INSERT INTO groups_table (group_id, name, created_by, created_at)
        VALUES (%s, %s, %s, %s)
    """, (group_id, group_name, user_id or None, datetime.now()))

    # Insert members
    for member in members:
        execute_query("""
            INSERT INTO group_members (group_id, member_name, joined_at)
            VALUES (%s, %s, %s)
        """, (group_id, member, datetime.now()))

    return {'success': True, 'group_id': group_id, 'group_name': group_name}


def get_group(group_id):
    group = execute_one(
        "SELECT * FROM groups_table WHERE group_id = %s", (group_id,)
    )
    if not group:
        return None

    members = execute_query(
        "SELECT member_name FROM group_members WHERE group_id = %s",
        (group_id,), fetch=True
    ) or []

    vote_count = execute_one(
        "SELECT COUNT(*) as cnt FROM votes WHERE group_id = %s", (group_id,)
    )

    return {
        'group_id':    group_id,
        'name':        group['name'],
        'members':     [m['member_name'] for m in members],
        'total_votes': vote_count['cnt'] if vote_count else 0,
        'created_at':  str(group['created_at'])
    }


def submit_vote(group_id, user_name, preferences):
    # Check group exists
    group = execute_one(
        "SELECT group_id FROM groups_table WHERE group_id = %s", (group_id,)
    )
    if not group:
        return {'success': False, 'error': 'Group not found'}

    destinations  = json.dumps(preferences.get('destinations', []))
    travel_style  = json.dumps(preferences.get('travel_style', []))
    budget        = preferences.get('budget', 'medium')
    duration      = preferences.get('duration', 7)
    month         = preferences.get('month', 'December')

    # Check if user already voted — update if so
    existing = execute_one(
        "SELECT id FROM votes WHERE group_id = %s AND user_name = %s",
        (group_id, user_name)
    )

    if existing:
        execute_query("""
            UPDATE votes SET
                destinations  = %s,
                budget        = %s,
                travel_style  = %s,
                duration      = %s,
                month         = %s,
                submitted_at  = %s
            WHERE group_id = %s AND user_name = %s
        """, (destinations, budget, travel_style, duration, month,
              datetime.now(), group_id, user_name))
    else:
        execute_query("""
            INSERT INTO votes
                (group_id, user_name, destinations, budget, travel_style, duration, month, submitted_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (group_id, user_name, destinations, budget, travel_style,
              duration, month, datetime.now()))

    return {'success': True, 'message': f'Vote recorded for {user_name}'}


def get_results(group_id):
    group = execute_one(
        "SELECT * FROM groups_table WHERE group_id = %s", (group_id,)
    )
    if not group:
        return {'error': 'Group not found'}

    votes = execute_query(
        "SELECT * FROM votes WHERE group_id = %s", (group_id,), fetch=True
    ) or []

    if not votes:
        return {'error': 'No votes yet'}

    engine    = VotingEngine()
    consensus = engine.calculate_consensus(votes)

    return {
        'group_id':   group_id,
        'group_name': group['name'],
        'total_votes': len(votes),
        'consensus':  consensus
    }