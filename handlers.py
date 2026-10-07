"""
JSON file handlers for Family Family Hub.
"""
import json
import os
from datetime import datetime, timedelta

# Data file paths
# Set FP_DATA_DIR to keep the JSON data somewhere other than next to the code.
DATA_DIR = os.environ.get("FP_DATA_DIR") or os.path.dirname(os.path.abspath(__file__))

# Cache for JSON files - avoids disk reads on every request
_FILE_CACHE = {}  # {filepath: {"data": ..., "mtime": ...}}
CALENDAR_FILE = os.path.join(DATA_DIR, "calendar.json")
CHORES_FILE = os.path.join(DATA_DIR, "chores.json")
REWARDS_FILE = os.path.join(DATA_DIR, "rewards.json")
MEALS_FILE = os.path.join(DATA_DIR, "meals.json")
SHOPPING_FILE = os.path.join(DATA_DIR, "shopping.json")
TVSHOWS_FILE = os.path.join(DATA_DIR, "tvshows.json")
NOTES_FILE = os.path.join(DATA_DIR, "notes.json")
POLLS_FILE = os.path.join(DATA_DIR, "polls.json")
ROUTINES_FILE = os.path.join(DATA_DIR, "routines.json")
# Latest digest posted by an optional school-email watcher (POST /api/school/report).
SCHOOL_FILE = os.path.join(DATA_DIR, "school.json")


def load_json(filepath, default):
    """Load JSON with caching - only reads disk if file changed."""
    if not os.path.exists(filepath):
        return default

    try:
        mtime = os.path.getmtime(filepath)
        cached = _FILE_CACHE.get(filepath)

        # Return cached data if file hasn't been modified
        if cached and cached["mtime"] == mtime:
            return cached["data"]

        # Read from disk and cache
        with open(filepath, 'r') as f:
            data = json.load(f)
        _FILE_CACHE[filepath] = {"data": data, "mtime": mtime}
        return data
    except:
        return default


def save_json(filepath, data):
    """Save JSON and update cache."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    # Update cache with new data and mtime
    _FILE_CACHE[filepath] = {"data": data, "mtime": os.path.getmtime(filepath)}


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


def get_polls():
    return load_json(POLLS_FILE, {
        "polls": [],
        "votes": []
    })


def get_routines():
    return load_json(ROUTINES_FILE, {
        "routines": {
            "kid1": {
                "name": "Kid 1's Bedtime",
                "tasks": [3],  # Brush teeth (night) by default
                "icon": "🌙"
            },
            "kid2": {
                "name": "Kid 2's Bedtime",
                "tasks": [3],
                "icon": "🌙"
            }
        },
        "progress": {
            "kid1": {"date": "", "completed": []},
            "kid2": {"date": "", "completed": []}
        }
    })


KEEP_DAYS = 21
SCHOOL_KEYS = ("todos", "added", "summaries", "not_added", "mentioned")


def get_school():
    """What the school-email watcher has reported (see POST /api/school/report)."""
    d = load_json(SCHOOL_FILE, None)
    if not d:
        d = {"ts": "", "summary": "", "homework": None}
        for k in SCHOOL_KEYS:
            d[k] = []
    d.setdefault("homework", None)
    return d


def save_school(report):
    """Merge, do not replace. One run that finds a single email should not erase
    what the schools said last week — this card is the parents' running record."""
    prev = load_json(SCHOOL_FILE, {}) or {}
    now = report.get("ts") or datetime.now().isoformat(timespec="seconds")
    cutoff = (datetime.now() - timedelta(days=KEEP_DAYS)).isoformat(timespec="seconds")

    def words(t):
        import re
        return {w for w in re.findall(r"[a-z]+", t.lower()) if len(w) > 3}

    def near(a, b):
        """Same ask, different wording — the schools repeat themselves weekly."""
        wa, wb = words(a), words(b)
        if not wa or not wb:
            return a == b
        return len(wa & wb) / min(len(wa), len(wb)) >= 0.75

    items = prev.get("_items", {})
    merged = {}
    for key in SCHOOL_KEYS:
        old = [e for e in items.get(key, []) if e.get("ts", "") >= cutoff]
        fresh = []
        for t in (report.get(key) or []):
            if any(near(t, e.get("t", "")) for e in old) or any(near(t, f["t"]) for f in fresh):
                continue
            fresh.append({"t": t, "ts": now})
        merged[key] = (fresh + old)[:60]          # newest first

    # The Home Practice sheet is a whole week in one piece, so it is replaced,
    # not merged line by line: a run that reads no new school mail must keep
    # showing this week's homework, and next Monday's sheet must replace it
    # outright rather than pile up next to the old page numbers.
    homework = report.get("homework") or prev.get("homework")
    if homework:
        try:
            last = max(d["date"] for d in homework.get("days") or [])
            if last < (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d"):
                homework = None          # last week's sheet, the week is done
        except (ValueError, KeyError, TypeError):
            homework = None

    data = {"ts": now, "summary": report.get("summary", ""),
            "homework": homework, "_items": merged}
    for key in SCHOOL_KEYS:
        data[key] = [e["t"] for e in merged[key]]
    save_json(SCHOOL_FILE, data)
    return data
