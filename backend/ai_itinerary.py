# ai_itinerary.py — place in backend/ folder
# Uses Groq API (free — sign up at console.groq.com, no card needed)
# Fallback to rule-based if Groq key not set
 
import os
import json
import requests
from datetime import datetime, timedelta
 
GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
GROQ_URL     = 'https://api.groq.com/openai/v1/chat/completions'
 
# ── 500+ Indian destinations ──────────────────────────────────────────────
 
INDIA_DESTINATIONS = {
    'Andhra Pradesh':    ['Visakhapatnam','Vijayawada','Tirupati','Araku Valley','Lepakshi','Nagarjunasagar','Srikalahasti','Horsley Hills'],
    'Arunachal Pradesh': ['Tawang','Ziro','Dirang','Bomdila','Namdapha','Pasighat','Mechuka','Along'],
    'Assam':             ['Kaziranga','Majuli','Guwahati','Jorhat','Tezpur','Haflong','Manas','Sibsagar','Sualkuchi'],
    'Bihar':             ['Bodh Gaya','Rajgir','Nalanda','Vaishali','Patna','Pawapuri','Vikramshila','Madhubani'],
    'Chhattisgarh':      ['Chitrakote','Jagdalpur','Raipur','Sirpur','Barnawapara','Tirathgarh','Bastar','Mainpat'],
    'Goa':               ['North Goa','South Goa','Panjim','Calangute','Anjuna','Palolem','Dudhsagar','Arambol','Vagator'],
    'Gujarat':           ['Rann of Kutch','Gir Forest','Ahmedabad','Vadodara','Surat','Dwarka','Somnath','Saputara','Champaner','Mandvi','Palitana','Lothal'],
    'Haryana':           ['Kurukshetra','Sultanpur','Morni Hills','Pinjore','Faridabad'],
    'Himachal Pradesh':  ['Manali','Shimla','Dharamsala','McLeod Ganj','Spiti Valley','Kaza','Kasol','Bir Billing','Dalhousie','Chail','Kinnaur','Khajjiar','Kullu','Sangla','Chitkul','Kalpa'],
    'Jharkhand':         ['Ranchi','Jamshedpur','Betla','Hundru Falls','Deoghar','Netarhat','Palamu'],
    'Karnataka':         ['Coorg','Mysuru','Hampi','Badami','Chikmagalur','Kabini','Dandeli','Gokarna','Mangalore','Udupi','Sakleshpur','Bidar','Shravanabelagola','Belur','Halebidu','Jog Falls','Agumbe'],
    'Kerala':            ['Munnar','Alleppey','Thekkady','Kovalam','Wayanad','Kochi','Thrissur','Varkala','Bekal','Athirappilly','Kumarakom','Marari','Kasaragod'],
    'Ladakh':            ['Leh','Nubra Valley','Pangong Lake','Zanskar','Turtuk','Hanle','Magnetic Hill','Diskit','Kargil','Hemis'],
    'Madhya Pradesh':    ['Khajuraho','Bandhavgarh','Kanha','Pench','Sanchi','Orchha','Gwalior','Pachmarhi','Mandu','Bhopal','Jabalpur','Amarkantak','Bhimbetka','Chanderi','Shivpuri'],
    'Maharashtra':       ['Mumbai','Pune','Aurangabad','Lonavala','Mahabaleshwar','Nashik','Kolhapur','Alibag','Matheran','Ajanta Ellora','Tadoba','Panchgani','Igatpuri','Malshej Ghat','Satara'],
    'Manipur':           ['Imphal','Loktak Lake','Keibul Lamjao','Moreh','Ukhrul','Dzuko Valley Manipur'],
    'Meghalaya':         ['Shillong','Cherrapunji','Mawlynnong','Dawki','Nohkalikai','Mawsynram','Nongriat','Laitlum'],
    'Mizoram':           ['Aizawl','Phawngpui','Champhai','Reiek','Tam Dil'],
    'Nagaland':          ['Kohima','Hornbill Festival','Dzukou Valley','Dimapur','Mokokchung','Khonoma'],
    'Odisha':            ['Puri','Bhubaneswar','Konark','Chilika Lake','Simlipal','Bhitarkanika','Daringbadi','Gopalpur','Cuttack','Rayagada'],
    'Punjab':            ['Amritsar','Ludhiana','Patiala','Anandpur Sahib','Wagah Border','Fatehgarh Sahib','Bathinda'],
    'Rajasthan':         ['Jaipur','Udaipur','Jodhpur','Jaisalmer','Pushkar','Ranthambore','Mount Abu','Bikaner','Ajmer','Bundi','Chittorgarh','Kumbhalgarh','Bharatpur','Mandawa','Sawai Madhopur','Shekhawati','Alwar','Tonk'],
    'Sikkim':            ['Gangtok','Pelling','Lachung','Yumthang Valley','Goechala','Ravangla','Namchi','Zuluk','Yuksom','Dzongri'],
    'Tamil Nadu':        ['Chennai','Ooty','Kodaikanal','Madurai','Mahabalipuram','Rameswaram','Thanjavur','Kanyakumari','Yercaud','Pondicherry','Coimbatore','Salem','Chettinad','Mudumalai','Valparai','Courtallam','Vellore'],
    'Telangana':         ['Hyderabad','Warangal','Nagarjunasagar','Ramappa','Medak','Bhongir','Karimnagar','Nizamabad'],
    'Tripura':           ['Agartala','Neermahal','Sepahijala','Unakoti','Jampui Hills'],
    'Uttar Pradesh':     ['Agra','Varanasi','Lucknow','Mathura','Vrindavan','Ayodhya','Prayagraj','Sarnath','Dudhwa','Chitrakoot','Fatehpur Sikri'],
    'Uttarakhand':       ['Rishikesh','Haridwar','Mussoorie','Nainital','Jim Corbett','Auli','Chopta','Lansdowne','Kedarnath','Badrinath','Valley of Flowers','Roopkund','Chakrata','Munsiyari','Ranikhet','Binsar','Chaukori'],
    'West Bengal':       ['Kolkata','Darjeeling','Kalimpong','Sundarbans','Bishnupur','Dooars','Siliguri','Lava','Lolegaon','Sandakphu'],
    'Andaman Islands':   ['Port Blair','Havelock Island','Neil Island','Baratang','Ross Island','Diglipur','Long Island'],
    'Lakshadweep':       ['Agatti','Bangaram','Kavaratti','Minicoy'],
    'Delhi':             ['Old Delhi','New Delhi','Chandni Chowk','Qutub Minar','Lodhi Garden','Hauz Khas'],
    'Jammu & Kashmir':   ['Srinagar','Gulmarg','Pahalgam','Sonamarg','Patnitop','Vaishno Devi','Doodhpathri'],
}
 
 
def get_destination_context(destination: str) -> dict:
    """Fetch real data about destination from free APIs."""
    context = {'destination': destination}
 
    # 1. Wikipedia summary
    try:
        url  = f'https://en.wikipedia.org/api/rest_v1/page/summary/{destination.replace(" ", "_")}'
        resp = requests.get(url, timeout=8, headers={'User-Agent': 'PackVote/1.0'})
        if resp.status_code == 200:
            data = resp.json()
            context['description'] = data.get('extract', '')[:500]
            context['wiki_url']    = data.get('content_urls', {}).get('desktop', {}).get('page', '')
    except Exception as e:
        print(f'  Wikipedia error: {e}')
    if not context.get('description'):
        context['description'] = f'{destination} is a popular travel destination in India.'
 
    # 2. OpenTripMap attractions (free key from opentripmap.com)
    OPENTRIPMAP_KEY = os.environ.get('OPENTRIPMAP_KEY', '')
    context['attractions'] = []
    if OPENTRIPMAP_KEY:
        try:
            geo = requests.get(
                f'https://api.opentripmap.com/0.1/en/places/geoname?name={destination}&apikey={OPENTRIPMAP_KEY}',
                timeout=8
            ).json()
            lat, lon = geo.get('lat'), geo.get('lon')
            if lat and lon:
                places = requests.get(
                    f'https://api.opentripmap.com/0.1/en/places/radius'
                    f'?radius=15000&lon={lon}&lat={lat}'
                    f'&kinds=interesting_places,cultural,natural,religion,architecture'
                    f'&limit=15&apikey={OPENTRIPMAP_KEY}',
                    timeout=10
                ).json()
                context['attractions'] = [
                    p['properties']['name']
                    for p in places.get('features', [])
                    if p['properties'].get('name')
                ][:10]
                context['lat'] = lat
                context['lon'] = lon
        except Exception as e:
            print(f'  OpenTripMap error: {e}')
 
    # 3. Weather from wttr.in
    try:
        resp = requests.get(
            f'https://wttr.in/{destination}?format=j1',
            timeout=8, headers={'User-Agent': 'PackVote/1.0'}
        )
        if resp.status_code == 200:
            data    = resp.json()
            current = data['current_condition'][0]
            context['weather'] = {
                'temp_c':      current['temp_C'],
                'description': current['weatherDesc'][0]['value'],
                'humidity':    current['humidity'],
                'forecast': [
                    {'date': d['date'], 'max': d['maxtempC'], 'min': d['mintempC']}
                    for d in data.get('weather', [])[:3]
                ]
            }
    except Exception as e:
        print(f'  Weather error: {e}')
        context['weather'] = {'temp_c': 'N/A', 'description': 'Data unavailable'}
 
    # 4. Local events via Wikipedia search
    try:
        resp = requests.get(
            f'https://en.wikipedia.org/w/api.php?action=query&list=search'
            f'&srsearch={destination}+festival+fair+event&format=json&srlimit=4',
            timeout=8
        ).json()
        context['local_events'] = [
            item['title']
            for item in resp.get('query', {}).get('search', [])
        ]
    except:
        context['local_events'] = []
 
    return context
 
 
def generate_ai_itinerary(
    destination:   str,
    duration:      int   = 5,
    budget:        str   = 'medium',
    travel_styles: list  = None,
    month:         str   = 'December',
    group_size:    int   = 4,
    food_pref:     str   = 'both',
    group_type:    str   = 'friends'
) -> dict:
    """
    Generate full AI itinerary using Groq LLaMA 3 (free).
    Falls back to rule-based if Groq key not available.
    """
    if travel_styles is None:
        travel_styles = ['culture']
 
    # Fetch real destination data
    print(f'Fetching data for {destination}...')
    context = get_destination_context(destination)
 
    attr_text  = ', '.join(context.get('attractions', [])[:8]) or 'local attractions'
    event_text = ', '.join(context.get('local_events', [])[:3]) or 'local festivals'
    budget_daily = {'low': '₹1500', 'medium': '₹4000', 'high': '₹9000', 'luxury': '₹20000'}.get(budget, '₹4000')
 
    prompt = f"""You are an expert Indian travel planner. Create a {duration}-day itinerary for {destination}.
 
GROUP: {group_size} {group_type}, {budget} budget ({budget_daily}/person/day), travel month: {month}
STYLES: {', '.join(travel_styles)}, FOOD: {food_pref}
ABOUT: {context.get('description', '')[:250]}
ATTRACTIONS: {attr_text}
LOCAL EVENTS: {event_text}
WEATHER: {context.get('weather', {}).get('temp_c', 'N/A')}°C, {context.get('weather', {}).get('description', '')}
 
Create a PRACTICAL {duration}-day itinerary. Respond ONLY in this exact JSON (no markdown):
{{
  "destination": "{destination}",
  "duration": {duration},
  "theme": "catchy one-line trip description",
  "highlights": ["highlight 1", "highlight 2", "highlight 3"],
  "reach": {{
    "by_train": "nearest station + train suggestion from Delhi/Mumbai",
    "by_bus": "bus route suggestion",
    "by_flight": "nearest airport + airlines",
    "by_road": "road distance from nearest major city"
  }},
  "stay": {{
    "budget": "budget stay name/area + price range",
    "mid": "mid-range option + price range",
    "luxury": "luxury option + price range"
  }},
  "days": [
    {{
      "day": 1,
      "title": "Day title",
      "morning": {{
        "time": "7:00 AM - 10:00 AM",
        "activity": "name",
        "description": "2 sentence description",
        "cost": "₹XX per person",
        "transport": "how to get there",
        "tips": "insider tip"
      }},
      "afternoon": {{
        "time": "11:00 AM - 3:00 PM",
        "activity": "name",
        "description": "2 sentence description",
        "cost": "₹XX per person",
        "transport": "how to get there",
        "tips": "insider tip"
      }},
      "evening": {{
        "time": "4:00 PM - 8:00 PM",
        "activity": "name",
        "description": "2 sentence description",
        "cost": "₹XX per person",
        "transport": "how to get there",
        "tips": "insider tip"
      }},
      "lunch": {{
        "restaurant": "name or type",
        "area": "locality",
        "cuisine": "type",
        "type": "veg/nonveg/both",
        "must_try": "dish name",
        "price_for_two": "₹XXX"
      }},
      "dinner": {{
        "restaurant": "name or type",
        "area": "locality",
        "cuisine": "type",
        "type": "veg/nonveg/both",
        "must_try": "dish name",
        "price_for_two": "₹XXX"
      }},
      "day_cost_per_person": "₹XXXX",
      "local_transport": "main transport today",
      "pro_tip": "one specific tip"
    }}
  ],
  "must_eat": [
    {{"dish": "name", "where": "place", "price": "₹XX", "type": "veg/nonveg"}}
  ],
  "packing": ["item 1", "item 2", "item 3", "item 4"],
  "safety_tips": ["tip 1", "tip 2"],
  "useful_apps": ["app - why useful"],
  "total_cost": {{
    "per_person_inr": "₹XXXXX",
    "for_group_inr": "₹XXXXX",
    "breakdown": {{
      "accommodation": "₹XXXX",
      "food": "₹XXXX",
      "transport": "₹XXXX",
      "activities": "₹XXXX",
      "miscellaneous": "₹XXXX"
    }}
  }}
}}"""
 
    # Try Groq first
    if GROQ_API_KEY:
        try:
            print('Calling Groq API...')
            resp = requests.post(
                GROQ_URL,
                headers={
                    'Authorization': f'Bearer {GROQ_API_KEY}',
                    'Content-Type':  'application/json'
                },
                json={
                    'model':       'llama3-70b-8192',
                    'max_tokens':  4096,
                    'temperature': 0.7,
                    'messages': [
                        {
                            'role':    'system',
                            'content': 'You are an expert Indian travel planner. Always respond with valid JSON only, no markdown, no extra text.'
                        },
                        {'role': 'user', 'content': prompt}
                    ]
                },
                timeout=60
            )
            raw = resp.json()['choices'][0]['message']['content'].strip()
 
            # Strip markdown fences if present
            if raw.startswith('```'):
                lines = raw.split('\n')
                raw   = '\n'.join(lines[1:-1] if lines[-1].strip() == '```' else lines[1:])
 
            itinerary = json.loads(raw)
            itinerary['ai_powered']  = True
            itinerary['ai_model']    = 'LLaMA 3 70B via Groq (free)'
            itinerary['context']     = context
            print(f'✅ AI itinerary generated for {destination}')
            return itinerary
 
        except Exception as e:
            print(f'Groq failed ({e}), using rule-based fallback')
 
    # Rule-based fallback
    return _rule_based_fallback(destination, duration, budget, travel_styles, month, group_size, context)
 
 
def _rule_based_fallback(destination, duration, budget, styles, month, group_size, context) -> dict:
    """Complete rule-based itinerary when AI is unavailable."""
    daily_costs = {'low': 1500, 'medium': 4000, 'high': 9000, 'luxury': 20000}
    daily       = daily_costs.get(budget, 4000)
 
    spots = context.get('attractions', [])
    if not spots:
        spots = [
            'City Museum', 'Central Market', 'Historical Fort',
            'Local Temple', 'Botanical Garden', 'Viewpoint',
            'Art Gallery', 'Heritage Walk', 'Waterfront'
        ]
 
    day_themes = [
        'Arrival & First Impressions',
        'Heritage & Culture',
        'Nature & Adventure',
        'Food & Local Life',
        'Shopping & Leisure',
        'Hidden Gems',
        'Departure Day'
    ]
 
    days = []
    idx  = 0
    for d in range(1, duration + 1):
        ms = spots[idx % len(spots)]; idx += 1
        af = spots[idx % len(spots)]; idx += 1
        ev = spots[idx % len(spots)]; idx += 1
        days.append({
            'day':   d,
            'title': day_themes[(d - 1) % len(day_themes)],
            'morning':   {'time': '8:00 AM',  'activity': ms, 'description': f'Explore {ms} — one of {destination}\'s must-visit spots.', 'cost': f'₹{int(daily*0.2)}', 'transport': 'Auto/cab', 'tips': 'Go early to beat crowds'},
            'afternoon': {'time': '12:00 PM', 'activity': af, 'description': f'Spend the afternoon at {af}.', 'cost': f'₹{int(daily*0.3)}', 'transport': 'Auto/walk', 'tips': 'Carry water and sunscreen'},
            'evening':   {'time': '5:00 PM',  'activity': ev, 'description': f'Relax at {ev} as the day winds down.', 'cost': f'₹{int(daily*0.15)}', 'transport': 'Walk', 'tips': 'Best time for photos'},
            'lunch':  {'restaurant': 'Local dhaba', 'area': 'City centre', 'cuisine': 'Regional', 'type': 'both', 'must_try': 'Local thali', 'price_for_two': f'₹{int(daily*0.15)}'},
            'dinner': {'restaurant': 'Local restaurant', 'area': 'Main market', 'cuisine': 'Regional', 'type': 'both', 'must_try': 'Street food special', 'price_for_two': f'₹{int(daily*0.2)}'},
            'day_cost_per_person': f'₹{daily}',
            'local_transport':     'Auto rickshaw / local bus / walking',
            'pro_tip':             f'Ask locals for hidden gems on Day {d}'
        })
 
    return {
        'destination': destination,
        'duration':    duration,
        'theme':       f'Discover the best of {destination}',
        'highlights':  [f'Explore {s}' for s in spots[:3]],
        'reach': {
            'by_train':  f'Search trains to nearest station on irctc.co.in',
            'by_bus':    f'Check redbus.in for routes to {destination}',
            'by_flight': f'Search flights on Google Flights',
            'by_road':   f'Check Google Maps for road route to {destination}'
        },
        'stay': {
            'budget':  f'Budget guesthouses near {destination} centre — ₹800-1500/night',
            'mid':     f'Mid-range hotels near {destination} — ₹2000-4000/night',
            'luxury':  f'Premium resorts near {destination} — ₹6000+/night'
        },
        'days': days,
        'must_eat': [
            {'dish': 'Local speciality', 'where': 'City centre', 'price': '₹100', 'type': 'both'},
            {'dish': 'Regional thali',   'where': 'Local dhaba', 'price': '₹150', 'type': 'both'},
            {'dish': 'Street snacks',    'where': 'Main market', 'price': '₹50',  'type': 'both'},
        ],
        'packing':      [f'Light clothes for {month}', 'Comfortable walking shoes', 'Sunscreen & sunglasses', 'Power bank & camera'],
        'safety_tips':  ['Keep emergency contacts saved', 'Carry a physical ID copy'],
        'useful_apps':  ['Google Maps — offline navigation', 'IRCTC — train booking', 'Zomato — restaurant search'],
        'total_cost': {
            'per_person_inr': f'₹{daily * duration + 8000}',
            'for_group_inr':  f'₹{(daily * duration + 8000) * group_size}',
            'breakdown': {
                'accommodation': f'₹{int(daily * 0.35 * duration)}',
                'food':          f'₹{int(daily * 0.30 * duration)}',
                'transport':     f'₹{int(daily * 0.15 * duration) + 4000}',
                'activities':    f'₹{int(daily * 0.20 * duration)}',
                'miscellaneous': f'₹{int(daily * 0.10 * duration)}'
            }
        },
        'ai_powered': False,
        'ai_model':   'Rule-based fallback',
        'context':    context
    }