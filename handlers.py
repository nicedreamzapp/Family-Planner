"""
JSON file handlers for Family Family Hub.
"""
import json
import os

# Data file paths
DATA_DIR = os.path.dirname(os.path.abspath(__file__))
CALENDAR_FILE = os.path.join(DATA_DIR, "calendar.json")
CHORES_FILE = os.path.join(DATA_DIR, "chores.json")
REWARDS_FILE = os.path.join(DATA_DIR, "rewards.json")
MEALS_FILE = os.path.join(DATA_DIR, "meals.json")
SHOPPING_FILE = os.path.join(DATA_DIR, "shopping.json")
TVSHOWS_FILE = os.path.join(DATA_DIR, "tvshows.json")
NOTES_FILE = os.path.join(DATA_DIR, "notes.json")


def load_json(filepath, default):
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except:
            pass
    return default


def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)


def get_calendar():
    return load_json(CALENDAR_FILE, {"events": []})


def get_chores():
    return load_json(CHORES_FILE, {
        "chores": [
            {"id": 1, "name": "Make bed", "points": 5, "assignedTo": ["kid1", "kid2"], "icon": "🛏️"},
            {"id": 2, "name": "Brush teeth (morning)", "points": 3, "assignedTo": ["kid1", "kid2"], "icon": "🦷"},
            {"id": 3, "name": "Brush teeth (night)", "points": 3, "assignedTo": ["kid1", "kid2"], "icon": "🦷"},
            {"id": 4, "name": "Clean room", "points": 10, "assignedTo": ["kid1", "kid2"], "icon": "🧹"},
            {"id": 5, "name": "Set table", "points": 5, "assignedTo": ["kid1", "kid2"], "icon": "🍽️"},
            {"id": 6, "name": "Clear table", "points": 5, "assignedTo": ["kid1", "kid2"], "icon": "🧽"},
            {"id": 7, "name": "Homework done", "points": 15, "assignedTo": ["kid1", "kid2"], "icon": "📚"},
            {"id": 8, "name": "Practice reading", "points": 10, "assignedTo": ["kid1", "kid2"], "icon": "📖"},
            {"id": 9, "name": "Help with dishes", "points": 8, "assignedTo": ["kid1", "kid2"], "icon": "🍳"},
            {"id": 10, "name": "Be kind to sister", "points": 5, "assignedTo": ["kid1", "kid2"], "icon": "💕"}
        ],
        "completed": []
    })


def get_rewards():
    rewards = load_json(REWARDS_FILE, {
        "points": {"kid1": 0, "kid2": 0},
        "rewards": [
            {"id": 1, "name": "Extra screen time (30 min)", "cost": 50, "icon": "📱"},
            {"id": 2, "name": "Pick what's for dinner", "cost": 75, "icon": "🍕"},
            {"id": 3, "name": "Stay up 30 min late", "cost": 100, "icon": "🌙"},
            {"id": 4, "name": "Pick movie night movie", "cost": 100, "icon": "🎬"},
            {"id": 5, "name": "Ice cream trip", "cost": 150, "icon": "🍦"},
            {"id": 6, "name": "Skip one chore", "cost": 75, "icon": "😎"},
            {"id": 7, "name": "Small toy or book", "cost": 300, "icon": "🎁"},
            {"id": 8, "name": "Special outing with parent", "cost": 500, "icon": "🎢"}
        ],
        "history": []
    })
    # Return in flat format for sidebar widget compatibility
    # Frontend expects {kid1: X, kid2: Y} not {points: {kid1: X, kid2: Y}}
    return rewards.get("points", {"kid1": 0, "kid2": 0})


def save_rewards(points_data):
    """Save rewards points. Accepts {kid1: X, kid2: Y} format."""
    current = load_json(REWARDS_FILE, {
        "points": {"kid1": 0, "kid2": 0},
        "rewards": [],
        "history": []
    })
    current["points"] = {
        "kid1": points_data.get("kid1", 0),
        "kid2": points_data.get("kid2", 0)
    }
    save_json(REWARDS_FILE, current)
    return {"success": True}


def get_meals():
    return load_json(MEALS_FILE, {
        "thisWeek": {},
        "favorites": [
            {"name": "Tacos", "icon": "🌮"},
            {"name": "Pasta", "icon": "🍝"},
            {"name": "Pizza", "icon": "🍕"},
            {"name": "Grilled Chicken", "icon": "🍗"},
            {"name": "Soup & Sandwiches", "icon": "🥪"},
            {"name": "Stir Fry", "icon": "🥡"},
            {"name": "Burgers", "icon": "🍔"},
            {"name": "Breakfast for Dinner", "icon": "🥞"}
        ]
    })


def get_shopping():
    return load_json(SHOPPING_FILE, {
        "items": [],
        "categories": ["Produce", "Dairy", "Meat", "Pantry", "Frozen", "Household", "Other"]
    })


def get_tvshows():
    return load_json(TVSHOWS_FILE, {
        "watching": [],
        "toWatch": [],
        "finished": []
    })


def get_notes():
    return load_json(NOTES_FILE, {"notes": []})
