import requests


class TravelAPI:
    """
    Handles all external API calls.
    All APIs used are FREE tier.
    """

    # ── Free API endpoints ────────────────────────────────────────────────────
    NOMINATIM_URL    = "https://nominatim.openstreetmap.org/search"
    WEATHER_URL      = "https://wttr.in"
    EXCHANGE_URL     = "https://api.exchangerate-api.com/v4/latest/INR"

    HEADERS = {'User-Agent': 'PackVote/1.0 (travel planning app)'}

    # ── Destination search ────────────────────────────────────────────────────

    def search_destination(self, query: str) -> list:
        """Search for destinations using OpenStreetMap Nominatim (free)."""
        try:
            params = {
                'q': query,
                'format': 'json',
                'limit': 5,
                'addressdetails': 1
            }
            res = requests.get(self.NOMINATIM_URL,
                               params=params,
                               headers=self.HEADERS,
                               timeout=5)
            data = res.json()
            return [
                {
                    'name': item.get('display_name', '').split(',')[0],
                    'full_name': item.get('display_name', ''),
                    'lat': float(item.get('lat', 0)),
                    'lon': float(item.get('lon', 0)),
                    'type': item.get('type', '')
                }
                for item in data
            ]
        except Exception as e:
            print(f"Nominatim search error: {e}")
            return []

    def get_coordinates(self, destination: str) -> dict:
        """Get lat/lon for a destination."""
        results = self.search_destination(destination)
        if results:
            return {'lat': results[0]['lat'], 'lon': results[0]['lon']}
        return {'lat': 20.5937, 'lon': 78.9629}  # default: centre of India

    # ── Weather ───────────────────────────────────────────────────────────────

    def get_weather(self, destination: str) -> dict:
        """Get weather using wttr.in (completely free, no API key needed)."""
        try:
            url = f"{self.WEATHER_URL}/{destination}?format=j1"
            res = requests.get(url, headers=self.HEADERS, timeout=5)
            data = res.json()

            current = data['current_condition'][0]
            weather_desc = current['weatherDesc'][0]['value']
            temp_c       = current['temp_C']
            humidity     = current['humidity']
            feels_like   = current['FeelsLikeC']

            # 3-day forecast
            forecast = []
            for day in data.get('weather', [])[:3]:
                forecast.append({
                    'date': day['date'],
                    'max_temp': day['maxtempC'],
                    'min_temp': day['mintempC'],
                    'description': day['hourly'][4]['weatherDesc'][0]['value']
                })

            return {
                'destination': destination,
                'temperature_c': temp_c,
                'feels_like_c': feels_like,
                'humidity': humidity,
                'description': weather_desc,
                'forecast': forecast
            }

        except Exception as e:
            print(f"Weather API error: {e}")
            return {
                'destination': destination,
                'temperature_c': 'N/A',
                'humidity': 'N/A',
                'description': 'Weather data unavailable',
                'forecast': []
            }

    # ── Places ────────────────────────────────────────────────────────────────

    def get_places(self, destination: str, travel_styles: list) -> dict:
        """Get attractions and restaurants using Nominatim (free)."""
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
        """Query Overpass API (free OpenStreetMap data)."""
        try:
            # Build Overpass QL query
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

            radius = 10000  # 10km radius
            overpass_url = "https://overpass-api.de/api/interpreter"

            filters = '|'.join(list(osm_types)[:5])
            query = f"""
            [out:json][timeout:10];
            node["{category}"~"{filters}"](around:{radius},{lat},{lon});
            out 10;
            """

            res = requests.post(overpass_url,
                                data={'data': query},
                                timeout=10)
            elements = res.json().get('elements', [])

            places = []
            for el in elements:
                tags = el.get('tags', {})
                name = tags.get('name', '')
                if name:
                    places.append({
                        'name': name,
                        'type': tags.get(category, 'place'),
                        'lat': el.get('lat', lat),
                        'lon': el.get('lon', lon),
                        'description': tags.get('description', ''),
                        'opening_hours': tags.get('opening_hours', 'Check locally')
                    })
            return places

        except Exception as e:
            print(f"Overpass API error: {e}")
            return self._fallback_places(category)

    def _fallback_places(self, category: str) -> list:
        """Fallback if API fails."""
        if category == 'tourism':
            return [
                {'name': 'City Museum', 'type': 'museum',
                 'description': 'Local heritage museum', 'lat': 0, 'lon': 0},
                {'name': 'Central Park', 'type': 'park',
                 'description': 'Main city park', 'lat': 0, 'lon': 0},
                {'name': 'Historic Fort', 'type': 'ruins',
                 'description': 'Ancient fortification', 'lat': 0, 'lon': 0},
            ]
        return [
            {'name': 'Local Restaurant', 'type': 'restaurant',
             'description': 'Authentic local cuisine', 'lat': 0, 'lon': 0},
            {'name': 'Street Food Market', 'type': 'market',
             'description': 'Best local street food', 'lat': 0, 'lon': 0},
        ]

    # ── Cost estimation ───────────────────────────────────────────────────────

    def estimate_cost(self, destination: str,
                      duration: int, budget: str) -> dict:
        """Estimate trip cost per person in INR."""

        daily_costs = {
            'low':    {'accommodation': 1500, 'food': 800,  'transport': 500,  'activities': 500},
            'medium': {'accommodation': 4000, 'food': 2000, 'transport': 1500, 'activities': 1500},
            'high':   {'accommodation': 9000, 'food': 4000, 'transport': 3000, 'activities': 3000},
            'luxury': {'accommodation': 20000,'food': 8000, 'transport': 6000, 'activities': 6000},
        }

        costs = daily_costs.get(budget, daily_costs['medium'])
        daily_total = sum(costs.values())
        total       = daily_total * duration

        # Flight estimate (rough average from major Indian cities)
        flight_estimates = {
            'low': 4000, 'medium': 8000, 'high': 15000, 'luxury': 35000
        }
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
            'budget_level': budget,
            'note': 'Estimates based on average costs. Actual prices may vary.'
        }