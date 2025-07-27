# 1. ADD render_template TO THE IMPORT
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# A list of travel destinations in India (your existing data)
travel_destinations = [
    {
        "id": 1,
        "name": "Goa",
        "season": "winter",
        "budget": "budget-friendly",
        "interests": ["beach", "nightlife", "water-sports"]
    },
    {
        "id": 2,
        "name": "Jaipur, Rajasthan",
        "season": "winter",
        "budget": "mid-range",
        "interests": ["historical", "culture", "shopping"]
    },
    {
        "id": 3,
        "name": "Rishikesh, Uttarakhand",
        "season": "any",
        "budget": "budget-friendly",
        "interests": ["spiritual", "adventure", "yoga", "mountains"]
    },
    {
        "id": 4,
        "name": "Kerala Backwaters",
        "season": "winter",
        "budget": "mid-range",
        "interests": ["nature", "relaxing", "houseboat"]
    },
    {
        "id": 5,
        "name": "Leh-Ladakh",
        "season": "summer",
        "budget": "mid-range",
        "interests": ["adventure", "mountains", "biking", "nature"]
    },
    {
        "id": 6,
        "name": "Varanasi, Uttar Pradesh",
        "season": "winter",
        "budget": "budget-friendly",
        "interests": ["spiritual", "culture", "historical"]
    },
    {
        "id": 7,
        "name": "Udaipur, Rajasthan",
        "season": "winter",
        "budget": "luxury",
        "interests": ["historical", "romance", "lakes"]
    },
    {
        "id": 8,
        "name": "Andaman and Nicobar Islands",
        "season": "winter",
        "budget": "luxury",
        "interests": ["beach", "water-sports", "scuba-diving", "nature"]
    },
    {
        "id": 9,
        "name": "Darjeeling, West Bengal",
        "season": "summer",
        "budget": "budget-friendly",
        "interests": ["mountains", "tea-gardens", "nature", "relaxing"]
    },
    {
        "id": 10,
        "name": "Hampi, Karnataka",
        "season": "winter",
        "budget": "budget-friendly",
        "interests": ["historical", "ruins", "culture"]
    },
    {
        "id": 11,
        "name": "Shimla, Himachal Pradesh",
        "season": "summer",
        "budget": "mid-range",
        "interests": ["mountains", "colonial-architecture", "relaxing"]
    },
    {
        "id": 12,
        "name": "Mumbai, Maharashtra",
        "season": "winter",
        "budget": "luxury",
        "interests": ["city-life", "nightlife", "foodie", "shopping"]
    },
    {
        "id": 13,
        "name": "Amritsar, Punjab",
        "season": "winter",
        "budget": "budget-friendly",
        "interests": ["spiritual", "historical", "foodie"]
    },
    {
        "id": 14,
        "name": "Spiti Valley, Himachal Pradesh",
        "season": "summer",
        "budget": "mid-range",
        "interests": ["adventure", "mountains", "monasteries", "road-trip"]
    },
    {
        "id": 15,
        "name": "Pondicherry",
        "season": "winter",
        "budget": "budget-friendly",
        "interests": ["beach", "french-architecture", "spiritual", "relaxing"]
    },
    {
        "id": 16,
        "name": "Meghalaya",
        "season": "any",
        "budget": "mid-range",
        "interests": ["nature", "waterfalls", "caves", "trekking"]
    },
    {
        "id": 17,
        "name": "Rann of Kutch, Gujarat",
        "season": "winter",
        "budget": "mid-range",
        "interests": ["culture", "desert", "festivals", "nature"]
    },
    {
        "id": 18,
        "name": "Munnar, Kerala",
        "season": "winter",
        "budget": "budget-friendly",
        "interests": ["tea-gardens", "nature", "mountains", "relaxing"]
    },
    {
        "id": 19,
        "name": "Ooty, Tamil Nadu",
        "season": "summer",
        "budget": "budget-friendly",
        "interests": ["hill-station", "nature", "lakes", "tea-gardens"]
    },
    {
        "id": 20,
        "name": "Coorg, Karnataka",
        "season": "any",
        "budget": "mid-range",
        "interests": ["coffee-plantations", "nature", "waterfalls", "trekking"]
    },
    {
        "id": 21,
        "name": "Mahabaleshwar, Maharashtra",
        "season": "any",
        "budget": "budget-friendly",
        "interests": ["hill-station", "nature", "lakes", "viewpoints"]
    },
    {
        "id": 22,
        "name": "Nainital, Uttarakhand",
        "season": "summer",
        "budget": "budget-friendly",
        "interests": ["hill-station", "lakes", "nature", "boating"]
    },
    {
        "id": 23,
        "name": "Manali, Himachal Pradesh",
        "season": "any",
        "budget": "budget-friendly",
        "interests": ["mountains", "adventure", "snow", "honeymoon"]
    },
    {
        "id": 24,
        "name": "Auli, Uttarakhand",
        "season": "winter",
        "budget": "mid-range",
        "interests": ["skiing", "mountains", "snow", "adventure"]
    },
    {
        "id": 25,
        "name": "Jaisalmer, Rajasthan",
        "season": "winter",
        "budget": "mid-range",
        "interests": ["desert", "historical", "camel-safari", "culture"]
    },
    {
        "id": 26,
        "name": "Khajuraho, Madhya Pradesh",
        "season": "winter",
        "budget": "budget-friendly",
        "interests": ["historical", "temples", "sculptures", "culture"]
    },
    {
        "id": 27,
        "name": "Agra, Uttar Pradesh",
        "season": "winter",
        "budget": "budget-friendly",
        "interests": ["historical", "monuments", "culture", "romance"]
    },
    {
        "id": 28,
        "name": "Delhi",
        "season": "winter",
        "budget": "mid-range",
        "interests": ["historical", "city-life", "foodie", "shopping"]
    },
    {
        "id": 29,
        "name": "Kolkata, West Bengal",
        "season": "winter",
        "budget": "budget-friendly",
        "interests": ["culture", "historical", "foodie", "city-life"]
    },
    {
        "id": 30,
        "name": "Hyderabad, Telangana",
        "season": "winter",
        "budget": "mid-range",
        "interests": ["historical", "foodie", "city-life", "culture"]
    },
    {
        "id": 31,
        "name": "Bangalore, Karnataka",
        "season": "any",
        "budget": "luxury",
        "interests": ["city-life", "gardens", "nightlife", "foodie"]
    },
    {
        "id": 32,
        "name": "Chennai, Tamil Nadu",
        "season": "winter",
        "budget": "mid-range",
        "interests": ["city-life", "beach", "temples", "culture"]
    },
    {
        "id": 33,
        "name": "Kaziranga National Park, Assam",
        "season": "winter",
        "budget": "mid-range",
        "interests": ["wildlife", "nature", "safari", "national-park"]
    },
    {
        "id": 34,
        "name": "Sundarbans National Park, West Bengal",
        "season": "winter",
        "budget": "mid-range",
        "interests": ["wildlife", "nature", "mangroves", "boating"]
    },
    {
        "id": 35,
        "name": "Gokarna, Karnataka",
        "season": "winter",
        "budget": "budget-friendly",
        "interests": ["beach", "relaxing", "spiritual", "trekking"]
    }
]


# 2. ADD THIS NEW ROUTE TO SERVE THE WEBPAGE
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend():
    budget = request.args.get('budget')
    season = request.args.get('season')
    interests_str = request.args.get('interests')

    filtered_destinations = travel_destinations

    if budget:
        filtered_destinations = [dest for dest in filtered_destinations if dest['budget'].lower() == budget.lower()]

    if season:
        filtered_destinations = [dest for dest in filtered_destinations if dest['season'].lower() == season.lower() or dest['season'].lower() == 'any']

    if interests_str:
        interests = [interest.strip().lower() for interest in interests_str.split(',')]
        # --- THIS IS THE ONLY LINE THAT HAS CHANGED ---
        # We changed all() to any() to make the search more flexible.
        filtered_destinations = [dest for dest in filtered_destinations if any(interest in dest['interests'] for interest in interests)]

    return jsonify(filtered_destinations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)