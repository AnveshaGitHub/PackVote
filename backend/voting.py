from collections import defaultdict


class VotingEngine:
    def calculate_consensus(self, votes: dict) -> dict:
        destination_scores = defaultdict(float)
        budget_votes       = defaultdict(int)
        style_votes        = defaultdict(int)
        duration_votes     = []
        month_votes        = defaultdict(int)

        total_voters = len(votes)

        for user, vote_data in votes.items():
            prefs = vote_data.get('preferences', {})

            destinations = prefs.get('destinations', [])
            n = len(destinations)
            for rank, dest in enumerate(destinations):
                points = n - rank
                destination_scores[dest] += points

            budget = prefs.get('budget', 'medium')
            budget_votes[budget] += 1

            for style in prefs.get('travel_style', []):
                style_votes[style] += 1

            duration_votes.append(prefs.get('duration', 7))
            month_votes[prefs.get('month', 'June')] += 1

        sorted_dests = sorted(destination_scores.items(), key=lambda x: x[1], reverse=True)
        top_destinations = [
            {'destination': d, 'score': s, 'percentage': round(s / max(destination_scores.values()) * 100)}
            for d, s in sorted_dests[:5]
        ]

        consensus_budget = max(budget_votes, key=budget_votes.get)
        sorted_styles = sorted(style_votes.items(), key=lambda x: x[1], reverse=True)
        top_styles = [s for s, _ in sorted_styles[:3]]
        avg_duration = round(sum(duration_votes) / len(duration_votes)) if duration_votes else 7
        consensus_month = max(month_votes, key=month_votes.get)
        conflicts = self.detect_conflicts(votes, consensus_budget, avg_duration)

        return {
            'top_destinations': top_destinations,
            'winner': top_destinations[0]['destination'] if top_destinations else None,
            'consensus_budget': consensus_budget,
            'top_styles': top_styles,
            'avg_duration': avg_duration,
            'consensus_month': consensus_month,
            'total_voters': total_voters,
            'conflicts': conflicts,
            'score_breakdown': dict(destination_scores)
        }

    def detect_conflicts(self, votes: dict, consensus_budget: str, avg_duration: int) -> list:
        conflicts = []
        budget_map = {'low': 1, 'medium': 2, 'high': 3, 'luxury': 4}
        consensus_level = budget_map.get(consensus_budget, 2)

        for user, vote_data in votes.items():
            prefs = vote_data.get('preferences', {})
            user_budget = prefs.get('budget', 'medium')
            user_level = budget_map.get(user_budget, 2)
            if abs(user_level - consensus_level) >= 2:
                conflicts.append({
                    'type': 'budget',
                    'message': f'{user} prefers {user_budget} vs group consensus {consensus_budget}',
                    'severity': 'high'
                })

        for user, vote_data in votes.items():
            prefs = vote_data.get('preferences', {})
            user_dur = prefs.get('duration', 7)
            if abs(user_dur - avg_duration) > 3:
                conflicts.append({
                    'type': 'duration',
                    'message': f'{user} wants {user_dur} days vs group average {avg_duration} days',
                    'severity': 'medium'
                })

        return conflicts

    def get_vote_summary(self, votes: dict) -> dict:
        return {
            'total_voters': len(votes),
            'voters': list(votes.keys()),
            'all_destinations': list({
                dest
                for v in votes.values()
                for dest in v.get('preferences', {}).get('destinations', [])
            })
        }