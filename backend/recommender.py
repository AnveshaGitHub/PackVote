from collections import defaultdict


class RecommendationEngine:

    DESTINATIONS = {
        # ── INDIA ─────────────────────────────────────────────────────────────

        # Metro Cities
        'Mumbai': {
            'tags': ['culture', 'food', 'nightlife', 'shopping', 'history', 'beach'],
            'budget_level': 'medium',
            'best_months': ['November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 60,
            'description': 'The city of dreams — Bollywood, street food and the sea'
        },
        'Delhi': {
            'tags': ['history', 'culture', 'food', 'art', 'shopping'],
            'budget_level': 'medium',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 55,
            'description': 'India\'s capital — Mughal monuments and chaotic bazaars'
        },
        'Bangalore': {
            'tags': ['nightlife', 'food', 'technology', 'culture', 'shopping'],
            'budget_level': 'medium',
            'best_months': ['October', 'November', 'December', 'January', 'February'],
            'avg_cost_per_day': 60,
            'description': 'Garden city and India\'s Silicon Valley'
        },
        'Chennai': {
            'tags': ['culture', 'history', 'food', 'beach', 'art'],
            'budget_level': 'low',
            'best_months': ['November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 45,
            'description': 'Gateway to South India — temples, classical arts and beaches'
        },
        'Kolkata': {
            'tags': ['culture', 'history', 'food', 'art', 'music'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February'],
            'avg_cost_per_day': 40,
            'description': 'City of joy — colonial charm, literature and street food'
        },
        'Hyderabad': {
            'tags': ['history', 'food', 'culture', 'shopping', 'technology'],
            'budget_level': 'medium',
            'best_months': ['October', 'November', 'December', 'January', 'February'],
            'avg_cost_per_day': 50,
            'description': 'City of pearls, biryani and Nizami heritage'
        },
        'Pune': {
            'tags': ['culture', 'food', 'nightlife', 'history', 'nature'],
            'budget_level': 'medium',
            'best_months': ['October', 'November', 'December', 'January', 'February'],
            'avg_cost_per_day': 55,
            'description': 'Oxford of the East — vibrant student city with forts'
        },
        'Ahmedabad': {
            'tags': ['history', 'culture', 'food', 'art', 'shopping'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 40,
            'description': 'UNESCO heritage city — stepwells, textiles and Gandhi\'s ashram'
        },

        # Rajasthan
        'Jaipur': {
            'tags': ['history', 'culture', 'art', 'shopping', 'food'],
            'budget_level': 'medium',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 55,
            'description': 'The Pink City — palaces, forts and vibrant bazaars'
        },
        'Udaipur': {
            'tags': ['romance', 'history', 'culture', 'art', 'nature'],
            'budget_level': 'medium',
            'best_months': ['September', 'October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 60,
            'description': 'City of lakes — the most romantic city in India'
        },
        'Jodhpur': {
            'tags': ['history', 'culture', 'adventure', 'art', 'food'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 45,
            'description': 'The Blue City — Mehrangarh Fort and desert landscapes'
        },
        'Jaisalmer': {
            'tags': ['adventure', 'history', 'culture', 'nature', 'romance'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 50,
            'description': 'Golden city rising from the Thar Desert'
        },
        'Pushkar': {
            'tags': ['culture', 'wellness', 'history', 'nature', 'food'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 35,
            'description': 'Sacred lake town — camel fair and Brahma temple'
        },
        'Bikaner': {
            'tags': ['history', 'culture', 'food', 'adventure'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February'],
            'avg_cost_per_day': 35,
            'description': 'Desert city of ornate havelis and camel festivals'
        },
        'Ajmer': {
            'tags': ['history', 'culture', 'wellness', 'food'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 35,
            'description': 'Dargah Sharif — spiritual heart of Rajasthan'
        },

        # Goa
        'Goa': {
            'tags': ['beach', 'nightlife', 'food', 'culture', 'adventure'],
            'budget_level': 'medium',
            'best_months': ['November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 65,
            'description': 'India\'s beach paradise — sun, seafood and parties'
        },
        'North Goa': {
            'tags': ['beach', 'nightlife', 'food', 'adventure', 'shopping'],
            'budget_level': 'medium',
            'best_months': ['November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 70,
            'description': 'Lively beaches, shacks and legendary nightlife'
        },
        'South Goa': {
            'tags': ['beach', 'romance', 'wellness', 'nature', 'culture'],
            'budget_level': 'medium',
            'best_months': ['November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 75,
            'description': 'Serene beaches and luxury resorts away from crowds'
        },

        # Kerala
        'Kochi': {
            'tags': ['culture', 'history', 'food', 'art', 'nature'],
            'budget_level': 'medium',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 55,
            'description': 'Queen of the Arabian Sea — spices, backwaters and Chinese nets'
        },
        'Munnar': {
            'tags': ['nature', 'adventure', 'wellness', 'romance'],
            'budget_level': 'medium',
            'best_months': ['September', 'October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 60,
            'description': 'Rolling tea gardens in the misty Western Ghats'
        },
        'Alleppey': {
            'tags': ['nature', 'romance', 'wellness', 'culture', 'adventure'],
            'budget_level': 'medium',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 65,
            'description': 'Venice of the East — houseboat cruises on the backwaters'
        },
        'Thekkady': {
            'tags': ['nature', 'adventure', 'wildlife', 'wellness'],
            'budget_level': 'medium',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 55,
            'description': 'Periyar wildlife sanctuary — elephants and spice plantations'
        },
        'Kovalam': {
            'tags': ['beach', 'wellness', 'romance', 'nature'],
            'budget_level': 'medium',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 60,
            'description': 'Crescent beaches and Ayurvedic retreats'
        },
        'Wayanad': {
            'tags': ['nature', 'adventure', 'wildlife', 'wellness', 'culture'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 50,
            'description': 'Green hills, tribal culture and ancient caves'
        },
        'Thiruvananthapuram': {
            'tags': ['culture', 'history', 'beach', 'food', 'wellness'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 45,
            'description': 'Capital of Kerala — temples, beaches and Padmanabhaswamy'
        },

        # Himachal Pradesh
        'Shimla': {
            'tags': ['nature', 'adventure', 'romance', 'history', 'culture'],
            'budget_level': 'medium',
            'best_months': ['March', 'April', 'May', 'June', 'October', 'November', 'December', 'January', 'February'],
            'avg_cost_per_day': 55,
            'description': 'Queen of hills — colonial charm and snow-capped peaks'
        },
        'Manali': {
            'tags': ['adventure', 'nature', 'romance', 'culture'],
            'budget_level': 'medium',
            'best_months': ['March', 'April', 'May', 'June', 'October', 'November'],
            'avg_cost_per_day': 60,
            'description': 'Adventure capital — skiing, trekking and Rohtang Pass'
        },
        'Dharamsala': {
            'tags': ['culture', 'wellness', 'nature', 'adventure', 'history'],
            'budget_level': 'low',
            'best_months': ['March', 'April', 'May', 'September', 'October', 'November'],
            'avg_cost_per_day': 45,
            'description': 'Home of the Dalai Lama — Tibetan culture in the Himalayas'
        },
        'Spiti Valley': {
            'tags': ['adventure', 'nature', 'culture', 'history'],
            'budget_level': 'low',
            'best_months': ['June', 'July', 'August', 'September'],
            'avg_cost_per_day': 40,
            'description': 'Cold desert mountain valley — monasteries and dramatic landscapes'
        },
        'Kasol': {
            'tags': ['adventure', 'nature', 'wellness', 'culture'],
            'budget_level': 'low',
            'best_months': ['March', 'April', 'May', 'June', 'September', 'October'],
            'avg_cost_per_day': 35,
            'description': 'Mini Israel of India — trekking and Parvati Valley'
        },
        'Dalhousie': {
            'tags': ['nature', 'romance', 'history', 'wellness'],
            'budget_level': 'low',
            'best_months': ['March', 'April', 'May', 'June', 'October', 'November'],
            'avg_cost_per_day': 45,
            'description': 'Colonial hill station with Himalayan panoramas'
        },

        # Uttarakhand
        'Rishikesh': {
            'tags': ['wellness', 'adventure', 'culture', 'nature', 'history'],
            'budget_level': 'low',
            'best_months': ['February', 'March', 'April', 'May', 'September', 'October', 'November'],
            'avg_cost_per_day': 40,
            'description': 'Yoga capital of the world — rafting and Ganges ghats'
        },
        'Haridwar': {
            'tags': ['culture', 'wellness', 'history', 'nature'],
            'budget_level': 'low',
            'best_months': ['February', 'March', 'April', 'October', 'November'],
            'avg_cost_per_day': 35,
            'description': 'Gateway to the gods — Ganga Aarti and sacred ghats'
        },
        'Nainital': {
            'tags': ['nature', 'romance', 'adventure', 'culture'],
            'budget_level': 'medium',
            'best_months': ['March', 'April', 'May', 'June', 'October', 'November'],
            'avg_cost_per_day': 55,
            'description': 'Lake district of India — boating and Kumaon hills'
        },
        'Mussoorie': {
            'tags': ['nature', 'romance', 'adventure', 'history'],
            'budget_level': 'medium',
            'best_months': ['March', 'April', 'May', 'June', 'October', 'November'],
            'avg_cost_per_day': 55,
            'description': 'Queen of hill stations — waterfalls and Kempty Falls'
        },
        'Auli': {
            'tags': ['adventure', 'nature', 'romance'],
            'budget_level': 'medium',
            'best_months': ['January', 'February', 'March', 'April', 'May'],
            'avg_cost_per_day': 60,
            'description': 'India\'s top ski resort with Himalayan views'
        },

        # Uttar Pradesh
        'Agra': {
            'tags': ['history', 'culture', 'romance', 'art'],
            'budget_level': 'medium',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 50,
            'description': 'Home of the Taj Mahal — Mughal architecture at its finest'
        },
        'Varanasi': {
            'tags': ['culture', 'history', 'wellness', 'food', 'art'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 40,
            'description': 'Oldest living city — ghats, rituals and spiritual energy'
        },
        'Lucknow': {
            'tags': ['food', 'history', 'culture', 'art', 'shopping'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 40,
            'description': 'City of nawabs — kebabs, biryani and chikankari'
        },
        'Mathura': {
            'tags': ['culture', 'history', 'wellness', 'food'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 30,
            'description': 'Birthplace of Lord Krishna — temples and Holi celebrations'
        },
        'Vrindavan': {
            'tags': ['culture', 'wellness', 'history'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 30,
            'description': 'Sacred land of Krishna — 5000 temples and devotion'
        },

        # Tamil Nadu
        'Ooty': {
            'tags': ['nature', 'romance', 'adventure', 'culture'],
            'budget_level': 'low',
            'best_months': ['April', 'May', 'June', 'September', 'October', 'November'],
            'avg_cost_per_day': 45,
            'description': 'Queen of hill stations — tea gardens and toy train'
        },
        'Kodaikanal': {
            'tags': ['nature', 'romance', 'wellness', 'adventure'],
            'budget_level': 'low',
            'best_months': ['April', 'May', 'June', 'September', 'October'],
            'avg_cost_per_day': 45,
            'description': 'Princess of hill stations — misty lakes and waterfalls'
        },
        'Madurai': {
            'tags': ['history', 'culture', 'food', 'art'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 35,
            'description': 'Temple city — Meenakshi Amman and ancient Dravidian culture'
        },
        'Mahabalipuram': {
            'tags': ['history', 'culture', 'beach', 'art'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 40,
            'description': 'UNESCO shore temples and rock-cut sculptures by the sea'
        },
        'Pondicherry': {
            'tags': ['culture', 'beach', 'food', 'wellness', 'history'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 50,
            'description': 'French Riviera of India — promenades, cafes and ashrams'
        },
        'Rameswaram': {
            'tags': ['culture', 'history', 'wellness', 'beach'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 30,
            'description': 'Sacred island town — Ramanathaswamy temple and Pamban bridge'
        },

        # Karnataka
        'Mysuru': {
            'tags': ['history', 'culture', 'food', 'art', 'nature'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 45,
            'description': 'City of palaces — grand Dasara celebrations and sandalwood'
        },
        'Hampi': {
            'tags': ['history', 'culture', 'adventure', 'art', 'nature'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 35,
            'description': 'UNESCO ruins of the Vijayanagara Empire amid boulders'
        },
        'Coorg': {
            'tags': ['nature', 'adventure', 'wellness', 'romance', 'food'],
            'budget_level': 'medium',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 65,
            'description': 'Scotland of India — coffee estates and misty hills'
        },
        'Gokarna': {
            'tags': ['beach', 'culture', 'wellness', 'adventure', 'nature'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 40,
            'description': 'Unspoilt beaches and sacred Shiva temple'
        },
        'Badami': {
            'tags': ['history', 'culture', 'adventure', 'art'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 30,
            'description': 'Cave temples carved into red sandstone cliffs'
        },

        # Northeast India
        'Gangtok': {
            'tags': ['nature', 'adventure', 'culture', 'romance'],
            'budget_level': 'medium',
            'best_months': ['March', 'April', 'May', 'October', 'November', 'December'],
            'avg_cost_per_day': 55,
            'description': 'Sikkim\'s capital — monasteries and Kanchenjunga views'
        },
        'Darjeeling': {
            'tags': ['nature', 'romance', 'culture', 'food', 'adventure'],
            'budget_level': 'medium',
            'best_months': ['March', 'April', 'May', 'October', 'November'],
            'avg_cost_per_day': 50,
            'description': 'Queen of hills — tea estates and Tiger Hill sunrise'
        },
        'Shillong': {
            'tags': ['nature', 'adventure', 'culture', 'music'],
            'budget_level': 'low',
            'best_months': ['September', 'October', 'November', 'December', 'January', 'February', 'March', 'April'],
            'avg_cost_per_day': 45,
            'description': 'Scotland of the East — living root bridges and waterfalls'
        },
        'Kaziranga': {
            'tags': ['nature', 'adventure', 'wildlife'],
            'budget_level': 'medium',
            'best_months': ['November', 'December', 'January', 'February', 'March', 'April'],
            'avg_cost_per_day': 70,
            'description': 'UNESCO national park — one-horned rhinos and Bengal tigers'
        },
        'Tawang': {
            'tags': ['culture', 'nature', 'adventure', 'history'],
            'budget_level': 'medium',
            'best_months': ['March', 'April', 'May', 'June', 'September', 'October'],
            'avg_cost_per_day': 55,
            'description': 'Remote Arunachal monastery town near the Himalayas'
        },
        'Ziro': {
            'tags': ['nature', 'culture', 'music', 'adventure'],
            'budget_level': 'low',
            'best_months': ['March', 'April', 'May', 'September', 'October'],
            'avg_cost_per_day': 40,
            'description': 'UNESCO rice fields and famous Ziro music festival'
        },

        # Gujarat
        'Rann of Kutch': {
            'tags': ['nature', 'culture', 'adventure', 'art'],
            'budget_level': 'medium',
            'best_months': ['November', 'December', 'January', 'February'],
            'avg_cost_per_day': 55,
            'description': 'White salt desert — Rann Utsav festival under the stars'
        },
        'Dwarka': {
            'tags': ['culture', 'history', 'wellness', 'beach'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 35,
            'description': 'Ancient sacred city — Krishna\'s kingdom on the Arabian Sea'
        },
        'Somnath': {
            'tags': ['history', 'culture', 'wellness', 'beach'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 35,
            'description': 'First of 12 Jyotirlinga temples — rebuilt through the ages'
        },
        'Saputara': {
            'tags': ['nature', 'adventure', 'romance', 'wellness'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March', 'June', 'July'],
            'avg_cost_per_day': 40,
            'description': 'Gujarat\'s only hill station — tribal culture and misty valleys'
        },

        # Madhya Pradesh
        'Khajuraho': {
            'tags': ['history', 'culture', 'art'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 40,
            'description': 'UNESCO temples — medieval erotic sculptures and artistry'
        },
        'Orchha': {
            'tags': ['history', 'culture', 'nature', 'art'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 35,
            'description': 'Forgotten Bundelkhand kingdom — cenotaphs and riverside forts'
        },
        'Bandhavgarh': {
            'tags': ['nature', 'adventure', 'wildlife'],
            'budget_level': 'high',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March', 'April', 'May'],
            'avg_cost_per_day': 120,
            'description': 'Highest density of Bengal tigers in India'
        },
        'Pachmarhi': {
            'tags': ['nature', 'adventure', 'wellness', 'history'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March', 'April', 'May'],
            'avg_cost_per_day': 40,
            'description': 'Queen of Satpura — waterfalls, caves and dense forests'
        },
        'Bhopal': {
            'tags': ['history', 'culture', 'food', 'nature'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 35,
            'description': 'City of lakes — Bhimbetka caves and kebab culture'
        },

        # Andaman & Lakshadweep
        'Port Blair': {
            'tags': ['beach', 'history', 'nature', 'adventure'],
            'budget_level': 'medium',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March', 'April', 'May'],
            'avg_cost_per_day': 65,
            'description': 'Gateway to Andamans — Cellular Jail and coral reefs'
        },
        'Havelock Island': {
            'tags': ['beach', 'adventure', 'nature', 'romance', 'wellness'],
            'budget_level': 'medium',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March', 'April', 'May'],
            'avg_cost_per_day': 75,
            'description': 'Radhanagar Beach — Asia\'s best beach and scuba diving'
        },
        'Neil Island': {
            'tags': ['beach', 'nature', 'romance', 'wellness'],
            'budget_level': 'medium',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 65,
            'description': 'Quiet island paradise — natural bridge and clear waters'
        },
        'Lakshadweep': {
            'tags': ['beach', 'nature', 'adventure', 'romance', 'wellness'],
            'budget_level': 'high',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March', 'April', 'May'],
            'avg_cost_per_day': 150,
            'description': 'India\'s coral archipelago — lagoons and pristine reefs'
        },

        # Jammu & Kashmir / Ladakh
        'Srinagar': {
            'tags': ['romance', 'nature', 'culture', 'history', 'adventure'],
            'budget_level': 'medium',
            'best_months': ['April', 'May', 'June', 'September', 'October'],
            'avg_cost_per_day': 65,
            'description': 'Paradise on earth — Dal Lake houseboats and Mughal gardens'
        },
        'Leh Ladakh': {
            'tags': ['adventure', 'nature', 'culture', 'history'],
            'budget_level': 'medium',
            'best_months': ['June', 'July', 'August', 'September'],
            'avg_cost_per_day': 70,
            'description': 'Roof of the world — monasteries, lakes and mountain passes'
        },
        'Gulmarg': {
            'tags': ['adventure', 'nature', 'romance', 'wellness'],
            'budget_level': 'medium',
            'best_months': ['December', 'January', 'February', 'March', 'April', 'May', 'June'],
            'avg_cost_per_day': 80,
            'description': 'Meadow of flowers — Asia\'s highest gondola and skiing'
        },
        'Pahalgam': {
            'tags': ['nature', 'adventure', 'romance', 'wellness'],
            'budget_level': 'medium',
            'best_months': ['April', 'May', 'June', 'September', 'October'],
            'avg_cost_per_day': 65,
            'description': 'Valley of shepherds — Lidder River and Betaab Valley'
        },

        # Odisha
        'Puri': {
            'tags': ['culture', 'history', 'beach', 'food', 'wellness'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 35,
            'description': 'Jagannath Dham — sacred beach town and Rath Yatra'
        },
        'Konark': {
            'tags': ['history', 'culture', 'art', 'beach'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 30,
            'description': 'UNESCO Sun Temple — masterpiece of Kalinga architecture'
        },
        'Bhubaneswar': {
            'tags': ['history', 'culture', 'food', 'art'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 35,
            'description': 'Temple city of India — over 700 ancient temples'
        },

        # Maharashtra
        'Aurangabad': {
            'tags': ['history', 'culture', 'art'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 40,
            'description': 'Gateway to Ajanta and Ellora — UNESCO cave masterpieces'
        },
        'Lonavala': {
            'tags': ['nature', 'adventure', 'romance', 'wellness'],
            'budget_level': 'medium',
            'best_months': ['June', 'July', 'August', 'September', 'October', 'November'],
            'avg_cost_per_day': 55,
            'description': 'Hill station getaway from Mumbai — forts and waterfalls'
        },
        'Mahabaleshwar': {
            'tags': ['nature', 'romance', 'food', 'wellness'],
            'budget_level': 'medium',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March', 'April', 'May'],
            'avg_cost_per_day': 60,
            'description': 'Strawberry capital of India — valley viewpoints and cool air'
        },
        'Nashik': {
            'tags': ['culture', 'food', 'history', 'nature'],
            'budget_level': 'low',
            'best_months': ['October', 'November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 40,
            'description': 'Wine capital of India and sacred Kumbh Mela city'
        },

        # ── INTERNATIONAL ──────────────────────────────────────────────────────

        'Paris': {
            'tags': ['culture', 'food', 'romance', 'art', 'history'],
            'budget_level': 'high',
            'best_months': ['April', 'May', 'June', 'September', 'October'],
            'avg_cost_per_day': 200,
            'description': 'City of lights, art and cuisine'
        },
        'Tokyo': {
            'tags': ['culture', 'food', 'technology', 'adventure', 'shopping'],
            'budget_level': 'high',
            'best_months': ['March', 'April', 'October', 'November'],
            'avg_cost_per_day': 180,
            'description': 'Ultra-modern meets ancient tradition'
        },
        'Bali': {
            'tags': ['beach', 'adventure', 'nature', 'wellness', 'culture'],
            'budget_level': 'low',
            'best_months': ['April', 'May', 'June', 'July', 'August', 'September'],
            'avg_cost_per_day': 80,
            'description': 'Tropical paradise with rich spiritual culture'
        },
        'Bangkok': {
            'tags': ['food', 'culture', 'adventure', 'shopping', 'nightlife'],
            'budget_level': 'low',
            'best_months': ['November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 60,
            'description': 'Street food capital with stunning temples'
        },
        'Dubai': {
            'tags': ['luxury', 'shopping', 'adventure', 'food', 'nightlife'],
            'budget_level': 'luxury',
            'best_months': ['November', 'December', 'January', 'February', 'March', 'April'],
            'avg_cost_per_day': 250,
            'description': 'City of superlatives — tallest, largest, most luxurious'
        },
        'Singapore': {
            'tags': ['food', 'culture', 'shopping', 'technology', 'nightlife'],
            'budget_level': 'high',
            'best_months': ['February', 'March', 'April', 'July', 'August'],
            'avg_cost_per_day': 160,
            'description': 'Lion city — a melting pot of cultures and cuisines'
        },
        'Maldives': {
            'tags': ['beach', 'romance', 'wellness', 'nature', 'luxury'],
            'budget_level': 'luxury',
            'best_months': ['November', 'December', 'January', 'February', 'March', 'April'],
            'avg_cost_per_day': 400,
            'description': 'Paradise overwater bungalows and crystal seas'
        },
        'Sri Lanka': {
            'tags': ['culture', 'beach', 'nature', 'history', 'food', 'adventure'],
            'budget_level': 'low',
            'best_months': ['December', 'January', 'February', 'March', 'April'],
            'avg_cost_per_day': 55,
            'description': 'Pearl of the Indian Ocean — temples, tea and leopards'
        },
        'Nepal': {
            'tags': ['adventure', 'nature', 'culture', 'history', 'wellness'],
            'budget_level': 'low',
            'best_months': ['March', 'April', 'May', 'October', 'November'],
            'avg_cost_per_day': 45,
            'description': 'Roof of the world — Everest base camp and Kathmandu'
        },
        'Bhutan': {
            'tags': ['culture', 'nature', 'wellness', 'history', 'adventure'],
            'budget_level': 'high',
            'best_months': ['March', 'April', 'May', 'September', 'October', 'November'],
            'avg_cost_per_day': 200,
            'description': 'Last Shangri-La — happiness index and Tiger\'s Nest monastery'
        },
        'Vietnam': {
            'tags': ['food', 'culture', 'history', 'nature', 'adventure', 'beach'],
            'budget_level': 'low',
            'best_months': ['February', 'March', 'April', 'August', 'September'],
            'avg_cost_per_day': 50,
            'description': 'From Hanoi phở to Ha Long Bay — a country of contrasts'
        },
        'Barcelona': {
            'tags': ['beach', 'culture', 'food', 'nightlife', 'art', 'history'],
            'budget_level': 'medium',
            'best_months': ['May', 'June', 'September', 'October'],
            'avg_cost_per_day': 150,
            'description': 'Vibrant city of Gaudi and Mediterranean vibes'
        },
        'New York': {
            'tags': ['culture', 'food', 'shopping', 'nightlife', 'art'],
            'budget_level': 'high',
            'best_months': ['April', 'May', 'September', 'October'],
            'avg_cost_per_day': 250,
            'description': 'The city that never sleeps'
        },
        'London': {
            'tags': ['history', 'culture', 'food', 'art', 'shopping', 'nightlife'],
            'budget_level': 'high',
            'best_months': ['May', 'June', 'July', 'August', 'September'],
            'avg_cost_per_day': 220,
            'description': 'Royal history meets modern multiculturalism'
        },
        'Cape Town': {
            'tags': ['nature', 'adventure', 'beach', 'culture', 'food'],
            'budget_level': 'medium',
            'best_months': ['November', 'December', 'January', 'February', 'March'],
            'avg_cost_per_day': 100,
            'description': 'Where mountains meet the ocean'
        },
    }

    ALL_TAGS = ['culture', 'food', 'romance', 'art', 'history', 'technology',
                'adventure', 'shopping', 'beach', 'nature', 'wellness',
                'nightlife', 'luxury', 'music', 'wildlife']

    def get_recommendations(self, consensus: dict) -> list:
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
                'match_percentage': min(100, round(score)),
                'description': info['description'],
                'avg_cost_per_day': info['avg_cost_per_day'],
                'best_months': info['best_months'],
                'tags': info['tags'],
                'budget_level': info['budget_level']
            })

        scored.sort(key=lambda x: x['score'], reverse=True)
        return scored[:5]

    def _score_destination(self, dest, info, top_styles, budget, month) -> float:
        score = 0.0
        dest_tags = info.get('tags', [])
        matches = sum(1 for style in top_styles if style in dest_tags)
        if top_styles:
            score += (matches / len(top_styles)) * 50

        budget_map = {'low': 1, 'medium': 2, 'high': 3, 'luxury': 4}
        dest_budget = budget_map.get(info.get('budget_level', 'medium'), 2)
        user_budget = budget_map.get(budget, 2)
        score += max(0, 30 - abs(dest_budget - user_budget) * 10)

        if month in info.get('best_months', []):
            score += 20

        return score

    def get_similar_destinations(self, destination: str) -> list:
        if destination not in self.DESTINATIONS:
            return []
        base_tags = set(self.DESTINATIONS[destination]['tags'])
        similar = []
        for dest, info in self.DESTINATIONS.items():
            if dest == destination:
                continue
            overlap = len(base_tags & set(info['tags']))
            if overlap >= 2:
                similar.append({
                    'destination': dest,
                    'shared_tags': list(base_tags & set(info['tags'])),
                    'description': info['description']
                })
        similar.sort(key=lambda x: len(x['shared_tags']), reverse=True)
        return similar[:3]