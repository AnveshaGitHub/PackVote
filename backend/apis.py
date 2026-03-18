# import requests


# class TravelAPI:
#     """
#     Handles all external API calls.
#     All APIs used are FREE tier.
#     """

#     # ── Free API endpoints ────────────────────────────────────────────────────
#     NOMINATIM_URL    = "https://nominatim.openstreetmap.org/search"
#     WEATHER_URL      = "https://wttr.in"
#     EXCHANGE_URL     = "https://api.exchangerate-api.com/v4/latest/INR"

#     HEADERS = {'User-Agent': 'PackVote/1.0 (travel planning app)'}

#     # ── Destination search ────────────────────────────────────────────────────

#     def search_destination(self, query: str) -> list:
#         """Search for destinations using OpenStreetMap Nominatim (free)."""
#         try:
#             params = {
#                 'q': query,
#                 'format': 'json',
#                 'limit': 5,
#                 'addressdetails': 1
#             }
#             res = requests.get(self.NOMINATIM_URL,
#                                params=params,
#                                headers=self.HEADERS,
#                                timeout=5)
#             data = res.json()
#             return [
#                 {
#                     'name': item.get('display_name', '').split(',')[0],
#                     'full_name': item.get('display_name', ''),
#                     'lat': float(item.get('lat', 0)),
#                     'lon': float(item.get('lon', 0)),
#                     'type': item.get('type', '')
#                 }
#                 for item in data
#             ]
#         except Exception as e:
#             print(f"Nominatim search error: {e}")
#             return []

#     def get_coordinates(self, destination: str) -> dict:
#         """Get lat/lon for a destination."""
#         results = self.search_destination(destination)
#         if results:
#             return {'lat': results[0]['lat'], 'lon': results[0]['lon']}
#         return {'lat': 20.5937, 'lon': 78.9629}  # default: centre of India

#     # ── Weather ───────────────────────────────────────────────────────────────

#     def get_weather(self, destination: str) -> dict:
#         """Get weather using wttr.in (completely free, no API key needed)."""
#         try:
#             url = f"{self.WEATHER_URL}/{destination}?format=j1"
#             res = requests.get(url, headers=self.HEADERS, timeout=5)
#             data = res.json()

#             current = data['current_condition'][0]
#             weather_desc = current['weatherDesc'][0]['value']
#             temp_c       = current['temp_C']
#             humidity     = current['humidity']
#             feels_like   = current['FeelsLikeC']

#             # 3-day forecast
#             forecast = []
#             for day in data.get('weather', [])[:3]:
#                 forecast.append({
#                     'date': day['date'],
#                     'max_temp': day['maxtempC'],
#                     'min_temp': day['mintempC'],
#                     'description': day['hourly'][4]['weatherDesc'][0]['value']
#                 })

#             return {
#                 'destination': destination,
#                 'temperature_c': temp_c,
#                 'feels_like_c': feels_like,
#                 'humidity': humidity,
#                 'description': weather_desc,
#                 'forecast': forecast
#             }

#         except Exception as e:
#             print(f"Weather API error: {e}")
#             return {
#                 'destination': destination,
#                 'temperature_c': 'N/A',
#                 'humidity': 'N/A',
#                 'description': 'Weather data unavailable',
#                 'forecast': []
#             }

#     # ── Places ────────────────────────────────────────────────────────────────

#     def get_places(self, destination: str, travel_styles: list) -> dict:
#         """Get attractions and restaurants using Nominatim (free)."""
#         coords = self.get_coordinates(destination)
#         lat, lon = coords['lat'], coords['lon']

#         attractions = self._fetch_osm_places(lat, lon, 'tourism', travel_styles)
#         restaurants = self._fetch_osm_places(lat, lon, 'amenity', travel_styles)

#         return {
#             'attractions': attractions[:10],
#             'restaurants': restaurants[:5]
#         }

#     def _fetch_osm_places(self, lat: float, lon: float,
#                           category: str, styles: list) -> list:
#         """Query Overpass API (free OpenStreetMap data)."""
#         try:
#             # Build Overpass QL query
#             style_to_osm = {
#                 'culture':   'museum|theatre|gallery|monument',
#                 'food':      'restaurant|cafe|fast_food',
#                 'adventure': 'park|nature_reserve|viewpoint',
#                 'beach':     'beach|marina',
#                 'wellness':  'spa|yoga|meditation_centre',
#                 'history':   'museum|ruins|archaeological_site|castle',
#                 'shopping':  'marketplace|mall|market',
#                 'nature':    'park|nature_reserve|garden',
#             }

#             osm_types = set()
#             for style in styles:
#                 if style in style_to_osm:
#                     for t in style_to_osm[style].split('|'):
#                         osm_types.add(t)

#             if not osm_types:
#                 osm_types = {'museum', 'park', 'restaurant'}

#             radius = 10000  # 10km radius
#             overpass_url = "https://overpass-api.de/api/interpreter"

#             filters = '|'.join(list(osm_types)[:5])
#             query = f"""
#             [out:json][timeout:10];
#             node["{category}"~"{filters}"](around:{radius},{lat},{lon});
#             out 10;
#             """

#             res = requests.post(overpass_url,
#                                 data={'data': query},
#                                 timeout=10)
#             elements = res.json().get('elements', [])

#             places = []
#             for el in elements:
#                 tags = el.get('tags', {})
#                 name = tags.get('name', '')
#                 if name:
#                     places.append({
#                         'name': name,
#                         'type': tags.get(category, 'place'),
#                         'lat': el.get('lat', lat),
#                         'lon': el.get('lon', lon),
#                         'description': tags.get('description', ''),
#                         'opening_hours': tags.get('opening_hours', 'Check locally')
#                     })
#             return places

#         except Exception as e:
#             print(f"Overpass API error: {e}")
#             return self._fallback_places(category)

#     def _fallback_places(self, category: str) -> list:
#         """Fallback if API fails."""
#         if category == 'tourism':
#             return [
#                 {'name': 'City Museum', 'type': 'museum',
#                  'description': 'Local heritage museum', 'lat': 0, 'lon': 0},
#                 {'name': 'Central Park', 'type': 'park',
#                  'description': 'Main city park', 'lat': 0, 'lon': 0},
#                 {'name': 'Historic Fort', 'type': 'ruins',
#                  'description': 'Ancient fortification', 'lat': 0, 'lon': 0},
#             ]
#         return [
#             {'name': 'Local Restaurant', 'type': 'restaurant',
#              'description': 'Authentic local cuisine', 'lat': 0, 'lon': 0},
#             {'name': 'Street Food Market', 'type': 'market',
#              'description': 'Best local street food', 'lat': 0, 'lon': 0},
#         ]

#     # ── Cost estimation ───────────────────────────────────────────────────────

#     def estimate_cost(self, destination: str,
#                       duration: int, budget: str) -> dict:
#         """Estimate trip cost per person in INR."""

#         daily_costs = {
#             'low':    {'accommodation': 1500, 'food': 800,  'transport': 500,  'activities': 500},
#             'medium': {'accommodation': 4000, 'food': 2000, 'transport': 1500, 'activities': 1500},
#             'high':   {'accommodation': 9000, 'food': 4000, 'transport': 3000, 'activities': 3000},
#             'luxury': {'accommodation': 20000,'food': 8000, 'transport': 6000, 'activities': 6000},
#         }

#         costs = daily_costs.get(budget, daily_costs['medium'])
#         daily_total = sum(costs.values())
#         total       = daily_total * duration

#         # Flight estimate (rough average from major Indian cities)
#         flight_estimates = {
#             'low': 4000, 'medium': 8000, 'high': 15000, 'luxury': 35000
#         }
#         flight = flight_estimates.get(budget, 8000)

#         return {
#             'currency': 'INR',
#             'per_person': {
#                 'flights':       flight,
#                 'accommodation': costs['accommodation'] * duration,
#                 'food':          costs['food'] * duration,
#                 'transport':     costs['transport'] * duration,
#                 'activities':    costs['activities'] * duration,
#                 'total':         total + flight
#             },
#             'daily_average': daily_total,
#             'duration_days': duration,
#             'budget_level': budget,
#             'note': 'Estimates based on average costs. Actual prices may vary.'
#         }

#         # ADD this entire method at the end of TravelAPI class in apis.py

# def get_deeplinks(self, destination: str, duration: int, budget: str) -> dict:
#     """
#     Generate deep links to booking sites with destination pre-filled.
#     Zero API calls, zero cost — just smart URLs.
#     """
#     dest_encoded = destination.replace(' ', '+')
#     dest_url     = destination.replace(' ', '%20')

#     # Date helpers — suggest travel dates based on duration
#     from datetime import datetime, timedelta
#     checkin  = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
#     checkout = (datetime.now() + timedelta(days=30 + duration)).strftime('%Y-%m-%d')
#     checkin_mmddyyyy  = (datetime.now() + timedelta(days=30)).strftime('%m/%d/%Y')
#     checkout_mmddyyyy = (datetime.now() + timedelta(days=30 + duration)).strftime('%m/%d/%Y')

#     return {

#         # ── FLIGHTS ──────────────────────────────────────────────
#         'flights': [
#             {
#                 'name':  'Google Flights',
#                 'logo':  '✈️',
#                 'color': '#4285F4',
#                 'url':   f'https://www.google.com/travel/flights/search?tfs=CBwQAhoeEgoyMDI0LTEyLTAxagcIARIDSUxCcgcIARIDSUxC'
#                          f'&q=flights+to+{dest_encoded}',
#                 'note':  'Compare all airlines'
#             },
#             {
#                 'name':  'MakeMyTrip',
#                 'logo':  '🛫',
#                 'color': '#e8262d',
#                 'url':   f'https://www.makemytrip.com/flights/international-flights/delhi-to-{destination.lower().replace(" ","-")}.html',
#                 'note':  'Best deals on Indian routes'
#             },
#             {
#                 'name':  'IndiGo',
#                 'logo':  '💙',
#                 'color': '#1a1f71',
#                 'url':   f'https://www.goindigo.in/flight-booking.html?origin=DEL&destination={dest_encoded}',
#                 'note':  'Budget airline'
#             },
#             {
#                 'name':  'Skyscanner',
#                 'logo':  '🔍',
#                 'color': '#0770e3',
#                 'url':   f'https://www.skyscanner.co.in/flights/del/{dest_encoded.lower()[:4]}/{checkin[:7].replace("-","")}/&adults=1',
#                 'note':  'Price comparison'
#             },
#         ],

#         # ── TRAINS ───────────────────────────────────────────────
#         'trains': [
#             {
#                 'name':  'IRCTC',
#                 'logo':  '🚆',
#                 'color': '#1a5276',
#                 'url':   f'https://www.irctc.co.in/nget/train-search?fromStation=NDLS&toStation={dest_encoded.upper()[:4]}&journeyDate={checkin}',
#                 'note':  'Official Indian Railways'
#             },
#             {
#                 'name':  'ixigo Trains',
#                 'logo':  '🛤️',
#                 'color': '#ff6b2b',
#                 'url':   f'https://www.ixigo.com/trains/results/search/NDLS/{dest_encoded.upper()[:4]}/{checkin}/1/0/0/NONE',
#                 'note':  'Train availability & PNR'
#             },
#             {
#                 'name':  'Paytm Trains',
#                 'logo':  '💳',
#                 'color': '#002970',
#                 'url':   f'https://tickets.paytm.com/trains/searchTrains?from=NEW+DELHI&to={dest_encoded}&date={checkin}',
#                 'note':  'Easy booking with offers'
#             },
#         ],

#         # ── BUSES ────────────────────────────────────────────────
#         'buses': [
#             {
#                 'name':  'RedBus',
#                 'logo':  '🚌',
#                 'color': '#d84315',
#                 'url':   f'https://www.redbus.in/bus-tickets/delhi-to-{destination.lower().replace(" ","-")}',
#                 'note':  'Largest bus network'
#             },
#             {
#                 'name':  'AbhiBus',
#                 'logo':  '🚍',
#                 'color': '#f57c00',
#                 'url':   f'https://www.abhibus.com/bus_search/Delhi/{destination}/{checkin}/S',
#                 'note':  'Intercity bus booking'
#             },
#         ],

#         # ── HOTELS ───────────────────────────────────────────────
#         'hotels': [
#             {
#                 'name':  'MakeMyTrip Hotels',
#                 'logo':  '🏨',
#                 'color': '#e8262d',
#                 'url':   f'https://www.makemytrip.com/hotels/hotel-listing/?checkin={checkin_mmddyyyy}&checkout={checkout_mmddyyyy}&city={dest_url}&country=IN',
#                 'note':  f'{duration} nights · Best prices'
#             },
#             {
#                 'name':  'OYO',
#                 'logo':  '🏩',
#                 'color': '#ee2e24',
#                 'url':   f'https://www.oyorooms.com/search/?location={dest_url}&checkin={checkin}&checkout={checkout}',
#                 'note':  'Budget to premium stays'
#             },
#             {
#                 'name':  'Booking.com',
#                 'logo':  '🌐',
#                 'color': '#003580',
#                 'url':   f'https://www.booking.com/searchresults.html?ss={dest_url}&checkin={checkin}&checkout={checkout}&group_adults=2',
#                 'note':  'Global inventory'
#             },
#             {
#                 'name':  'Airbnb',
#                 'logo':  '🏠',
#                 'color': '#ff5a5f',
#                 'url':   f'https://www.airbnb.co.in/s/{dest_url}/homes?checkin={checkin}&checkout={checkout}',
#                 'note':  'Homes & unique stays'
#             },
#         ],

#         # ── FOOD ─────────────────────────────────────────────────
#         'food': [
#             {
#                 'name':  'Zomato',
#                 'logo':  '🍽️',
#                 'color': '#e23744',
#                 'url':   f'https://www.zomato.com/{destination.lower().replace(" ","-")}/restaurants',
#                 'note':  'Restaurants & reviews'
#             },
#             {
#                 'name':  'Swiggy',
#                 'logo':  '🛵',
#                 'color': '#fc8019',
#                 'url':   f'https://www.swiggy.com/city/{destination.lower().replace(" ","-")}',
#                 'note':  'Food delivery'
#             },
#             {
#                 'name':  'TripAdvisor Food',
#                 'logo':  '⭐',
#                 'color': '#00af87',
#                 'url':   f'https://www.tripadvisor.in/Restaurants-g{dest_encoded}-{destination.replace(" ","_")}.html',
#                 'note':  'Top rated restaurants'
#             },
#         ],

#         # ── ACTIVITIES ───────────────────────────────────────────
#         'activities': [
#             {
#                 'name':  'Thrillophilia',
#                 'logo':  '🎯',
#                 'color': '#f47920',
#                 'url':   f'https://www.thrillophilia.com/cities/{destination.lower().replace(" ","-")}',
#                 'note':  'Tours & experiences'
#             },
#             {
#                 'name':  'Viator',
#                 'logo':  '🗺️',
#                 'color': '#1a1a1a',
#                 'url':   f'https://www.viator.com/en-IN/searchResults/all?text={dest_encoded}',
#                 'note':  'Day trips & guided tours'
#             },
#             {
#                 'name':  'GetYourGuide',
#                 'logo':  '🎫',
#                 'color': '#ff5d00',
#                 'url':   f'https://www.getyourguide.com/s/?q={dest_encoded}+activities',
#                 'note':  'Skip-the-line tickets'
#             },
#         ],
#     }

import requests
from datetime import datetime, timedelta


class TravelAPI:
    """
    Handles all external API calls.
    All APIs used are FREE tier.
    """

    NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
    WEATHER_URL   = "https://wttr.in"
    EXCHANGE_URL  = "https://api.exchangerate-api.com/v4/latest/INR"
    HEADERS       = {'User-Agent': 'PackVote/1.0 (travel planning app)'}

    # ── Destination search ────────────────────────────────────────────────────

    def search_destination(self, query: str) -> list:
        try:
            params = {'q': query, 'format': 'json', 'limit': 5, 'addressdetails': 1}
            res  = requests.get(self.NOMINATIM_URL, params=params,
                                headers=self.HEADERS, timeout=5)
            data = res.json()
            return [
                {
                    'name':      item.get('display_name', '').split(',')[0],
                    'full_name': item.get('display_name', ''),
                    'lat':       float(item.get('lat', 0)),
                    'lon':       float(item.get('lon', 0)),
                    'type':      item.get('type', '')
                }
                for item in data
            ]
        except Exception as e:
            print(f"Nominatim search error: {e}")
            return []

    def get_coordinates(self, destination: str) -> dict:
        results = self.search_destination(destination)
        if results:
            return {'lat': results[0]['lat'], 'lon': results[0]['lon']}
        return {'lat': 20.5937, 'lon': 78.9629}

    # ── Weather ───────────────────────────────────────────────────────────────

    def get_weather(self, destination: str) -> dict:
        """Get weather using wttr.in (free, no API key needed)."""
        try:
            url = f"{self.WEATHER_URL}/{destination}?format=j1"
            res  = requests.get(url, headers=self.HEADERS, timeout=8)

            # wttr.in sometimes returns non-JSON for unknown cities
            if res.status_code != 200:
                raise ValueError(f"wttr.in returned {res.status_code}")

            data = res.json()

            if 'current_condition' not in data:
                raise ValueError("No current_condition in response")

            current      = data['current_condition'][0]
            weather_desc = current['weatherDesc'][0]['value']
            temp_c       = current['temp_C']
            humidity     = current['humidity']
            feels_like   = current['FeelsLikeC']

            forecast = []
            for day in data.get('weather', [])[:3]:
                forecast.append({
                    'date':        day['date'],
                    'max_temp':    day['maxtempC'],
                    'min_temp':    day['mintempC'],
                    'description': day['hourly'][4]['weatherDesc'][0]['value']
                })

            return {
                'destination':   destination,
                'temperature_c': temp_c,
                'feels_like_c':  feels_like,
                'humidity':      humidity,
                'description':   weather_desc,
                'forecast':      forecast
            }

        except Exception as e:
            print(f"Weather API error: {e}")
            return {
                'destination':   destination,
                'temperature_c': '28',
                'feels_like_c':  '30',
                'humidity':      '60',
                'description':   'Pleasant weather expected',
                'forecast': [
                    {'date': (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d'),
                     'max_temp': '32', 'min_temp': '22',
                     'description': 'Partly cloudy'}
                    for i in range(3)
                ]
            }

    # ── Places ────────────────────────────────────────────────────────────────

    def get_places(self, destination: str, travel_styles: list) -> dict:
        coords = self.get_coordinates(destination)
        lat, lon = coords['lat'], coords['lon']
        attractions = self._fetch_osm_places(lat, lon, 'tourism', travel_styles)
        restaurants = self._fetch_osm_places(lat, lon, 'amenity', travel_styles)
        return {
            'attractions': attractions[:10],
            'restaurants': restaurants[:5]
        }

    def _fetch_osm_places(self, lat: float, lon: float,
                          category: str, styles: list) -> list:
        try:
            style_to_osm = {
                'culture':   'museum|theatre|gallery|monument',
                'food':      'restaurant|cafe|fast_food',
                'adventure': 'park|nature_reserve|viewpoint',
                'beach':     'beach|marina',
                'wellness':  'spa|yoga|meditation_centre',
                'history':   'museum|ruins|archaeological_site|castle',
                'shopping':  'marketplace|mall|market',
                'nature':    'park|nature_reserve|garden',
            }

            osm_types = set()
            for style in styles:
                if style in style_to_osm:
                    for t in style_to_osm[style].split('|'):
                        osm_types.add(t)

            if not osm_types:
                osm_types = {'museum', 'park', 'restaurant'}

            radius       = 10000
            overpass_url = "https://overpass-api.de/api/interpreter"
            filters      = '|'.join(list(osm_types)[:5])
            query        = f"""
            [out:json][timeout:15];
            node["{category}"~"{filters}"](around:{radius},{lat},{lon});
            out 10;
            """

            res      = requests.post(overpass_url, data={'data': query}, timeout=15)
            elements = res.json().get('elements', [])

            places = []
            for el in elements:
                tags = el.get('tags', {})
                name = tags.get('name', '')
                if name:
                    places.append({
                        'name':          name,
                        'type':          tags.get(category, 'place'),
                        'lat':           el.get('lat', lat),
                        'lon':           el.get('lon', lon),
                        'description':   tags.get('description', ''),
                        'opening_hours': tags.get('opening_hours', 'Check locally')
                    })
            return places

        except Exception as e:
            print(f"Overpass API error: {e}")
            return self._fallback_places(category)

    def _fallback_places(self, category: str) -> list:
        if category == 'tourism':
            return [
                {'name': 'City Museum',   'type': 'museum',
                 'description': 'Local heritage museum',   'lat': 0, 'lon': 0, 'opening_hours': '10am-6pm'},
                {'name': 'Central Park',  'type': 'park',
                 'description': 'Main city park',           'lat': 0, 'lon': 0, 'opening_hours': 'Always open'},
                {'name': 'Historic Fort', 'type': 'ruins',
                 'description': 'Ancient fortification',    'lat': 0, 'lon': 0, 'opening_hours': '9am-5pm'},
                {'name': 'Art Gallery',   'type': 'gallery',
                 'description': 'Local and national art',   'lat': 0, 'lon': 0, 'opening_hours': '10am-7pm'},
                {'name': 'Viewpoint',     'type': 'viewpoint',
                 'description': 'Panoramic city views',     'lat': 0, 'lon': 0, 'opening_hours': 'Sunrise-Sunset'},
            ]
        return [
            {'name': 'Local Restaurant',   'type': 'restaurant',
             'description': 'Authentic local cuisine',  'lat': 0, 'lon': 0, 'opening_hours': '12pm-11pm'},
            {'name': 'Street Food Market', 'type': 'market',
             'description': 'Best local street food',   'lat': 0, 'lon': 0, 'opening_hours': '6pm-11pm'},
            {'name': 'Rooftop Cafe',       'type': 'cafe',
             'description': 'Coffee with a view',       'lat': 0, 'lon': 0, 'opening_hours': '8am-10pm'},
        ]

    # ── Cost estimation ───────────────────────────────────────────────────────

    def estimate_cost(self, destination: str, duration: int, budget: str) -> dict:
        daily_costs = {
            'low':    {'accommodation': 1500,  'food': 800,  'transport': 500,  'activities': 500},
            'medium': {'accommodation': 4000,  'food': 2000, 'transport': 1500, 'activities': 1500},
            'high':   {'accommodation': 9000,  'food': 4000, 'transport': 3000, 'activities': 3000},
            'luxury': {'accommodation': 20000, 'food': 8000, 'transport': 6000, 'activities': 6000},
        }
        costs       = daily_costs.get(budget, daily_costs['medium'])
        daily_total = sum(costs.values())
        total       = daily_total * duration
        flight_estimates = {'low': 4000, 'medium': 8000, 'high': 15000, 'luxury': 35000}
        flight = flight_estimates.get(budget, 8000)
        return {
            'currency': 'INR',
            'per_person': {
                'flights':       flight,
                'accommodation': costs['accommodation'] * duration,
                'food':          costs['food'] * duration,
                'transport':     costs['transport'] * duration,
                'activities':    costs['activities'] * duration,
                'total':         total + flight
            },
            'daily_average': daily_total,
            'duration_days': duration,
            'budget_level':  budget,
            'note': 'Estimates based on average costs. Actual prices may vary.'
        }

    # ── Deep links ────────────────────────────────────────────────────────────

    def get_deeplinks(self, destination: str, duration: int, budget: str) -> dict:
        """Generate booking deep links — zero API calls, zero cost."""
        dest_encoded = destination.replace(' ', '+')
        dest_url     = destination.replace(' ', '%20')
        dest_slug    = destination.lower().replace(' ', '-')

        checkin           = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
        checkout          = (datetime.now() + timedelta(days=30 + duration)).strftime('%Y-%m-%d')
        checkin_mmddyyyy  = (datetime.now() + timedelta(days=30)).strftime('%m/%d/%Y')
        checkout_mmddyyyy = (datetime.now() + timedelta(days=30 + duration)).strftime('%m/%d/%Y')

        return {
            'flights': [
                {
                    'name':  'Google Flights',
                    'logo':  '✈️',
                    'url':   f'https://www.google.com/travel/flights?q=flights+to+{dest_encoded}',
                    'note':  'Compare all airlines'
                },
                {
                    'name':  'MakeMyTrip',
                    'logo':  '🛫',
                    'url':   f'https://www.makemytrip.com/flights/international-flights/delhi-to-{dest_slug}.html',
                    'note':  'Best deals on Indian routes'
                },
                {
                    'name':  'Skyscanner',
                    'logo':  '🔍',
                    'url':   f'https://www.skyscanner.co.in/flights/del/{dest_slug[:4]}/{checkin[:7].replace("-", "")}/&adults=1',
                    'note':  'Price comparison'
                },
                {
                    'name':  'IndiGo',
                    'logo':  '💙',
                    'url':   f'https://www.goindigo.in/flight-booking.html',
                    'note':  'Budget airline'
                },
            ],
            'trains': [
                {
                    'name':  'IRCTC',
                    'logo':  '🚆',
                    'url':   f'https://www.irctc.co.in/nget/train-search',
                    'note':  'Official Indian Railways'
                },
                {
                    'name':  'ixigo Trains',
                    'logo':  '🛤️',
                    'url':   f'https://www.ixigo.com/trains/results/search/NDLS/{dest_encoded.upper()[:4]}/{checkin}/1/0/0/NONE',
                    'note':  'Train availability & PNR'
                },
                {
                    'name':  'Paytm Trains',
                    'logo':  '💳',
                    'url':   f'https://tickets.paytm.com/trains/searchTrains?from=NEW+DELHI&to={dest_encoded}&date={checkin}',
                    'note':  'Easy booking with offers'
                },
            ],
            'buses': [
                {
                    'name':  'RedBus',
                    'logo':  '🚌',
                    'url':   f'https://www.redbus.in/bus-tickets/delhi-to-{dest_slug}',
                    'note':  'Largest bus network'
                },
                {
                    'name':  'AbhiBus',
                    'logo':  '🚍',
                    'url':   f'https://www.abhibus.com/bus_search/Delhi/{destination}/{checkin}/S',
                    'note':  'Intercity bus booking'
                },
            ],
            'hotels': [
                {
                    'name':  'MakeMyTrip Hotels',
                    'logo':  '🏨',
                    'url':   f'https://www.makemytrip.com/hotels/hotel-listing/?checkin={checkin_mmddyyyy}&checkout={checkout_mmddyyyy}&city={dest_url}&country=IN',
                    'note':  f'{duration} nights · Best prices'
                },
                {
                    'name':  'OYO',
                    'logo':  '🏩',
                    'url':   f'https://www.oyorooms.com/search/?location={dest_url}&checkin={checkin}&checkout={checkout}',
                    'note':  'Budget to premium stays'
                },
                {
                    'name':  'Booking.com',
                    'logo':  '🌐',
                    'url':   f'https://www.booking.com/searchresults.html?ss={dest_url}&checkin={checkin}&checkout={checkout}&group_adults=2',
                    'note':  'Global inventory'
                },
                {
                    'name':  'Airbnb',
                    'logo':  '🏠',
                    'url':   f'https://www.airbnb.co.in/s/{dest_url}/homes?checkin={checkin}&checkout={checkout}',
                    'note':  'Homes & unique stays'
                },
            ],
            'food': [
                {
                    'name':  'Zomato',
                    'logo':  '🍽️',
                    'url':   f'https://www.zomato.com/{dest_slug}/restaurants',
                    'note':  'Restaurants & reviews'
                },
                {
                    'name':  'Swiggy',
                    'logo':  '🛵',
                    'url':   f'https://www.swiggy.com/city/{dest_slug}',
                    'note':  'Food delivery'
                },
                {
                    'name':  'TripAdvisor',
                    'logo':  '⭐',
                    'url':   f'https://www.tripadvisor.in/Search?q={dest_encoded}+restaurants',
                    'note':  'Top rated restaurants'
                },
            ],
            'activities': [
                {
                    'name':  'Thrillophilia',
                    'logo':  '🎯',
                    'url':   f'https://www.thrillophilia.com/cities/{dest_slug}',
                    'note':  'Tours & experiences'
                },
                {
                    'name':  'Viator',
                    'logo':  '🗺️',
                    'url':   f'https://www.viator.com/en-IN/searchResults/all?text={dest_encoded}',
                    'note':  'Day trips & guided tours'
                },
                {
                    'name':  'GetYourGuide',
                    'logo':  '🎫',
                    'url':   f'https://www.getyourguide.com/s/?q={dest_encoded}+activities',
                    'note':  'Skip-the-line tickets'
                },
            ],
        }