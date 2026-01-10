#!/usr/bin/env python3
"""
Family Family Hub - Skylight Calendar Style
Beautiful warm family dashboard inspired by Skylight Calendar.

This is the main server file. The code is organized into modules:
- data.py: Family data, holidays, school menus, and categories
- handlers.py: JSON file loading/saving and data getters
- html_template.py: The HTML/CSS/JS dashboard template
"""
import json
import os
import tempfile
import subprocess
import time
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse
import urllib.request

# OpenAI API key for Whisper transcription
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')

# Weather cache (30 minute TTL)
WEATHER_CACHE = {"data": None, "timestamp": 0}
WEATHER_CACHE_TTL = 1800  # 30 minutes in seconds

# Import from modules
from data import (
    FAMILY, HOLIDAYS, SCHOOL_LUNCHES, SCHOOL_BREAKFAST,
    SCHOOL_SNACK, EVENT_CATEGORIES
)
from handlers import (
    CALENDAR_FILE, CHORES_FILE, REWARDS_FILE, MEALS_FILE,
    SHOPPING_FILE, TVSHOWS_FILE, NOTES_FILE,
    load_json, save_json,
    get_calendar, get_chores, get_rewards, save_rewards, get_meals,
    get_shopping, get_tvshows, get_notes
)
from html_template import get_dashboard_html


class DashboardHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)

        if parsed.path.startswith("/static/"):
            self._serve_static_file(parsed.path)
        elif parsed.path == "/" or parsed.path == "/index.html":
            self._serve_new_html()  # New refactored version is now the default
        elif parsed.path == "/old" or parsed.path == "/old.html":
            self._serve_html()  # Legacy version moved to /old
        elif parsed.path == "/api/calendar":
            self.send_json(get_calendar())
        elif parsed.path == "/api/chores":
            self.send_json(get_chores())
        elif parsed.path == "/api/rewards":
            self.send_json(get_rewards())
        elif parsed.path == "/api/meals":
            self.send_json(get_meals())
        elif parsed.path == "/api/shopping":
            self.send_json(get_shopping())
        elif parsed.path == "/api/tvshows":
            self.send_json(get_tvshows())
        elif parsed.path == "/api/notes":
            self.send_json(get_notes())
        elif parsed.path == "/api/family":
            self.send_json(FAMILY)
        elif parsed.path == "/api/holidays":
            self.send_json(HOLIDAYS)
        elif parsed.path == "/api/lunches":
            self.send_json(SCHOOL_LUNCHES)
        elif parsed.path == "/api/breakfast":
            self.send_json(SCHOOL_BREAKFAST)
        elif parsed.path == "/api/snacks":
            self.send_json(SCHOOL_SNACK)
        elif parsed.path == "/api/school-menu":
            self.send_json({
                "lunches": SCHOOL_LUNCHES,
                "breakfast": SCHOOL_BREAKFAST,
                "snacks": SCHOOL_SNACK
            })
        elif parsed.path == "/api/weather":
            self._serve_weather()
        elif parsed.path == "/api/videos":
            self._serve_video_list()
        elif parsed.path == "/api/fia-config":
            self._serve_fia_config()
        elif parsed.path.startswith("/videos/"):
            self._serve_video_file(parsed.path)
        else:
            super().do_GET()

    def _serve_static_file(self, path):
        """Serve static files (CSS, JS, videos, images, etc.)"""
        try:
            # Remove leading /static/ from path
            relative_path = path[8:] if path.startswith("/static/") else path
            relative_path = urllib.parse.unquote(relative_path)

            # Prevent directory traversal
            if ".." in relative_path:
                self.send_error(403, "Forbidden")
                return

            # Use the directory where server.py is located
            base_path = os.path.dirname(os.path.abspath(__file__))

            # First, try serving from static/ subdirectory
            static_path = os.path.join(base_path, "static", relative_path)
            file_path = None

            if os.path.exists(static_path) and os.path.isfile(static_path):
                file_path = static_path
            else:
                # Fallback to root directory (for ocean videos, etc.)
                filename = os.path.basename(relative_path)
                root_path = os.path.join(base_path, filename)

                if os.path.exists(root_path) and os.path.isfile(root_path):
                    file_path = root_path
                elif "ocean" in filename.lower() or "video" in filename.lower():
                    # Try finding video files with case-insensitive match
                    for f in os.listdir(base_path):
                        if f.lower() == filename.lower():
                            file_path = os.path.join(base_path, f)
                            break

            if file_path and os.path.exists(file_path) and os.path.isfile(file_path):
                self.send_response(200)

                # Set appropriate content type based on file extension
                ext = file_path.lower().split(".")[-1] if "." in file_path else ""
                content_types = {
                    "html": "text/html",
                    "css": "text/css",
                    "js": "application/javascript",
                    "json": "application/json",
                    "mp4": "video/mp4",
                    "png": "image/png",
                    "jpg": "image/jpeg",
                    "jpeg": "image/jpeg",
                    "gif": "image/gif",
                    "svg": "image/svg+xml",
                    "ico": "image/x-icon",
                    "woff": "font/woff",
                    "woff2": "font/woff2",
                    "ttf": "font/ttf"
                }
                content_type = content_types.get(ext, "application/octet-stream")
                self.send_header("Content-type", content_type)

                if ext == "mp4":
                    self.send_header("Accept-Ranges", "bytes")

                self.end_headers()
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "File not found")
        except Exception as e:
            self.send_error(500, str(e))

    def _serve_html(self):
        """Serve the main HTML dashboard."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(get_dashboard_html().encode())

    def _serve_new_html(self):
        """Serve the refactored HTML dashboard from static/index.html."""
        try:
            base_path = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(base_path, "static", "index.html")
            if os.path.exists(file_path):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "New index.html not found")
        except Exception as e:
            self.send_error(500, str(e))

    def _serve_weather(self):
        """Fetch and serve weather data from Open-Meteo API with caching."""
        global WEATHER_CACHE

        # Check cache first
        now = time.time()
        if WEATHER_CACHE["data"] and (now - WEATHER_CACHE["timestamp"]) < WEATHER_CACHE_TTL:
            self.send_json(WEATHER_CACHE["data"])
            return

        try:
            # Trinidad, CA coordinates
            url = "https://api.open-meteo.com/v1/forecast?latitude=41.0593&longitude=-124.1431&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_probability_max&current_weather=true&temperature_unit=fahrenheit&timezone=America%2FLos_Angeles&forecast_days=3"
            with urllib.request.urlopen(url, timeout=10) as response:
                data = json.loads(response.read().decode())

            def get_weather_emoji(code):
                if code == 0: return "☀️"
                if code in [1, 2, 3]: return "⛅"
                if code in [45, 48]: return "🌫️"
                if code in [51, 53, 55, 61, 63, 65]: return "🌧️"
                if code in [71, 73, 75]: return "❄️"
                if code in [95, 96, 99]: return "⛈️"
                return "🌡️"

            weather = {
                "current": {
                    "temp": round(data["current_weather"]["temperature"]),
                    "code": data["current_weather"]["weathercode"],
                    "emoji": get_weather_emoji(data["current_weather"]["weathercode"])
                },
                "forecast": []
            }

            for i in range(1, 3):
                date_obj = datetime.strptime(data["daily"]["time"][i], "%Y-%m-%d")
                day_name = date_obj.strftime("%A")
                weather["forecast"].append({
                    "day": day_name,
                    "high": round(data["daily"]["temperature_2m_max"][i]),
                    "low": round(data["daily"]["temperature_2m_min"][i]),
                    "rain": data["daily"]["precipitation_probability_max"][i],
                    "emoji": get_weather_emoji(data["daily"]["weathercode"][i])
                })

            # Update cache
            WEATHER_CACHE["data"] = weather
            WEATHER_CACHE["timestamp"] = now

            self.send_json(weather)
        except Exception as e:
            print(f"Weather error: {e}")
            # Return cached data if available, even if stale
            if WEATHER_CACHE["data"]:
                self.send_json(WEATHER_CACHE["data"])
            else:
                self.send_json({"error": "Failed to fetch weather"})

    def _serve_fia_config(self):
        """Return Fia server configuration."""
        try:
            base_path = os.path.dirname(os.path.abspath(__file__))
            config_file = os.path.join(base_path, "fia_config.json")
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    config = json.load(f)
                    self.send_json(config)
            else:
                # Default config - localhost
                self.send_json({"url": ""})
        except Exception as e:
            self.send_json({"url": "", "error": str(e)})

    def _serve_video_list(self):
        """Scan for ocean video files in root folder only (not monthly backgrounds)."""
        try:
            base_path = os.path.dirname(os.path.abspath(__file__))
            video_files = []

            # Check root directory for ocean screensaver videos only
            for file in os.listdir(base_path):
                if file.lower().endswith(".mp4") and not file.startswith("._") and "ocean" in file.lower():
                    video_files.append(file)

            video_files.sort()
            self.send_json({"videos": video_files})
        except Exception as e:
            self.send_json({"error": str(e), "videos": []})

    def _serve_video_file(self, path):
        """Serve video files from root or static directory."""
        try:
            # Extract filename from /videos/filename.mp4
            filename = path[8:] if path.startswith("/videos/") else path
            filename = urllib.parse.unquote(filename)

            # Security check
            if ".." in filename or "/" in filename:
                self.send_error(403, "Forbidden")
                return

            base_path = os.path.dirname(os.path.abspath(__file__))

            # Check root directory first, then static folder
            file_path = os.path.join(base_path, filename)
            if not os.path.exists(file_path):
                file_path = os.path.join(base_path, "static", filename)

            if os.path.exists(file_path) and os.path.isfile(file_path) and filename.endswith(".mp4"):
                self.send_response(200)
                self.send_header("Content-type", "video/mp4")
                self.send_header("Accept-Ranges", "bytes")
                file_size = os.path.getsize(file_path)
                self.send_header("Content-Length", str(file_size))
                self.end_headers()
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "Video not found")
        except Exception as e:
            self.send_error(500, str(e))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        content_type = self.headers.get('Content-Type', '')

        # Handle audio transcription endpoint (multipart form data)
        if self.path == "/api/transcribe":
            self._handle_transcribe(content_length, content_type)
            return

        # Handle OCR endpoint (multipart form data)
        if self.path == "/api/ocr":
            self._handle_ocr(content_length, content_type)
            return

        # Handle Fia chat endpoint (proxy to Mac via tunnel)
        if self.path == "/api/fia-chat":
            self._handle_fia_chat(content_length, content_type)
            return

        # Regular JSON endpoints
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode())

        # Calendar endpoints
        if self.path == "/api/calendar/add" or self.path == "/api/calendar":
            self._handle_calendar_add(data)
        elif self.path == "/api/calendar/delete":
            self._handle_calendar_delete(data)
        # Chores endpoints
        elif self.path == "/api/chores/complete":
            self._handle_chore_complete(data)
        elif self.path == "/api/chores/uncomplete":
            self._handle_chore_uncomplete(data)
        elif self.path == "/api/chores/reset":
            self._handle_chore_reset(data)
        # Rewards endpoints
        elif self.path == "/api/rewards/redeem":
            self._handle_reward_redeem(data)
        elif self.path == "/api/rewards/save":
            self._handle_rewards_save(data)
        # Meals endpoints
        elif self.path == "/api/meals/set" or self.path == "/api/meals":
            self._handle_meal_set(data)
        elif self.path == "/api/meals/favorite/add":
            self._handle_meal_favorite_add(data)
        # Shopping endpoints
        elif self.path == "/api/shopping/add" or self.path == "/api/shopping":
            self._handle_shopping_add(data)
        elif self.path == "/api/shopping/batch":
            self._handle_shopping_batch(data)
        elif self.path == "/api/shopping/toggle":
            self._handle_shopping_toggle(data)
        elif self.path == "/api/shopping/clear":
            self._handle_shopping_clear(data)
        elif self.path == "/api/shopping/delete":
            self._handle_shopping_delete(data)
        elif self.path == "/api/shopping/clearall":
            self._handle_shopping_clearall(data)
        # Notes endpoints
        elif self.path == "/api/notes/add":
            self._handle_notes_add(data)
        elif self.path == "/api/notes/delete":
            self._handle_notes_delete(data)
        # TV Shows endpoints
        elif self.path == "/api/tvshows/add":
            self._handle_tvshows_add(data)
        elif self.path == "/api/tvshows/move":
            self._handle_tvshows_move(data)
        else:
            self.send_json({"error": "Unknown endpoint"})

    def _handle_transcribe(self, content_length, content_type):
        """Forward audio to local Fia (via tunnel) for transcription."""
        try:
            # Read the raw multipart data
            post_data = self.rfile.read(content_length)

            # Forward to Fia running on localhost:8765 (via SSH tunnel from Mac)
            import http.client

            conn = http.client.HTTPConnection("localhost", 8765, timeout=30)
            conn.request("POST", "/api/transcribe", post_data, {
                'Content-Type': content_type,
                'Content-Length': str(len(post_data))
            })
            response = conn.getresponse()
            result = json.loads(response.read().decode())
            conn.close()

            self.send_json(result)

        except ConnectionRefusedError:
            self.send_json({"error": "Fia not connected. Run tunnel_to_vps.sh on your Mac."})
        except Exception as e:
            print(f"Transcription error: {e}")
            self.send_json({"error": f"Transcription failed: {str(e)}"})

    def _handle_ocr(self, content_length, content_type):
        """Forward image to Fia OCR, parse results, and extract calendar events."""
        try:
            # Read the raw multipart data
            post_data = self.rfile.read(content_length)

            # Forward to Fia running on localhost:8765 (via SSH tunnel from Mac)
            import http.client

            conn = http.client.HTTPConnection("localhost", 8765, timeout=120)
            conn.request("POST", "/api/ocr", post_data, {
                'Content-Type': content_type,
                'Content-Length': str(len(post_data))
            })
            response = conn.getresponse()
            result = json.loads(response.read().decode())
            conn.close()

            if "error" in result:
                self.send_json(result)
                return

            ocr_text = result.get("text", "")

            # Now parse the OCR text to extract events
            events = self._parse_ocr_for_events(ocr_text)

            self.send_json({
                "success": True,
                "raw_text": ocr_text,
                "events": events
            })

        except ConnectionRefusedError:
            self.send_json({"error": "Fia not connected. Run fia_server.py on your Mac."})
        except Exception as e:
            print(f"OCR error: {e}")
            self.send_json({"error": f"OCR failed: {str(e)}"})

    def _handle_fia_chat(self, content_length, content_type):
        """Forward chat message to Fia brain (via SSH tunnel from Mac)."""
        try:
            post_data = self.rfile.read(content_length)

            import http.client
            conn = http.client.HTTPConnection("localhost", 8765, timeout=60)
            conn.request("POST", "/api/chat", post_data, {
                'Content-Type': 'application/json',
                'Content-Length': str(len(post_data))
            })
            response = conn.getresponse()
            result = json.loads(response.read().decode())
            conn.close()

            self.send_json(result)

        except ConnectionRefusedError:
            self.send_json({"status": "error", "response": "Fia not connected. Make sure Launch Family Planner is running on your Mac."})
        except Exception as e:
            print(f"Fia chat error: {e}")
            self.send_json({"status": "error", "response": f"Chat failed: {str(e)}"})

    def _parse_ocr_for_events(self, ocr_text):
        """Parse OCR text to extract calendar events with dates."""
        import re
        events = []

        # Common date patterns
        date_patterns = [
            r'(\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?(?:,?\s*\d{4})?)\b',
            r'(\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\.?\s+\d{1,2}(?:st|nd|rd|th)?(?:,?\s*\d{4})?)\b',
            r'\b(\d{1,2}/\d{1,2}(?:/\d{2,4})?)\b',
            r'\b(\d{1,2}-\d{1,2}(?:-\d{2,4})?)\b',
        ]

        month_map = {
            'january': 1, 'february': 2, 'march': 3, 'april': 4,
            'may': 5, 'june': 6, 'july': 7, 'august': 8,
            'september': 9, 'october': 10, 'november': 11, 'december': 12,
            'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'jun': 6,
            'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
        }

        # Keywords that indicate what kind of event this is
        context_keywords = {
            'due': 'Due',
            'deadline': 'Deadline',
            'expires': 'Expires',
            'expiration': 'Expiration',
            'appointment': 'Appointment',
            'meeting': 'Meeting',
            'event': 'Event',
            'fee': 'Fee Due',
            'payment': 'Payment Due',
            'renew': 'Renewal',
            'registration': 'Registration',
            'dmv': 'DMV',
            'birthday': 'Birthday',
            'party': 'Party'
        }

        lines = ocr_text.split('\n')
        current_year = datetime.now().year
        # If we're late in the year and see a date in early months, assume next year
        current_month = datetime.now().month

        for idx, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue

            # Try to find a date in this line
            date_found = None
            date_str = None

            for pattern in date_patterns:
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    date_str = match.group(1)
                    try:
                        # Try Month Day format
                        for month_name, month_num in month_map.items():
                            if month_name in date_str.lower():
                                day_match = re.search(r'(\d{1,2})', date_str)
                                if day_match:
                                    day = int(day_match.group(1))
                                    year_match = re.search(r'(\d{4})', date_str)
                                    if year_match:
                                        year = int(year_match.group(1))
                                    else:
                                        # Smart year: if month is before current month, assume next year
                                        year = current_year
                                        if month_num < current_month:
                                            year = current_year + 1
                                    date_found = f"{year}-{month_num:02d}-{day:02d}"
                                break

                        # Try numeric format (1/15 or 1-15)
                        if not date_found:
                            numeric_match = re.match(r'(\d{1,2})[/-](\d{1,2})(?:[/-](\d{2,4}))?', date_str)
                            if numeric_match:
                                month = int(numeric_match.group(1))
                                day = int(numeric_match.group(2))
                                year = numeric_match.group(3)
                                if year:
                                    year = int(year)
                                    if year < 100:
                                        year += 2000
                                else:
                                    year = current_year
                                    if month < current_month:
                                        year = current_year + 1
                                if 1 <= month <= 12 and 1 <= day <= 31:
                                    date_found = f"{year}-{month:02d}-{day:02d}"
                    except:
                        pass

                    if date_found:
                        break

            if date_found:
                # Extract event title (remove the date from the line)
                title = re.sub('|'.join(date_patterns), '', line, flags=re.IGNORECASE).strip()
                title = re.sub(r'^[-:,.\s]+|[-:,.\s]+$', '', title)  # Clean up punctuation

                # If title is empty or too short, look for context
                if not title or len(title) < 2:
                    # Check line for keywords
                    full_text = line.lower()
                    # Also check previous line for context
                    if idx > 0:
                        full_text = lines[idx-1].lower() + " " + full_text

                    for keyword, label in context_keywords.items():
                        if keyword in full_text:
                            title = label
                            break

                    # If still no title, use generic
                    if not title or len(title) < 2:
                        title = "Event"

                events.append({
                    "title": title,
                    "date": date_found,
                    "time": "",
                    "person": "family"
                })

        return events

    def _handle_calendar_add(self, data):
        cal = get_calendar()
        # Get next unique ID (max existing + 1, not len which can cause duplicates after deletes)
        max_id = max([e.get("id", 0) for e in cal["events"]], default=0)
        event = {
            "id": max_id + 1,
            "title": data.get("title", ""),
            "date": data.get("date", ""),
            "time": data.get("time", ""),
            "person": data.get("person", data.get("member", "family")),
            "notes": data.get("notes", ""),
            "created": datetime.now().isoformat()
        }
        cal["events"].append(event)
        save_json(CALENDAR_FILE, cal)
        self.send_json({"success": True, "event": event})

    def _handle_calendar_delete(self, data):
        cal = get_calendar()
        cal["events"] = [e for e in cal["events"] if e["id"] != data["id"]]
        save_json(CALENDAR_FILE, cal)
        self.send_json({"success": True})

    def _handle_chore_complete(self, data):
        chores = get_chores()
        rewards = get_rewards()
        chore_id = data.get("choreId")
        person = data.get("person", data.get("child"))
        today = datetime.now().strftime("%Y-%m-%d")

        chore = next((c for c in chores["chores"] if c["id"] == chore_id), None)
        if not chore:
            chore_name = data.get("chore", "").lower()
            for c in chores["chores"]:
                if chore_name in c["name"].lower():
                    chore = c
                    chore_id = c["id"]
                    break

        if chore:
            completion = {"choreId": chore_id, "person": person, "date": today, "points": chore["points"]}
            chores["completed"].append(completion)
            save_json(CHORES_FILE, chores)
            rewards["points"][person] = rewards["points"].get(person, 0) + chore["points"]
            save_json(REWARDS_FILE, rewards)
            self.send_json({"success": True, "points": chore["points"]})
        else:
            self.send_json({"success": False, "error": "Chore not found"})

    def _handle_chore_uncomplete(self, data):
        chores = get_chores()
        rewards = get_rewards()
        today = datetime.now().strftime("%Y-%m-%d")
        for i, c in enumerate(chores["completed"]):
            if c["choreId"] == data["choreId"] and c["person"] == data["person"] and c["date"] == today:
                rewards["points"][data["person"]] -= c["points"]
                chores["completed"].pop(i)
                break
        save_json(CHORES_FILE, chores)
        save_json(REWARDS_FILE, rewards)
        self.send_json({"success": True, "points": rewards["points"]})

    def _handle_chore_reset(self, data):
        """Reset all completed chores (clear the completed array)."""
        chores = get_chores()
        chores["completed"] = []
        save_json(CHORES_FILE, chores)
        self.send_json({"success": True})

    def _handle_reward_redeem(self, data):
        rewards_data = load_json(REWARDS_FILE, {"points": {"liv": 0, "jane": 0}, "rewards": [], "history": []})
        person = data["person"]
        reward_id = data["rewardId"]
        reward = next((r for r in rewards_data["rewards"] if r["id"] == reward_id), None)
        if reward and rewards_data["points"].get(person, 0) >= reward["cost"]:
            rewards_data["points"][person] -= reward["cost"]
            rewards_data["history"].append({
                "person": person, "reward": reward["name"],
                "cost": reward["cost"], "date": datetime.now().isoformat()
            })
            save_json(REWARDS_FILE, rewards_data)
            self.send_json({"success": True, "points": rewards_data["points"]})
        else:
            self.send_json({"success": False, "error": "Not enough points"})

    def _handle_rewards_save(self, data):
        """Save rewards points from sidebar widget. Expects {liv: X, jane: Y}."""
        result = save_rewards(data)
        self.send_json(result)

    def _handle_meal_set(self, data):
        meals = get_meals()
        day = data.get("day")
        if not day:
            date_str = data.get("date")
            if date_str:
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                day = date_obj.strftime("%A").lower()
        meal_data = data.get("meal") if isinstance(data.get("meal"), dict) else {"name": data.get("meal"), "icon": "🍽️"}
        meals["thisWeek"][day] = meal_data
        save_json(MEALS_FILE, meals)
        self.send_json({"success": True})

    def _handle_meal_favorite_add(self, data):
        meals = get_meals()
        meals["favorites"].append({"name": data["name"], "icon": data.get("icon", "🍽️")})
        save_json(MEALS_FILE, meals)
        self.send_json({"success": True})

    def _handle_shopping_add(self, data):
        shopping = get_shopping()
        max_id = max([i.get("id", 0) for i in shopping["items"]], default=0)
        item = {
            "id": max_id + 1,
            "name": data.get("name", data.get("item", "")),
            "category": data.get("category", "Other"),
            "quantity": data.get("quantity", 1),
            "checked": False
        }
        shopping["items"].append(item)
        save_json(SHOPPING_FILE, shopping)
        self.send_json({"success": True, "item": item})

    def _handle_shopping_batch(self, data):
        """Add multiple shopping items in one request."""
        shopping = get_shopping()
        items = data.get("items", [])
        added = []
        max_id = max([i.get("id", 0) for i in shopping["items"]], default=0)
        for item_data in items:
            max_id += 1
            name = item_data if isinstance(item_data, str) else item_data.get("name", "")
            item = {
                "id": max_id,
                "name": name,
                "category": item_data.get("category", "Other") if isinstance(item_data, dict) else "Other",
                "quantity": item_data.get("quantity", 1) if isinstance(item_data, dict) else 1,
                "checked": False
            }
            shopping["items"].append(item)
            added.append(item)
        save_json(SHOPPING_FILE, shopping)
        self.send_json({"success": True, "items": added, "count": len(added)})

    def _handle_shopping_toggle(self, data):
        shopping = get_shopping()
        for item in shopping["items"]:
            if item["id"] == data["id"]:
                item["checked"] = not item["checked"]
                break
        save_json(SHOPPING_FILE, shopping)
        self.send_json({"success": True})

    def _handle_shopping_clear(self, data):
        shopping = get_shopping()
        shopping["items"] = [i for i in shopping["items"] if not i["checked"]]
        save_json(SHOPPING_FILE, shopping)
        self.send_json({"success": True})

    def _handle_shopping_delete(self, data):
        shopping = get_shopping()
        item_id = data.get("id")
        shopping["items"] = [i for i in shopping["items"] if i["id"] != item_id]
        save_json(SHOPPING_FILE, shopping)
        self.send_json({"success": True})

    def _handle_shopping_clearall(self, data):
        shopping = get_shopping()
        shopping["items"] = []
        save_json(SHOPPING_FILE, shopping)
        self.send_json({"success": True})

    def _handle_notes_add(self, data):
        notes = get_notes()
        note = {
            "id": len(notes["notes"]) + 1,
            "text": data["text"],
            "person": data.get("person", "family"),
            "created": datetime.now().isoformat()
        }
        notes["notes"].append(note)
        save_json(NOTES_FILE, notes)
        self.send_json({"success": True, "note": note})

    def _handle_notes_delete(self, data):
        notes = get_notes()
        notes["notes"] = [n for n in notes["notes"] if n["id"] != data["id"]]
        save_json(NOTES_FILE, notes)
        self.send_json({"success": True})

    def _handle_tvshows_add(self, data):
        shows = get_tvshows()
        show = {
            "id": len(shows["watching"]) + len(shows["toWatch"]) + 1,
            "name": data["name"],
            "status": data.get("status", "toWatch")
        }
        shows[show["status"]].append(show)
        save_json(TVSHOWS_FILE, shows)
        self.send_json({"success": True})

    def _handle_tvshows_move(self, data):
        shows = get_tvshows()
        show_id = data["id"]
        to_status = data["toStatus"]
        for status in ["watching", "toWatch", "finished"]:
            for i, show in enumerate(shows[status]):
                if show["id"] == show_id:
                    show["status"] = to_status
                    shows[status].pop(i)
                    shows[to_status].append(show)
                    save_json(TVSHOWS_FILE, shows)
                    self.send_json({"success": True})
                    return
        self.send_json({"success": False})

    def send_json(self, data):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    port = 8766
    print(f"Starting Family Dashboard Server on port {port}...")
    print(f"Open http://localhost:{port}")

    server_address = ('', port)
    httpd = HTTPServer(server_address, DashboardHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
