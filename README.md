# Family Planner Dashboard

**A Skylight Calendar-inspired family command center with voice control, OCR document scanning, AI assistant, and dynamic seasonal themes.**

> Built this because I wanted a fully customizable family hub that I control. Runs on a spare iPad and does everything - voice commands, document scanning, meal planning, chore tracking with celebrations, and ambient video screensavers. No subscriptions, no cloud dependency.

<a id="what-it-does"></a>
<picture><source media="(max-width: 610px), (min-width: 768px) and (max-width: 895px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s01-banner-m.svg"><source media="(max-width: 1149px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s01-banner-mid.svg"><img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s01-banner.svg" width="100%" alt="01. What it does. A family command center on a spare iPad"></picture>
<picture><source media="(max-width: 610px), (min-width: 768px) and (max-width: 895px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s01-r1-m.svg"><source media="(max-width: 1149px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s01-r1-mid.svg"><img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s01-r1.svg" width="100%" alt="Voice control. Talk to it on the calendar, meals, chores and shopping screens. OCR document scanning. Point the camera at a flyer and add its events to the calendar. AI assistant. Fia, a chat assistant powered by Claude, can change the calendar, shopping list and meal plan."></picture>

```
┌─────────────────────────────────────────────────────────────────┐
│  🎙️ VOICE    │  📸 OCR SCAN  │  🤖 AI CHAT   │  📺 SCREENSAVER │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   📅 CALENDAR          │    🍽️ MEAL PLANNER                    │
│   ├─ Events            │    ├─ Weekly meals                    │
│   ├─ Holidays          │    ├─ School lunch menus              │
│   ├─ Moon phases       │    └─ Voice: "Tacos for Friday"       │
│   ├─ Weather forecast  │                                       │
│   └─ Seasonal themes   │    🛒 SHOPPING LIST                   │
│                        │    └─ Voice: "Add milk"               │
│   ⭐ KIDS CHORES       │                                       │
│   ├─ Task tracking     │    🎬 MONTHLY SCREENSAVERS            │
│   ├─ Celebrations!     │    ├─ Seasonal video backgrounds      │
│   └─ No points needed  │    └─ Ocean idle screensaver          │
│                        │                                       │
└─────────────────────────────────────────────────────────────────┘
```

<img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s01-rule.svg" width="100%" alt="">

<a id="features"></a>
<picture><source media="(max-width: 610px), (min-width: 768px) and (max-width: 895px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s02-banner-m.svg"><source media="(max-width: 1149px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s02-banner-mid.svg"><img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s02-banner.svg" width="100%" alt="02. Features. Voice, scanning, chat, calendar, chores, meals, shopping, screensavers"></picture>
<picture><source media="(max-width: 610px), (min-width: 768px) and (max-width: 895px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s02-r1-m.svg"><source media="(max-width: 1149px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s02-r1-mid.svg"><img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s02-r1.svg" width="100%" alt="Voice with Whisper fallback. Web Speech API first, OpenAI Whisper when it needs more accuracy. Chores without points. Tap a chore, get a celebration. The reward is the celebration. Seasonal calendar. Moon phases, a 7-day forecast, color-coded events and built-in US holidays."></picture>

### 🎙️ Voice Commands (Works Everywhere)
Just talk to it. Uses Web Speech API with OpenAI Whisper fallback for accuracy.

```
"Add dentist appointment Tuesday at 3pm"
"kid1 brushed her teeth"
"Plan spaghetti for Wednesday"
"Add eggs to the shopping list"
```

The voice bar is everywhere - calendar, meals, chores, shopping. Speak naturally.

### 📸 OCR Document Scanning
Point your camera at a school flyer, sports schedule, or event poster. The system:
1. Captures the image
2. Sends to Claude Vision API
3. Extracts dates, times, and event names
4. Shows you what it found
5. One click to add to calendar

No more manually typing in school newsletters.

### 🤖 Fia - AI Family Assistant
Chat interface powered by Claude. Ask anything:
- "What's on the calendar today?"
- "What's for dinner?"
- "How are the kids doing with chores?"
- "Add a playdate with the Johnsons on Saturday"

Fia understands context and can modify your calendar, shopping list, and meal plan.

### 📅 Dynamic Calendar with Themes
- **Seasonal backgrounds** - December has snow video, January has sparkles
- **Moon phases** on every day
- **Weather forecast** integration (7-day)
- **Color-coded events** by family member
- **US holidays** built in for 2025-2026

### ⭐ Kids Chore System (No Points!)
We tried the point system. Kids gamed it. Now it's simple:
- Tap a chore when done
- Get a **celebration** (slot machine, confetti, bubble pop)
- That's it. The reward IS the celebration.

Chores auto-reset daily. Parents can see progress at a glance.

### 🍽️ Meal Planning
- Weekly meal grid
- School lunch/breakfast menus (customizable)
- Favorite meals library
- Voice: "Plan pizza for Friday dinner"

### 🛒 Shopping List
- Add items by voice or text
- Check off as you shop
- Syncs across devices

### 📺 Screensaver System
- **Idle screensaver**: Ocean videos play when inactive (configurable timeout)
- **Monthly screensaver**: Click the button to see the current month's themed video
- Videos play at 25% speed for ambient effect

<img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s02-rule.svg" width="100%" alt="">

<a id="tech"></a>
<picture><source media="(max-width: 610px), (min-width: 768px) and (max-width: 895px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s03-banner-m.svg"><source media="(max-width: 1149px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s03-banner-mid.svg"><img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s03-banner.svg" width="100%" alt="03. Tech stack and architecture. Python on the back, vanilla JS on the front"></picture>
<picture><source media="(max-width: 610px), (min-width: 768px) and (max-width: 895px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s03-r1-m.svg"><source media="(max-width: 1149px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s03-r1-mid.svg"><img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s03-r1.svg" width="100%" alt="Python 3. Built-in HTTPServer on the backend. Vanilla JS and CSS. No frameworks, because it runs as a PWA on an old iPad. Under 100KB of JS. Data lives in simple, portable JSON files."></picture>

| Layer | Technology |
|-------|------------|
| Backend | Python 3 + built-in HTTPServer |
| Frontend | Vanilla JS, CSS (no frameworks) |
| Voice | Web Speech API + OpenAI Whisper |
| OCR | Claude Vision API |
| AI Chat | Claude API |
| Data | JSON files (simple, portable) |

**Why no frameworks?** This runs on an old iPad as a PWA. Every KB matters. Total JS is under 100KB.

```
┌─────────────────────┐     ┌─────────────────────┐
│   Browser (PWA)     │────▶│   Python Server     │
│   - Voice capture   │     │   - API endpoints   │
│   - Camera access   │     │   - File serving    │
│   - Offline capable │     │   - JSON storage    │
└─────────────────────┘     └─────────────────────┘
                                     │
                    ┌────────────────┴────────────────┐
                    ▼                                 ▼
            ┌───────────────┐               ┌───────────────┐
            │ OpenAI Whisper│               │  Claude API   │
            │ (voice→text)  │               │ (OCR + Chat)  │
            └───────────────┘               └───────────────┘
```

<details>
<summary><b>File structure</b></summary>

```
Family-Planner/
├── server.py           # Main HTTP server
├── data.py             # Family config, holidays, school menus
├── handlers.py         # JSON file operations
├── fp_auth.py          # Optional password gate (behind a reverse proxy)
├── static/
│   ├── index.html      # Main dashboard
│   ├── css/
│   │   ├── variables.css   # Design tokens
│   │   ├── base.css        # Reset & typography
│   │   ├── layout.css      # Grid structure
│   │   ├── calendar.css    # Calendar styling
│   │   ├── components.css  # Buttons, modals, widgets
│   │   ├── themes.css      # Seasonal themes
│   │   └── responsive.css  # Mobile optimization
│   └── js/
│       ├── app.js          # Main app logic
│       ├── calendar.js     # Calendar rendering
│       ├── chores.js       # Kids task system
│       ├── meals.js        # Meal planning
│       ├── shopping.js     # Shopping list
│       ├── voice.js        # Speech recognition
│       ├── themes.js       # Seasonal theming
│       ├── celebrations.js # Kid reward animations
│       ├── screensaver.js  # Video screensaver
│       └── ocr.js          # Document scanning
├── video_ocean_*.mp4   # Screensaver videos (not included, add your own)
└── *.json              # Data files (gitignored)
```

</details>

<img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s03-rule.svg" width="100%" alt="">

<a id="setup"></a>
<picture><source media="(max-width: 610px), (min-width: 768px) and (max-width: 895px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s04-banner-m.svg"><source media="(max-width: 1149px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s04-banner-mid.svg"><img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s04-banner.svg" width="100%" alt="04. Setup. Clone, add your keys, run"></picture>
<picture><source media="(max-width: 610px), (min-width: 768px) and (max-width: 895px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s04-r1-m.svg"><source media="(max-width: 1149px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s04-r1-mid.svg"><img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s04-r1.svg" width="100%" alt="Python 3 with a venv. Install the anthropic and openai packages for the AI features. Two API keys. OpenAI for Whisper voice, Anthropic for OCR and Fia chat. Runs on port 8766. Open localhost:8766, or install it as a PWA from Safari."></picture>

### 1. Clone & Install

```bash
git clone https://github.com/nicedreamzapp/Family-Planner.git
cd Family-Planner
python3 -m venv .venv
source .venv/bin/activate
pip install anthropic openai  # For AI features
```

### 2. Configure API Keys

```bash
export OPENAI_API_KEY="your-key"      # For Whisper voice transcription
export ANTHROPIC_API_KEY="your-key"   # For OCR and Fia chat
```

### 3. Configure location and storage (optional)

Put these in the environment or a `.env` file next to `server.py`:

```bash
WEATHER_LAT=0            # your latitude (weather comes from Open-Meteo, no key needed)
WEATHER_LON=0            # your longitude
WEATHER_TZ=auto          # e.g. America/New_York
PORT=8766                # port the server listens on
FP_DATA_DIR=/path/to/data  # where the JSON data files live (default: next to the code)
```

### 4. Run

```bash
python3 server.py
```

Open `http://localhost:8766` in your browser.

If you put the planner behind nginx (which sets `X-Real-IP`), requests from outside are
password-gated by `fp_auth.py`. Set the password once with
`python3 -c "import fp_auth; fp_auth.set_password(input('password: '))"`.

### 5. Install as PWA (Optional)

On iPad/iPhone Safari:
1. Go to your server's URL
2. Share → Add to Home Screen
3. Now it runs like a native app

<img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s04-rule.svg" width="100%" alt="">

<a id="customize"></a>
<picture><source media="(max-width: 610px), (min-width: 768px) and (max-width: 895px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s05-banner-m.svg"><source media="(max-width: 1149px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s05-banner-mid.svg"><img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s05-banner.svg" width="100%" alt="05. Customization and themes. Make it yours"></picture>
<picture><source media="(max-width: 610px), (min-width: 768px) and (max-width: 895px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s05-r1-m.svg"><source media="(max-width: 1149px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s05-r1-mid.svg"><img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s05-r1.svg" width="100%" alt="Family members. Edit the FAMILY block in data.py. Monthly video backgrounds. Add a video, register it in themes.js, add a CSS theme. School menu. Replace the small example menu with your own."></picture>

### Change Family Members
Edit `data.py`:
```python
FAMILY = {
    "dad": {"name": "Dad", "color": "#5B9BD5", "emoji": "👨", "role": "dad"},
    "mom": {"name": "Mom", "color": "#E36B9A", "emoji": "👩", "role": "mom"},
    "kid1": {"name": "Kid 1", "color": "#9B59B6", "emoji": "👧", "role": "daughter"},
    "kid2": {"name": "Kid 2", "color": "#F39C12", "emoji": "👧", "role": "daughter"},
}
```

### Add Monthly Video Backgrounds
1. Add your video to `static/` (e.g., `february-bg.mp4`)
2. Edit `themes.js` to add the month:
```javascript
const MONTHLY_VIDEOS = {
    0: '/static/january-bg.mp4',
    1: '/static/february-bg.mp4',  // Add this
    11: '/static/december-bg.mp4'
};
```
3. Add CSS theme in `themes.css` (copy January theme, rename classes)

### School Menu
`data.py` ships with a tiny example `SCHOOL_LUNCHES` / `SCHOOL_BREAKFAST` / `SCHOOL_SNACK`.
Replace them with your own school's menu (lunches are keyed by date, breakfast/snack by weekday).

### Modify Chores
Edit `chores.json` or use the default in `handlers.py`.

<details>
<summary><b>Voice command examples and seasonal themes</b></summary>

### Voice Command Examples

| Say This | Result |
|----------|--------|
| "Dentist appointment Friday at 2" | Creates calendar event |
| "kid1 made her bed" | Marks chore complete + celebration |
| "Add milk and eggs" | Adds to shopping list |
| "Tacos for Tuesday dinner" | Sets meal plan |
| "What's happening tomorrow?" | Fia reads calendar |

### Seasonal Themes

The calendar automatically applies themes based on the viewing month:

| Month | Theme | Features |
|-------|-------|----------|
| January | New Year | Sparkles, video background |
| February | Valentine's | Hearts, pink tones |
| October | Halloween | Pumpkins, orange/purple |
| December | Winter | Snow video, Christmas decorations |

Each theme adjusts:
- Background video/animation
- Corner decorations
- Color palette
- Particle effects

</details>

<img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s05-rule.svg" width="100%" alt="">

<a id="why"></a>
<picture><source media="(max-width: 610px), (min-width: 768px) and (max-width: 895px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s06-banner-m.svg"><source media="(max-width: 1149px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s06-banner-mid.svg"><img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s06-banner.svg" width="100%" alt="06. Why I built this. Full control over the family hub"></picture>
<picture><source media="(max-width: 610px), (min-width: 768px) and (max-width: 895px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s06-r1-m.svg"><source media="(max-width: 1149px)" srcset="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s06-r1-mid.svg"><img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s06-r1.svg" width="100%" alt="Self-hosted. Runs locally, no cloud dependency. Fully customizable. Change anything in the code. No subscriptions. One-time setup, and it is open source under the MIT license."></picture>

I wanted full control over my family's command center:
- **Self-hosted** - runs locally, no cloud dependency
- **Fully customizable** - change anything in the code
- **AI-powered** - Claude for OCR and chat, Whisper for voice
- **No subscriptions** - one-time setup, runs forever
- **Open source** - learn from it, modify it, make it yours

### License

MIT - Do whatever you want with it.

<img src="https://raw.githubusercontent.com/nicedreamzapp/Family-Planner/6a4bef0b434ce74049b96cfcc285ee6549d1b010/assets/readme/s06-rule.svg" width="100%" alt="">
