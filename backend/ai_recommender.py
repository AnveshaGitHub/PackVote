import anthropic
import json
from recommender import RecommendationEngine

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

class AIRecommendationEngine(RecommendationEngine):
    """
    Extends the rule-based engine with an LLM re-ranking layer.
    Falls back to rule-based if the API call fails.
    """

    def get_ai_recommendations(self, consensus: dict) -> dict:
        # Step 1: Get rule-based top 10 (wider net for LLM to re-rank)
        base_recs = self._get_base_recommendations(consensus, top_n=10)

        # Step 2: Build the prompt
        prompt = self._build_prompt(consensus, base_recs)

        # Step 3: Call Claude
        try:
            response = client.messages.create(
                model="claude-opus-4-6",
                max_tokens=1500,
                system="""You are a travel recommendation expert for Indian group travellers.
You will be given a group's travel consensus and a list of candidate destinations.
Your job is to re-rank the top 5 destinations and write a 1-sentence personalised reason
for each one explaining WHY it suits this specific group.

Respond ONLY in this JSON format (no markdown, no extra text):
{
  "recommendations": [
    {
      "destination": "...",
      "rank": 1,
      "reason": "...",
      "highlight": "one key feature e.g. Best for couples in winter"
    }
  ],
  "group_insight": "One sentence summarising what kind of travellers this group is"
}""",
                messages=[{"role": "user", "content": prompt}]
            )

            # Parse the JSON response
            raw = response.content[0].text.strip()
            ai_output = json.loads(raw)

            # Step 4: Merge AI ranking with rule-based data
            return self._merge_results(ai_output, base_recs, consensus)

        except Exception as e:
            print(f"AI layer failed, using rule-based fallback: {e}")
            # Graceful fallback to existing engine
            return {
                "recommendations": self.get_recommendations(consensus),
                "group_insight": "A group with diverse travel preferences.",
                "ai_powered": False
            }

    def _get_base_recommendations(self, consensus: dict, top_n: int) -> list:
        """Get wider pool from rule-based engine."""
        top_styles  = consensus.get('top_styles', [])
        budget      = consensus.get('consensus_budget', 'medium')
        month       = consensus.get('consensus_month', 'June')
        voted_dests = [d['destination'] for d in consensus.get('top_destinations', [])]

        scored = []
        for dest, info in self.DESTINATIONS.items():
            score = self._score_destination(dest, info, top_styles, budget, month)
            if dest in voted_dests:
                rank = voted_dests.index(dest)
                score += (len(voted_dests) - rank) * 10
            scored.append({
                'destination': dest,
                'score': round(score, 2),
                'description': info['description'],
                'avg_cost_per_day': info['avg_cost_per_day'],
                'best_months': info['best_months'],
                'tags': info['tags'],
                'budget_level': info['budget_level']
            })

        scored.sort(key=lambda x: x['score'], reverse=True)
        return scored[:top_n]

    def _build_prompt(self, consensus: dict, candidates: list) -> str:
        return f"""
GROUP CONSENSUS:
- Top voted destinations: {[d['destination'] for d in consensus.get('top_destinations', [])[:5]]}
- Budget: {consensus.get('consensus_budget')}
- Travel styles: {consensus.get('top_styles')}
- Trip duration: {consensus.get('avg_duration')} days
- Month: {consensus.get('consensus_month')}
- Total voters: {consensus.get('total_voters')}
- Conflicts: {consensus.get('conflicts', [])}

CANDIDATE DESTINATIONS (rule-based top 10):
{json.dumps([{
    'destination': r['destination'],
    'tags': r['tags'],
    'budget_level': r['budget_level'],
    'description': r['description'],
    'avg_cost_per_day_usd': r['avg_cost_per_day']
} for r in candidates], indent=2)}

Re-rank the best 5 destinations for this group. 
Consider: group conflicts, travel style overlap, budget fit, and seasonal suitability.
Write a personalised reason for each that references the GROUP's specific preferences.
"""

    def _merge_results(self, ai_output: dict, base_recs: list, consensus: dict) -> dict:
        """Merge AI ranking with existing rule-based data."""
        base_map = {r['destination']: r for r in base_recs}
        final    = []

        for item in ai_output.get('recommendations', []):
            dest = item['destination']
            base = base_map.get(dest, {})
            final.append({
                **base,                           # all original fields
                'rank':      item.get('rank'),
                'reason':    item.get('reason', ''),
                'highlight': item.get('highlight', ''),
                'ai_powered': True
            })

        return {
            'recommendations': final,
            'group_insight':   ai_output.get('group_insight', ''),
            'ai_powered':      True
        }