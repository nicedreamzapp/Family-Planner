/* ==============================================
   Calendar.js - Calendar Rendering & Events
   Family Planner Application
   ============================================== */

// ==============================================
// Moon Phase Calculator
// ==============================================
function getMoonPhase(year, month, day) {
    // Calculate moon phase based on lunar cycle
    // Known new moon: January 18, 2026
    const knownNewMoon = new Date(2026, 0, 18);
    const targetDate = new Date(year, month, day);
    const lunarCycle = 29.53059; // days

    // Days since known new moon
    const daysDiff = (targetDate - knownNewMoon) / (1000 * 60 * 60 * 24);

    // Position in lunar cycle (0-1)
    let phase = (daysDiff % lunarCycle) / lunarCycle;
    if (phase < 0) phase += 1; // Handle negative values for dates before known new moon

    // Return moon emoji based on phase
    // 0 = new moon, 0.5 = full moon
    if (phase < 0.0625) return { emoji: '🌑', name: 'New Moon' };
    if (phase < 0.1875) return { emoji: '🌒', name: 'Waxing Crescent' };
    if (phase < 0.3125) return { emoji: '🌓', name: 'First Quarter' };
    if (phase < 0.4375) return { emoji: '🌔', name: 'Waxing Gibbous' };
    if (phase < 0.5625) return { emoji: '🌕', name: 'Full Moon' };
    if (phase < 0.6875) return { emoji: '🌖', name: 'Waning Gibbous' };
    if (phase < 0.8125) return { emoji: '🌗', name: 'Last Quarter' };
    if (phase < 0.9375) return { emoji: '🌘', name: 'Waning Crescent' };
    return { emoji: '🌑', name: 'New Moon' };
}

// ==============================================
// Month Navigation
// ==============================================
function renderMonthNav() {
    document.getElementById('monthNav').innerHTML = monthAbbrev.map((m, i) => `
        <button class="month-btn ${i === expandedMonth ? 'current' : ''}" onclick="openMonth(${i})">${m}</button>
    `).join('');
}

function openMonth(month) {
    if (month > 11) {
        month = 0;
        currentYear++;
        if (currentYear > 2030) currentYear = 2030;
    } else if (month < 0) {
        month = 11;
        currentYear--;
        if (currentYear < 2024) currentYear = 2024;
    }
    expandedMonth = month;
    renderMonthNav();
    renderCalendar();
    // Update theme based on month being viewed
    applySeasonalTheme(month);
    setTimeout(() => {
        const el = document.getElementById('month-' + month);
        if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 100);
}

function changeYear(delta) {
    currentYear += delta;
    if (currentYear < 2024) currentYear = 2024;
    if (currentYear > 2030) currentYear = 2030;
    renderCalendar();
}

function scrollToToday() {
    const today = new Date();
    currentYear = today.getFullYear();
    expandedMonth = today.getMonth();
    renderMonthNav();
    renderCalendar();
}

function scrollToMonth(month) {
    openMonth(month);
}

// ==============================================
// Calendar Rendering
// ==============================================
function renderCalendar() {
    const today = new Date();
    document.getElementById('yearTitle').textContent = currentYear;
    renderPreview(today);
    document.getElementById('yearCalendar').innerHTML = renderExpandedMonth(currentYear, expandedMonth, today);
}

function renderPreview(today) {
    const previewGrid = document.getElementById('previewGrid');
    if (!previewGrid) return;

    const dayNamesShort = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    let html = '';

    for (let i = 0; i < 4; i++) {
        const date = new Date(today);
        date.setDate(today.getDate() + i);
        const dateStr = getLocalDateString(date);
        const dayName = dayNamesShort[date.getDay()];
        const dayNum = date.getDate();

        let dayClass = 'preview-day';
        if (i === 0) dayClass += ' today';
        else if (i === 1) dayClass += ' tomorrow';

        const dayEvents = data.calendar.events.filter(e => e.date === dateStr);
        const holiday = data.holidays[dateStr];

        html += `<div class="${dayClass}">`;
        html += `<div class="preview-day-header">`;
        html += `<span class="preview-day-name">${i === 0 ? 'Today' : i === 1 ? 'Tomorrow' : dayName}</span>`;
        html += `<span class="preview-day-num">${dayNum}</span>`;
        html += `</div>`;
        html += `<div class="preview-events">`;

        if (holiday) {
            html += `<div class="preview-event holiday">${holiday}</div>`;
        }

        dayEvents.forEach(event => {
            let emoji = '';
            const titleLower = event.title.toLowerCase();
            if (titleLower.includes('birthday')) emoji = '\uD83C\uDF82 ';
            else if (titleLower.includes('grammy') || titleLower.includes('grandma')) emoji = '\uD83D\uDC75 ';
            else if (titleLower.includes('grandpa') || titleLower.includes('grandfather')) emoji = '\uD83D\uDC74 ';
            else if (titleLower.includes('dentist')) emoji = '\uD83E\uDDB7 ';
            else if (titleLower.includes('doctor') || titleLower.includes('appointment')) emoji = '\uD83C\uDFE5 ';
            else if (titleLower.includes('school')) emoji = '\uD83C\uDFEB ';
            else if (titleLower.includes('party')) emoji = '\uD83C\uDF89 ';
            else if (titleLower.includes('visit') || titleLower.includes('coming')) emoji = '\uD83C\uDFE0 ';

            const eventClass = titleLower.includes('birthday') ? 'preview-event birthday' : 'preview-event';
            html += `<div class="${eventClass}">${emoji}${event.title}</div>`;
        });

        if (!holiday && dayEvents.length === 0) {
            html += `<div style="color:#999; font-size:11px; font-style:italic;">No events</div>`;
        }

        html += `</div></div>`;
    }

    previewGrid.innerHTML = html;
}

function renderExpandedMonth(year, month, today) {
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const startDay = firstDay.getDay();
    const daysInMonth = lastDay.getDate();

    let html = `
        <div class="expanded-month" id="month-${month}">
            <div class="expanded-header">
                <button class="nav-arrow" onclick="event.stopPropagation(); openMonth(${month - 1})">\u25C0</button>
                <h2 class="month-title">${monthNames[month]} ${year}</h2>
                <button class="nav-arrow" onclick="event.stopPropagation(); openMonth(${month + 1})">\u25B6</button>
            </div>
            <div class="calendar-grid">
                <div class="day-header-row">
                    ${dayNames.map((d, i) => `<div class="day-header-cell ${i === 0 || i === 6 ? 'weekend' : ''}">${d}</div>`).join('')}
                </div>
    `;

    // Previous month padding
    const prevMonth = new Date(year, month, 0);
    const prevDays = prevMonth.getDate();
    for (let i = startDay - 1; i >= 0; i--) {
        const d = prevDays - i;
        html += `<div class="calendar-day other-month"><div class="day-num">${d}</div></div>`;
    }

    // Current month days
    for (let day = 1; day <= daysInMonth; day++) {
        const dateStr = `${year}-${String(month + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
        const date = new Date(year, month, day);
        const isToday = date.toDateString() === today.toDateString();
        const isWeekend = date.getDay() === 0 || date.getDay() === 6;
        const events = data.calendar.events.filter(e => e.date === dateStr);
        const holiday = data.holidays[dateStr];
        const lunch = data.lunches[dateStr];
        // Breakfast only shows if there's a lunch (meaning school is in session)
        const dayOfWeekNames = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
        const dayOfWeek = dayOfWeekNames[date.getDay()];
        const breakfast = lunch ? data.breakfast[dayOfWeek] : null; // Only show breakfast on school days
        const hasSchoolMeals = lunch && !isWeekend;

        // Normalize both dates to midnight for accurate day comparison
        const todayMidnight = new Date(today.getFullYear(), today.getMonth(), today.getDate());
        const dateMidnight = new Date(year, month, day);
        const daysFromToday = Math.round((dateMidnight - todayMidnight) / (1000 * 60 * 60 * 24));
        const holidayClass = holiday ? getHolidayClass(holiday.name) : '';

        // Build day classes based on distance from today
        let dayClasses = 'calendar-day';
        if (isToday) {
            dayClasses += ' today';
        } else if (daysFromToday === 1) {
            dayClasses += ' tomorrow';
        } else if (daysFromToday === -1) {
            dayClasses += ' yesterday';
        } else if (daysFromToday >= 2 && daysFromToday <= 3) {
            dayClasses += ' near-future-close';
        } else if (daysFromToday >= 4 && daysFromToday <= 7) {
            dayClasses += ' near-future';
        } else if (daysFromToday >= 8 && daysFromToday <= 14) {
            dayClasses += ' far-future';
        } else if (daysFromToday > 14) {
            dayClasses += ' distant-future';
        } else if (daysFromToday >= -3 && daysFromToday <= -2) {
            dayClasses += ' recent-past';
        } else if (daysFromToday >= -7 && daysFromToday <= -4) {
            dayClasses += ' past-week';
        } else if (daysFromToday < -7) {
            dayClasses += ' distant-past';
        }
        if (isWeekend) dayClasses += ' weekend';

        // Get moon phase for this day
        const moonPhase = getMoonPhase(year, month, day);

        // Get weather for this day (only show for today and next 2 days)
        const weather = (daysFromToday >= 0 && daysFromToday <= 2) ? weatherForecastByDate[dateStr] : null;

        // Render day cell
        if (isToday) {
            html += `
                <div class="${dayClasses}" onclick="showDayDetail('${dateStr}')">
                    <div class="day-header-info">
                        <div class="day-num">${day}</div>
                        ${weather ? `<div class="day-weather-card"><span class="weather-emoji">${weather.emoji}</span><span class="weather-temps">${weather.high}°</span>${weather.rain > 30 ? `<span class="rain-chance">☔${weather.rain}%</span>` : ''}</div>` : ''}
                        <div class="moon-phase" title="${moonPhase.name}">${moonPhase.emoji}</div>
                    </div>
                    ${holiday ? `<div class="holiday-pill ${holidayClass}"><span class="emoji">${holiday.emoji}</span>${holiday.name}</div>` : ''}
                    ${hasSchoolMeals ? `
                        <div class="school-meals-block">
                            ${breakfast ? `<div class="meal-line breakfast">🥣 ${breakfast}</div>` : ''}
                            ${lunch ? `<div class="meal-line lunch">🍽️ ${lunch}</div>` : ''}
                        </div>
                    ` : ''}
                    <div class="day-events">
                        ${events.slice(0, 3).map(e => `<div class="event-pill ${e.person}" onclick="event.stopPropagation(); showDayDetail('${dateStr}')">${e.title}<button class="pill-delete" onclick="event.stopPropagation(); deleteEventFromCalendar(${e.id})">\u2715</button></div>`).join('')}
                    </div>
                    <div class="today-chores-container">
                        <div class="chore-column kid1">
                            <div class="chore-column-header">Emma</div>
                            <div id="kid1Chores"></div>
                        </div>
                        <div class="chore-column kid2">
                            <div class="chore-column-header">Sophie</div>
                            <div id="kid2Chores"></div>
                        </div>
                    </div>
                </div>
            `;
        } else {
            html += `
                <div class="${dayClasses}" onclick="showDayDetail('${dateStr}')">
                    <div class="day-header-info">
                        <div class="day-num">${day}</div>
                        ${weather ? `<div class="day-weather-card"><span class="weather-emoji">${weather.emoji}</span><span class="weather-temps">${weather.high}°</span>${weather.rain > 30 ? `<span class="rain-chance">☔${weather.rain}%</span>` : ''}</div>` : ''}
                        <div class="moon-phase" title="${moonPhase.name}">${moonPhase.emoji}</div>
                    </div>
                    <div class="day-events">
                        ${holiday ? `<div class="holiday-pill ${holidayClass}"><span class="emoji">${holiday.emoji}</span>${holiday.name}</div>` : ''}
                        ${hasSchoolMeals ? `
                            <div class="school-meals-block">
                                ${breakfast ? `<div class="meal-line breakfast">🥣 ${breakfast}</div>` : ''}
                                ${lunch ? `<div class="meal-line lunch">🍽️ ${lunch}</div>` : ''}
                            </div>
                        ` : ''}
                        ${events.slice(0, 4).map(e => `<div class="event-pill ${e.person}">${e.title}${daysFromToday >= 0 ? `<button class="pill-delete" onclick="event.stopPropagation(); deleteEventFromCalendar(${e.id})">\u2715</button>` : ''}</div>`).join('')}
                        ${events.length > 4 ? `<div class="event-pill family">+${events.length - 4} more</div>` : ''}
                    </div>
                </div>
            `;
        }
    }

    // Next month padding
    const totalCells = startDay + daysInMonth;
    const remaining = totalCells % 7 === 0 ? 0 : 7 - (totalCells % 7);
    for (let i = 1; i <= remaining; i++) {
        html += `<div class="calendar-day other-month"><div class="day-num">${i}</div></div>`;
    }

    html += '</div></div>';
    return html;
}

// ==============================================
// Today's Events Sidebar
// ==============================================
function renderTodayEvents() {
    const today = getLocalDateString();
    const events = data.calendar.events.filter(e => e.date === today);
    const holiday = data.holidays[today];

    let html = '';

    if (holiday) {
        html += `
            <div class="today-event" style="border-color: ${holiday.color}">
                <span style="font-size:18px;margin-right:8px">${holiday.emoji}</span>
                <span class="event-title">${holiday.name}</span>
            </div>
        `;
    }

    if (events.length) {
        html += events.map(e => `
            <div class="today-event" style="border-color: ${data.family[e.person]?.color || '#666'}">
                <span class="event-time">${e.time || ''}</span>
                <span class="event-title">${e.title}</span>
            </div>
        `).join('');
    }

    if (!html) {
        html = '<div style="color:var(--text-muted);font-size:13px;padding:8px">No events today</div>';
    }

    document.getElementById('todayEvents').innerHTML = html;
}

// ==============================================
// Event Management
// ==============================================
function openAddEventForDate(dateStr) {
    clickedDate = dateStr;
    showAddEvent();
}

function showAddEvent() {
    // Reset edit mode
    editingEventId = null;

    document.getElementById('eventDate').value = clickedDate || getLocalDateString();
    document.getElementById('eventTitle').value = '';
    document.getElementById('eventTime').value = '';
    selectedPerson = 'family';

    // Show date and time inputs for new events
    document.getElementById('eventDate').style.display = '';
    document.getElementById('eventTime').style.display = '';

    // Reset modal title
    const modalTitle = document.querySelector('#eventModal h2');
    if (modalTitle) modalTitle.textContent = 'Add Event';

    const personGridEl = document.getElementById('personGrid');
    if (personGridEl) {
        personGridEl.innerHTML = Object.entries(data.family).map(([key, p]) => `
            <div class="person-opt ${key === 'family' ? 'selected' : ''}"
                 style="color: ${p.color}"
                 onclick="selectPerson('${key}', this)">
                <span class="emoji">${p.emoji}</span>
                <span class="name">${p.name}</span>
            </div>
        `).join('');
    }

    document.getElementById('eventModal').classList.add('show');
}

function selectPerson(person, el) {
    selectedPerson = person;
    document.querySelectorAll('.person-opt').forEach(p => p.classList.remove('selected'));
    el.classList.add('selected');
}

async function saveEvent() {
    const title = document.getElementById('eventTitle').value;
    const date = document.getElementById('eventDate').value;
    const time = document.getElementById('eventTime').value;
    if (!title || !date) return;

    if (editingEventId) {
        // EDIT MODE - update existing event
        const eventIdx = data.calendar.events.findIndex(e => e.id === editingEventId);
        if (eventIdx !== -1) {
            data.calendar.events[eventIdx] = {
                ...data.calendar.events[eventIdx],
                title, date, time, person: selectedPerson
            };
        }

        closeModal('eventModal');
        renderCalendar();
        renderTodayEvents();

        // Delete old and add updated (simple update approach)
        await fetch('/api/calendar/delete', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id: editingEventId })
        });

        const res = await fetch('/api/calendar/add', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, date, time, person: selectedPerson })
        });
        const result = await res.json();
        if (result.success && eventIdx !== -1) {
            data.calendar.events[eventIdx].id = result.event.id;
        }

        editingEventId = null;
    } else {
        // ADD MODE - create new event
        const tempId = Date.now();
        const newEvent = { id: tempId, title, date, time, person: selectedPerson };

        data.calendar.events.push(newEvent);
        closeModal('eventModal');
        renderCalendar();
        renderTodayEvents();

        fetch('/api/calendar/add', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, date, time, person: selectedPerson })
        }).then(res => res.json()).then(result => {
            if (result.success) {
                const idx = data.calendar.events.findIndex(e => e.id === tempId);
                if (idx !== -1) data.calendar.events[idx].id = result.event.id;
            }
        });
    }
}

async function deleteEvent(eventId, dateStr, btn) {
    const eventItem = btn.closest('.event-item');
    eventItem.style.transition = 'opacity 0.2s, transform 0.2s';
    eventItem.style.opacity = '0';
    eventItem.style.transform = 'translateX(20px)';

    data.calendar.events = data.calendar.events.filter(e => e.id !== eventId);
    renderCalendar();
    renderTodayEvents();

    setTimeout(() => eventItem.remove(), 200);

    fetch('/api/calendar/delete', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: eventId })
    });
}

// Edit event - stores the event being edited
let editingEventId = null;

function editEvent(eventId, dateStr) {
    const event = data.calendar.events.find(e => e.id === eventId);
    if (!event) return;

    editingEventId = eventId;
    clickedDate = dateStr;

    // Close day detail modal
    closeModal('dayModal');

    // Set values
    document.getElementById('eventDate').value = event.date;
    document.getElementById('eventTitle').value = event.title;
    document.getElementById('eventTime').value = event.time || '';
    selectedPerson = event.person || 'family';

    // Hide date and time inputs when editing (not needed)
    document.getElementById('eventDate').style.display = 'none';
    document.getElementById('eventTime').style.display = 'none';

    const personGridEl = document.getElementById('personGrid');
    if (personGridEl) {
        personGridEl.innerHTML = Object.entries(data.family).map(([key, p]) => `
            <div class="person-opt ${key === selectedPerson ? 'selected' : ''}"
                 style="color: ${p.color}"
                 onclick="selectPerson('${key}', this)">
                <span class="emoji">${p.emoji}</span>
                <span class="name">${p.name}</span>
            </div>
        `).join('');
    }

    // Update modal title to show "Edit Event"
    const modalTitle = document.querySelector('#eventModal h2');
    if (modalTitle) modalTitle.textContent = 'Edit Event';

    document.getElementById('eventModal').classList.add('show');
}

function deleteEventFromCalendar(eventId) {
    data.calendar.events = data.calendar.events.filter(e => e.id !== eventId);
    renderCalendar();
    renderTodayEvents();

    fetch('/api/calendar/delete', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: eventId })
    });
}

// ==============================================
// Day Detail Modal - Full Day View
// ==============================================
function showDayDetail(dateStr) {
    clickedDate = dateStr;
    const date = new Date(dateStr + 'T12:00:00');
    const events = data.calendar.events.filter(e => e.date === dateStr);
    const holiday = data.holidays[dateStr];
    const lunch = data.lunches[dateStr];
    const dayOfWeekNames = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
    const dayOfWeek = dayOfWeekNames[date.getDay()];
    const breakfast = lunch ? data.breakfast[dayOfWeek] : null;
    const isWeekend = date.getDay() === 0 || date.getDay() === 6;
    const moonPhase = getMoonPhase(date.getFullYear(), date.getMonth(), date.getDate());

    document.getElementById('dayModalTitle').textContent = date.toLocaleDateString('en-US', {
        weekday: 'long', month: 'long', day: 'numeric', year: 'numeric'
    });

    let html = '';

    // Moon phase
    html += `<div class="day-detail-moon"><span class="moon-icon">${moonPhase.emoji}</span> ${moonPhase.name}</div>`;

    // Holiday section
    if (holiday) {
        html += `
            <div class="day-detail-section">
                <div class="day-detail-label">Holiday</div>
                <div class="holiday-banner">
                    <span class="emoji">${holiday.emoji}</span>
                    <span class="text">${holiday.name}</span>
                </div>
            </div>
        `;
    }

    // Meals section (only on school days)
    if (lunch && !isWeekend) {
        html += `
            <div class="day-detail-section">
                <div class="day-detail-label">School Meals</div>
                <div class="day-detail-meals">
                    ${breakfast ? `<div class="detail-meal breakfast"><span class="meal-icon">🥣</span><span class="meal-type">Breakfast:</span> ${breakfast}</div>` : ''}
                    <div class="detail-meal lunch"><span class="meal-icon">🍽️</span><span class="meal-type">Lunch:</span> ${lunch}</div>
                </div>
            </div>
        `;
    }

    // Events section
    html += `<div class="day-detail-section">`;
    html += `<div class="day-detail-label">Events</div>`;

    if (events.length) {
        html += `<div class="day-detail-events">`;
        html += events.map(e => `
            <div class="event-item" style="border-left-color: ${data.family[e.person]?.color || 'var(--accent-orange)'}">
                <div class="event-info">
                    <span class="event-person-emoji">${data.family[e.person]?.emoji || '📅'}</span>
                    <span class="title">${e.title}</span>
                </div>
                <span class="time">${e.time || 'All day'}</span>
                <div class="event-actions">
                    <button class="edit-btn" onclick="event.stopPropagation(); editEvent(${e.id}, '${dateStr}')" title="Edit event">✎</button>
                    <button class="delete-btn" onclick="event.stopPropagation(); deleteEvent(${e.id}, '${dateStr}', this)" title="Delete event">✕</button>
                </div>
            </div>
        `).join('');
        html += `</div>`;
    } else {
        html += `<div class="no-events">No events scheduled</div>`;
    }
    html += `</div>`;

    // Add Event button at bottom
    html += `
        <div class="day-detail-actions">
            <button class="add-event-btn" onclick="closeModal('dayModal'); openAddEventForDate('${dateStr}')">
                <span class="btn-icon">+</span> Add Event
            </button>
        </div>
    `;

    document.getElementById('dayModalContent').innerHTML = html;
    document.getElementById('dayModal').classList.add('show');
}
