/* ==============================================
   App.js - Main Application Entry Point
   Family Planner Application
   ============================================== */

// ==============================================
// Global State
// ==============================================
let selectedKid = 'kid1';
let selectedPerson = 'family';
let selectedMealDay = null;
let clickedDate = null;
let currentYear = new Date().getFullYear();
let expandedMonth = new Date().getMonth();

// Global data store
let data = {
    calendar: { events: [] },
    chores: { chores: [], completed: [] },
    rewards: { points: {}, rewards: [] },
    meals: { thisWeek: {}, favorites: [] },
    shopping: { items: [] },
    polls: { polls: [], votes: [] },
    routines: { routines: {}, progress: {} },
    family: {},
    holidays: {},
    lunches: {},
    breakfast: {},
    snacks: {}
};

// Weather forecast by date (for calendar day cards)
let weatherForecastByDate = {};

// Constants
const monthNames = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December'];
const monthAbbrev = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
const dayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

// ==============================================
// Date Helper - Use LOCAL time, not UTC
// ==============================================
function getLocalDateString(date = new Date()) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

// ==============================================
// Initialization
// ==============================================
async function init() {
    updateClock();
    setInterval(updateClock, 1000);

    // Fetch all data from APIs
    const endpoints = ['calendar', 'chores', 'rewards', 'meals', 'shopping', 'polls', 'routines', 'family', 'holidays', 'lunches', 'breakfast', 'snacks'];
    const results = await Promise.all(endpoints.map(e => fetch(`/api/${e}`).then(r => r.json())));
    endpoints.forEach((e, i) => data[e] = results[i]);

    // Set expanded month to current month
    expandedMonth = new Date().getMonth();

    // Apply seasonal theme
    applySeasonalTheme();

    // Render all components
    renderMonthNav();
    renderCalendar();
    renderTodayChores();
    renderTodayEvents();
    renderShopping();
    renderMeals();
    renderKids();
    updateRewardsDisplay();
    fetchWeather();

    // Refresh weather every 10 minutes
    setInterval(fetchWeather, 600000);
}

// ==============================================
// Clock & Time
// ==============================================
function updateClock() {
    const now = new Date();
    const timeStr = now.toLocaleTimeString('en-US', {
        hour: 'numeric', minute: '2-digit', hour12: true
    });
    const dateStr = now.toLocaleDateString('en-US', {
        weekday: 'short', month: 'short', day: 'numeric'
    });
    // Update sidebar (if visible)
    const sidebarTime = document.getElementById('currentTime');
    const sidebarDate = document.getElementById('currentDate');
    if (sidebarTime) sidebarTime.textContent = timeStr;
    if (sidebarDate) sidebarDate.textContent = dateStr;
    // Update header
    const headerTime = document.getElementById('headerTime');
    const headerDate = document.getElementById('headerDate');
    if (headerTime) headerTime.textContent = timeStr;
    if (headerDate) headerDate.textContent = dateStr;
}

// ==============================================
// Weather
// ==============================================
async function fetchWeather() {
    try {
        console.log('Fetching weather...');
        const res = await fetch('/api/weather');
        const weather = await res.json();
        console.log('Weather data:', weather);

        if (weather.current) {
            // Update header weather
            const headerTemp = document.getElementById('headerWeatherTemp');
            const headerIcon = document.getElementById('headerWeatherIcon');
            console.log('Elements:', headerTemp, headerIcon);
            if (headerTemp) headerTemp.textContent = weather.current.temp + '°';
            if (headerIcon) headerIcon.textContent = weather.current.emoji;
            console.log('Weather updated:', weather.current.temp, weather.current.emoji);

            // Store forecast by date for calendar day cards
            weatherForecastByDate = {};
            const today = new Date();

            // Store current day weather
            const todayStr = getLocalDateString(today);
            weatherForecastByDate[todayStr] = {
                emoji: weather.current.emoji,
                high: weather.current.temp,
                low: weather.current.temp,
                rain: 0
            };

            // Store forecast days
            if (weather.forecast) {
                weather.forecast.forEach((day, i) => {
                    const forecastDate = new Date(today);
                    forecastDate.setDate(today.getDate() + i + 1);
                    const dateStr = getLocalDateString(forecastDate);
                    weatherForecastByDate[dateStr] = {
                        emoji: day.emoji,
                        high: day.high,
                        low: day.low,
                        rain: day.rain
                    };
                });
            }

            // Re-render calendar to show weather cards
            renderCalendar();
        }
    } catch (e) {
        console.error("Weather load failed:", e);
        // Show error in UI for debugging
        const headerTemp = document.getElementById('headerWeatherTemp');
        if (headerTemp) headerTemp.textContent = 'ERR';
    }
}

// ==============================================
// Panel Navigation
// ==============================================
function showPanel(panel) {
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));

    const panelId = panel + 'Panel';
    const panelEl = document.getElementById(panelId);
    if (panelEl) panelEl.classList.add('active');

    // Update header
    const calendarNav = document.getElementById('calendarNav');
    const pageTitle = document.getElementById('pageTitle');
    const todayBtn = document.getElementById('todayBtn');
    const monthSelectWrapper = document.getElementById('monthSelectWrapper');

    const titles = {
        'calendar': '',
        'meals': '\uD83C\uDF7D\uFE0F Meal Planner',
        'shopping': '\uD83D\uDED2 Shopping List',
        'kids': '\u2B50 Kids Corner',
        'polls': '\uD83D\uDDF3\uFE0F Family Polls',
        'bedtime': '\uD83C\uDF19 Bedtime Routine'
    };

    // Render panel-specific content
    if (panel === 'polls' && typeof renderPolls === 'function') {
        renderPolls();
    } else if (panel === 'bedtime' && typeof renderBedtime === 'function') {
        renderBedtime();
    }

    if (panel === 'calendar') {
        if (calendarNav) calendarNav.style.display = 'flex';
        if (pageTitle) pageTitle.style.display = 'none';
        if (todayBtn) todayBtn.style.display = '';
        if (monthSelectWrapper) monthSelectWrapper.style.display = '';
    } else {
        if (calendarNav) calendarNav.style.display = 'none';
        if (pageTitle) {
            pageTitle.style.display = '';
            pageTitle.textContent = titles[panel] || panel;
        }
        if (todayBtn) todayBtn.style.display = 'none';
        if (monthSelectWrapper) monthSelectWrapper.style.display = 'none';
    }

    // Update nav buttons visibility
    const navCalendar = document.getElementById('navCalendar');
    const navMeals = document.getElementById('navMeals');
    const navShopping = document.getElementById('navShopping');
    const navLiv = document.getElementById('navLiv');
    const navJane = document.getElementById('navJane');
    const navEvent = document.getElementById('navEvent');
    const navPolls = document.getElementById('navPolls');
    const navBedtime = document.getElementById('navBedtime');

    if (navCalendar) navCalendar.style.display = (panel === 'calendar') ? 'none' : '';
    if (navMeals) navMeals.style.display = (panel === 'meals') ? 'none' : '';
    if (navShopping) navShopping.style.display = (panel === 'shopping') ? 'none' : '';
    // Hide both kid buttons when on kids panel
    if (navLiv) navLiv.style.display = (panel === 'kids') ? 'none' : '';
    if (navJane) navJane.style.display = (panel === 'kids') ? 'none' : '';
    if (navEvent) navEvent.style.display = (panel === 'calendar') ? '' : 'none';
    if (navPolls) navPolls.style.display = (panel === 'polls') ? 'none' : '';
    if (navBedtime) navBedtime.style.display = (panel === 'bedtime') ? 'none' : '';
}

// Show kids panel with specific kid selected
function showKidPanel(kid) {
    // Map 'liv' and 'jane' to 'kid1' and 'kid2' for the existing system
    if (kid === 'liv') selectedKid = 'kid1';
    else if (kid === 'jane') selectedKid = 'kid2';
    else selectedKid = kid;

    showPanel('kids');
    // Update kid card selection using IDs (more reliable)
    const kid1Card = document.getElementById('kid1Card');
    const kid2Card = document.getElementById('kid2Card');
    if (kid1Card) {
        kid1Card.classList.remove('selected');
        if (selectedKid === 'kid1') kid1Card.classList.add('selected');
    }
    if (kid2Card) {
        kid2Card.classList.remove('selected');
        if (selectedKid === 'kid2') kid2Card.classList.add('selected');
    }
    renderKids();
}

// Jump to month from dropdown
function jumpToMonth(month) {
    expandedMonth = parseInt(month);
    renderMonthNav();
    renderCalendar();
    // Update dropdown to match
    const monthSelect = document.getElementById('monthSelect');
    if (monthSelect) monthSelect.value = month;
}

// ==============================================
// Modal Helpers
// ==============================================
function closeModal(id) {
    document.getElementById(id).classList.remove('show');
}

// Close modal on backdrop click
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.modal').forEach(modal => {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) modal.classList.remove('show');
        });
    });
});

// ==============================================
// Fullscreen Mode
// ==============================================
function toggleFullscreen() {
    if (!document.fullscreenElement && !document.webkitFullscreenElement) {
        // Enter fullscreen
        const elem = document.documentElement;
        if (elem.requestFullscreen) {
            elem.requestFullscreen();
        } else if (elem.webkitRequestFullscreen) {
            elem.webkitRequestFullscreen(); // Safari/iOS
        }
    } else {
        // Exit fullscreen
        if (document.exitFullscreen) {
            document.exitFullscreen();
        } else if (document.webkitExitFullscreen) {
            document.webkitExitFullscreen();
        }
    }
}

// Update fullscreen button icon based on state
document.addEventListener('fullscreenchange', updateFullscreenButton);
document.addEventListener('webkitfullscreenchange', updateFullscreenButton);

function updateFullscreenButton() {
    const btn = document.getElementById('navFullscreen');
    if (btn) {
        const isFullscreen = document.fullscreenElement || document.webkitFullscreenElement;
        btn.innerHTML = isFullscreen ? '&#10006; Exit' : '&#9974; Fullscreen';
    }
}

// ==============================================
// Utility Functions
// ==============================================
function getHolidayClass(holidayName) {
    const name = holidayName.toLowerCase();
    // Lunar phases
    if (name.includes('full') && name.includes('moon')) return 'full-moon';
    if (name.includes('new moon')) return 'new-moon';
    // Equinoxes and Solstices
    if (name.includes('spring equinox')) return 'spring-equinox';
    if (name.includes('summer solstice')) return 'summer-solstice';
    if (name.includes('fall equinox')) return 'fall-equinox';
    if (name.includes('winter solstice')) return 'winter-solstice';
    // Major Holidays
    if (name.includes('christmas day') || (name.includes('christmas') && !name.includes('eve'))) return 'christmas';
    if (name.includes('christmas eve')) return 'christmas-eve';
    if (name.includes('new year')) return 'new-years';
    if (name.includes('valentine')) return 'valentines';
    if (name.includes('halloween')) return 'halloween';
    if (name.includes('thanksgiving')) return 'thanksgiving';
    if (name.includes('easter')) return 'easter';
    if (name.includes('patrick')) return 'stpatricks';
    if (name.includes('independence') || name.includes('july 4') || name.includes('4th')) return 'july4th';
    if (name.includes('hanukkah')) return 'hanukkah';
    if (name.includes('kwanzaa')) return 'kwanzaa';
    if (name.includes('mother')) return 'mothers-day';
    if (name.includes('father')) return 'fathers-day';
    if (name.includes('memorial')) return 'memorial-day';
    if (name.includes('veteran')) return 'veterans-day';
    if (name.includes('labor')) return 'labor-day';
    // Cultural/Traditional holidays
    if (name.includes('chinese new year')) return 'chinese-new-year';
    if (name.includes('super bowl')) return 'super-bowl';
    if (name.includes('mardi gras')) return 'mardi-gras';
    if (name.includes('mlk') || name.includes('martin luther king')) return 'mlk-day';
    if (name.includes('tax day')) return 'tax-day';
    if (name.includes('election')) return 'election-day';
    return '';
}

function showRewardAnimation() {
    const emojis = ['\u2B50', '\uD83C\uDF89', '\uD83C\uDF1F', '\u2728', '\uD83C\uDF8A', '\uD83D\uDC4F', '\uD83D\uDCAA', '\uD83C\uDFC6'];
    const emoji = emojis[Math.floor(Math.random() * emojis.length)];
    const el = document.createElement('div');
    el.className = 'reward-animation';
    el.textContent = emoji;
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 800);
}

// ==============================================
// DirecTV App/Browser Launch
// ==============================================
function openDirectTV() {
    // Universal - just open the web stream, works on all devices
    window.open('https://stream.directv.com/watchnow', '_blank');
}

// ==============================================
// Start Application
// ==============================================
init();
