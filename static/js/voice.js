/* ==============================================
   Voice.js - Voice Commands & Speech Recognition
   Family Planner Application
   ============================================== */

// ==============================================
// Refresh All Data Function
// ==============================================
function refreshAllData() {
    /**
     * Refresh all dashboard data after Fia makes changes.
     * Called after confirmation of actions.
     */
    console.log('[Voice] Refreshing all data...');
    if (typeof renderCalendar === 'function') renderCalendar();
    if (typeof renderShopping === 'function') renderShopping();
    if (typeof renderMeals === 'function') renderMeals();
    if (typeof renderChores === 'function') renderChores();
    if (typeof updatePointsDisplay === 'function') updatePointsDisplay();
}

// ==============================================
// Speech Recognition Setup
// ==============================================
let recognition = null;
let currentVoiceContext = null;
let currentMicBtn = null;

// Initialize Web Speech API
if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = true;
    recognition.lang = 'en-US';
}

// ==============================================
// Voice Element Mapping
// ==============================================
function getVoiceElements(context) {
    const map = {
        'calendar': { input: 'calendarVoiceInput', status: 'calendarVoiceStatus' },
        'meals': { input: 'mealsVoiceInput', status: 'mealsVoiceStatus' },
        'chores': { input: 'kidsVoiceInput', status: 'kidsVoiceStatus' },
        'shopping': { input: 'newItem', status: null }
    };
    return map[context] || { input: null, status: null };
}

function setVoiceStatus(context, message, type = '') {
    const els = getVoiceElements(context);
    if (els.status) {
        const statusEl = document.getElementById(els.status);
        if (statusEl) {
            statusEl.textContent = message;
            statusEl.className = 'voice-status-text ' + type;
        }
    }
}

// ==============================================
// Voice Command Functions
// ==============================================
async function startVoiceCommand(context, btn) {
    currentVoiceContext = context;
    currentMicBtn = btn;

    if (btn.classList.contains('recording')) {
        stopVoiceCommand();
        return;
    }

    if (!recognition) {
        setVoiceStatus(context, 'Speech recognition not supported in this browser', 'error');
        return;
    }

    const els = getVoiceElements(context);
    const inputEl = document.getElementById(els.input);

    btn.classList.add('recording');
    btn.textContent = '\u23F9\uFE0F';
    setVoiceStatus(context, '\uD83C\uDFA4 Listening...', 'listening');

    recognition.onresult = (event) => {
        let interimTranscript = '';
        let finalTranscript = '';

        for (let i = event.resultIndex; i < event.results.length; i++) {
            const transcript = event.results[i][0].transcript;
            if (event.results[i].isFinal) {
                finalTranscript += transcript;
            } else {
                interimTranscript += transcript;
            }
        }

        if (inputEl) {
            inputEl.value = finalTranscript || interimTranscript;
        }

        if (finalTranscript) {
            setVoiceStatus(context, 'Processing...', '');
        }
    };

    recognition.onerror = (event) => {
        console.error('Speech recognition error:', event.error);
        let errorMsg = 'Error: ' + event.error;
        if (event.error === 'network') {
            errorMsg = 'No internet - use the text box instead';
        } else if (event.error === 'not-allowed') {
            errorMsg = 'Microphone blocked - check browser settings';
        } else if (event.error === 'no-speech') {
            errorMsg = 'No speech heard - try again';
        } else if (event.error === 'aborted') {
            errorMsg = '';
        }
        if (errorMsg) setVoiceStatus(context, errorMsg, 'error');
        stopVoiceCommand();
        if (errorMsg) setTimeout(() => setVoiceStatus(context, '', ''), 3000);
    };

    recognition.onend = () => {
        stopVoiceCommand();
        if (inputEl && inputEl.value.trim()) {
            processTextCommand(context, inputEl.value);
        }
    };

    try {
        recognition.start();
    } catch (err) {
        console.error('Recognition start error:', err);
        setVoiceStatus(context, 'Could not start listening', 'error');
        stopVoiceCommand();
    }
}

function stopVoiceCommand() {
    if (recognition) {
        try { recognition.stop(); } catch(e) {}
    }
    if (currentMicBtn) {
        currentMicBtn.classList.remove('recording');
        currentMicBtn.textContent = '\uD83C\uDFA4';
    }
}

// ==============================================
// Text Command Processing
// ==============================================
async function processTextCommand(context, text) {
    if (!text || !text.trim()) return;

    const els = getVoiceElements(context);
    setVoiceStatus(context, 'Adding...', '');

    try {
        if (context === 'calendar') {
            const eventData = parseEventText(text);
            const response = await fetch('/api/calendar/add', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(eventData)
            });
            if (response.ok) {
                setVoiceStatus(context, '\u2713 Added: ' + eventData.title, 'success');
                document.getElementById(els.input).value = '';
                // Reload calendar data
                const calData = await fetch('/api/calendar').then(r => r.json());
                data.calendar = calData;
                renderCalendar();
                setTimeout(() => setVoiceStatus(context, '', ''), 3000);
            }
        } else if (context === 'shopping') {
            const items = text.split(/,|and/).map(s => s.trim()).filter(s => s);
            for (const item of items) {
                await fetch('/api/shopping/add', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name: item })
                });
            }
            document.getElementById('newItem').value = '';
            // Reload shopping data
            const shopData = await fetch('/api/shopping').then(r => r.json());
            data.shopping = shopData;
            renderShopping();
        } else if (context === 'meals') {
            const mealData = parseMealText(text);
            await fetch('/api/meals/set', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(mealData)
            });
            setVoiceStatus(context, '\u2713 Meal planned!', 'success');
            document.getElementById(els.input).value = '';
            // Reload meals data
            const mealsData = await fetch('/api/meals').then(r => r.json());
            data.meals = mealsData;
            renderMeals();
            setTimeout(() => setVoiceStatus(context, '', ''), 3000);
        } else if (context === 'chores') {
            const choreData = parseChoreText(text);
            if (choreData.person && choreData.chore) {
                await fetch('/api/chores/complete', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(choreData)
                });
                setVoiceStatus(context, '\u2713 ' + choreData.person + ' completed: ' + choreData.chore, 'success');
                document.getElementById(els.input).value = '';
                renderKids();
                setTimeout(() => setVoiceStatus(context, '', ''), 3000);
            } else {
                setVoiceStatus(context, 'Could not understand. Try: "Liv made her bed"', 'error');
            }
        }
    } catch (err) {
        console.error('Command processing error:', err);
        setVoiceStatus(context, 'Error processing command', 'error');
    }
}

// ==============================================
// Natural Language Parsing - SMART DATE RANGES
// ==============================================
function parseEventText(text) {
    // This now returns an ARRAY of events to support date ranges
    const events = parseEventsWithDateRange(text);
    // For backward compatibility, return first event if only one
    return events.length === 1 ? events[0] : events;
}

function parseEventsWithDateRange(text) {
    const now = new Date();
    const currentYear = now.getFullYear();
    let title = text;
    let startDate = null;
    let endDate = null;
    let time = '';
    let endTime = '';

    const monthMap = { jan:0, feb:1, mar:2, apr:3, may:4, jun:5, jul:6, aug:7, sep:8, oct:9, nov:10, dec:11 };
    const monthNames = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'];

    // Extract time range first (e.g., "9am to 1pm", "9:00 AM - 1:00 PM")
    const timeRangeMatch = text.match(/(\d{1,2})(?::(\d{2}))?\s*(am|pm)?\s*(?:to|-|through|until)\s*(\d{1,2})(?::(\d{2}))?\s*(am|pm)?/i);
    if (timeRangeMatch) {
        let startHours = parseInt(timeRangeMatch[1]);
        const startMins = timeRangeMatch[2] || '00';
        const startAmpm = (timeRangeMatch[3] || timeRangeMatch[6] || 'am').toLowerCase();

        let endHours = parseInt(timeRangeMatch[4]);
        const endMins = timeRangeMatch[5] || '00';
        const endAmpm = (timeRangeMatch[6] || 'pm').toLowerCase();

        // Handle AM/PM
        if (startAmpm === 'pm' && startHours < 12) startHours += 12;
        if (startAmpm === 'am' && startHours === 12) startHours = 0;
        if (endAmpm === 'pm' && endHours < 12) endHours += 12;
        if (endAmpm === 'am' && endHours === 12) endHours = 0;

        time = startHours.toString().padStart(2, '0') + ':' + startMins;
        endTime = endHours.toString().padStart(2, '0') + ':' + endMins;
        title = title.replace(timeRangeMatch[0], '').trim();
    } else {
        // Single time extraction
        const timeMatch = text.match(/(?:at\s+)?(\d{1,2})(?::(\d{2}))?\s*(am|pm)/i);
        if (timeMatch) {
            let hours = parseInt(timeMatch[1]);
            const minutes = timeMatch[2] || '00';
            const ampm = timeMatch[3].toLowerCase();
            if (ampm === 'pm' && hours < 12) hours += 12;
            if (ampm === 'am' && hours === 12) hours = 0;
            time = hours.toString().padStart(2, '0') + ':' + minutes;
            title = title.replace(timeMatch[0], '').trim();
        }
    }

    // DATE RANGE PATTERNS
    // Pattern 1: "December 29 through 31", "Dec 29-31", "December 29th to the 31st"
    const dateRangeMatch = text.match(/(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+(\d{1,2})(?:st|nd|rd|th)?\s*(?:through|thru|to|-)\s*(?:the\s+)?(\d{1,2})(?:st|nd|rd|th)?/i);
    if (dateRangeMatch) {
        const month = monthMap[dateRangeMatch[1].toLowerCase().substring(0,3)];
        const startDay = parseInt(dateRangeMatch[2]);
        const endDay = parseInt(dateRangeMatch[3]);

        startDate = new Date(currentYear, month, startDay);
        endDate = new Date(currentYear, month, endDay);

        // If dates are in the past, use next year
        if (endDate < now) {
            startDate.setFullYear(currentYear + 1);
            endDate.setFullYear(currentYear + 1);
        }

        title = title.replace(dateRangeMatch[0], '').trim();
    }

    // Pattern 2: "Dec 29, 30, and 31" or "December 29 30 31"
    const multiDayMatch = text.match(/(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+(\d{1,2})(?:st|nd|rd|th)?(?:\s*,?\s*(?:and\s+)?(\d{1,2})(?:st|nd|rd|th)?)+/i);
    if (!dateRangeMatch && multiDayMatch) {
        const month = monthMap[multiDayMatch[1].toLowerCase().substring(0,3)];
        const daysStr = multiDayMatch[0].replace(/(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*/i, '');
        const days = daysStr.match(/\d+/g).map(d => parseInt(d));

        if (days.length > 1) {
            startDate = new Date(currentYear, month, Math.min(...days));
            endDate = new Date(currentYear, month, Math.max(...days));
            if (endDate < now) {
                startDate.setFullYear(currentYear + 1);
                endDate.setFullYear(currentYear + 1);
            }
            title = title.replace(multiDayMatch[0], '').trim();
        }
    }

    // Pattern 3: Single date "December 29th" or "Dec 29"
    if (!startDate) {
        const singleDateMatch = text.match(/(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+(\d{1,2})(?:st|nd|rd|th)?/i);
        if (singleDateMatch) {
            const month = monthMap[singleDateMatch[1].toLowerCase().substring(0,3)];
            const day = parseInt(singleDateMatch[2]);
            startDate = new Date(currentYear, month, day);
            if (startDate < now) startDate.setFullYear(currentYear + 1);
            title = title.replace(singleDateMatch[0], '').trim();
        }
    }

    // Pattern 4: "tomorrow", "today"
    if (!startDate && /tomorrow/i.test(text)) {
        startDate = new Date(now);
        startDate.setDate(startDate.getDate() + 1);
        title = title.replace(/tomorrow/i, '').trim();
    }
    if (!startDate && /today/i.test(text)) {
        startDate = new Date(now);
        title = title.replace(/today/i, '').trim();
    }

    // Pattern 5: Day of week - "next Monday", "this Tuesday"
    const dayNames = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
    const dayMatch = text.match(/(?:this|next)?\s*(monday|tuesday|wednesday|thursday|friday|saturday|sunday)/i);
    if (!startDate && dayMatch) {
        const targetDay = dayNames.indexOf(dayMatch[1].toLowerCase());
        startDate = new Date(now);
        const currentDay = startDate.getDay();
        let daysUntil = targetDay - currentDay;
        if (daysUntil <= 0) daysUntil += 7;
        if (/next/i.test(dayMatch[0]) && daysUntil < 7) daysUntil += 7;
        startDate.setDate(startDate.getDate() + daysUntil);
        title = title.replace(dayMatch[0], '').trim();
    }

    // Default to today if no date found
    if (!startDate) {
        startDate = new Date(now);
    }

    // Clean up title
    title = title.replace(/\b(each|every)\s+(day|morning|afternoon|evening)\b/gi, '').trim();
    title = title.replace(/^(add|create|schedule|set|put|have|got)\s+/i, '').trim();
    title = title.replace(/\s+(on|for|at)\s*$/i, '').trim();
    title = title.replace(/\s+/g, ' ').trim();
    if (!title) title = 'Event';
    // Capitalize first letter
    title = title.charAt(0).toUpperCase() + title.slice(1);

    // Generate events array
    const events = [];
    const formatDate = (d) => d.toISOString().split('T')[0];

    if (endDate && endDate > startDate) {
        // Create event for each day in range
        const current = new Date(startDate);
        while (current <= endDate) {
            events.push({
                title: title,
                date: formatDate(current),
                time: time,
                endTime: endTime,
                person: 'family'
            });
            current.setDate(current.getDate() + 1);
        }
    } else {
        // Single event
        events.push({
            title: title,
            date: formatDate(startDate),
            time: time,
            endTime: endTime,
            person: 'family'
        });
    }

    return events;
}

function parseMealText(text) {
    const days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
    let day = null;
    let meal = text;

    for (const d of days) {
        if (text.toLowerCase().includes(d)) {
            day = d;
            meal = text.replace(new RegExp(d, 'i'), '').trim();
            break;
        }
    }

    if (/tonight|today/i.test(text)) {
        day = days[new Date().getDay()];
        meal = text.replace(/tonight|today/i, '').trim();
    }

    meal = meal.replace(/^(plan|set|make|have|cook)\s+/i, '').trim();
    meal = meal.replace(/\s+for\s+(dinner|lunch|breakfast)\s*/i, '').trim();
    if (!meal) meal = 'Dinner';
    if (!day) day = days[new Date().getDay()];

    return { day, meal };
}

function parseChoreText(text) {
    let person = null;
    let chore = text;

    if (/kid1/i.test(text)) {
        person = 'kid1';
        chore = text.replace(/kid1('s)?\s*/i, '').trim();
    } else if (/kid2/i.test(text)) {
        person = 'kid2';
        chore = text.replace(/kid2('s)?\s*/i, '').trim();
    }

    chore = chore.replace(/^(completed|did|finished|made|brushed|cleaned)\s+/i, '').trim();
    chore = chore.replace(/^(her|his|the)\s+/i, '').trim();

    return { person, chore };
}

// ==============================================
// Smart Voice Command - Automatic Intent Detection
// ==============================================
let smartMicBtn = null;
let mediaRecorder = null;
let audioChunks = [];

// Text-to-Speech for voice confirmations
function speakConfirmation(message) {
    if ('speechSynthesis' in window) {
        // Cancel any ongoing speech
        speechSynthesis.cancel();

        const utterance = new SpeechSynthesisUtterance(message);
        utterance.rate = 1.0;
        utterance.pitch = 1.0;
        utterance.volume = 1.0;

        // Try to use a friendly voice
        const voices = speechSynthesis.getVoices();
        const preferredVoice = voices.find(v =>
            v.name.includes('Samantha') ||
            v.name.includes('Google') ||
            v.name.includes('Female') ||
            v.lang.startsWith('en')
        );
        if (preferredVoice) utterance.voice = preferredVoice;

        speechSynthesis.speak(utterance);
    }
}

// Process text command from input box using smart intent detection
async function processSmartTextCommand(text) {
    if (!text || !text.trim()) return;

    // Clear the input
    const inputEl = document.getElementById('calendarVoiceInput');
    if (inputEl) inputEl.value = '';

    // Use the same smart processing
    showSmartVoiceStatus('Processing: "' + text + '"', '');
    await processSmartVoiceCommand(text);
}

async function startSmartVoice(btn) {
    smartMicBtn = btn;

    // If already recording, stop
    if (btn.classList.contains('recording')) {
        stopSmartVoice();
        return;
    }

    try {
        // Request microphone access
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

        btn.classList.add('recording');
        btn.innerHTML = '⏹️';
        showSmartVoiceStatus('🎤 Recording... Click stop when done', 'listening');

        audioChunks = [];

        // Create MediaRecorder
        mediaRecorder = new MediaRecorder(stream, { mimeType: 'audio/webm' });

        mediaRecorder.ondataavailable = (event) => {
            if (event.data.size > 0) {
                audioChunks.push(event.data);
            }
        };

        mediaRecorder.onstop = async () => {
            // Stop all tracks
            stream.getTracks().forEach(track => track.stop());

            if (audioChunks.length === 0) {
                showSmartVoiceStatus('❌ No audio recorded', 'error');
                setTimeout(() => hideSmartVoiceStatus(), 3000);
                return;
            }

            showSmartVoiceStatus('🔄 Processing speech...', '');

            // Create audio blob and send to server
            const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
            await sendAudioForTranscription(audioBlob);
        };

        mediaRecorder.start();

        // Auto-stop after 15 seconds
        setTimeout(() => {
            if (mediaRecorder && mediaRecorder.state === 'recording') {
                stopSmartVoice();
            }
        }, 15000);

    } catch (err) {
        console.error('Microphone error:', err);
        let msg = 'Could not access microphone';
        if (err.name === 'NotAllowedError') {
            msg = 'Microphone access denied. Please allow microphone in browser settings.';
        }
        showSmartVoiceStatus('❌ ' + msg, 'error');
        speakConfirmation(msg);
        setTimeout(() => hideSmartVoiceStatus(), 4000);
    }
}

function stopSmartVoice() {
    if (mediaRecorder && mediaRecorder.state === 'recording') {
        mediaRecorder.stop();
    }
    if (smartMicBtn) {
        smartMicBtn.classList.remove('recording');
        smartMicBtn.innerHTML = '🎤';
    }
}

async function sendAudioForTranscription(audioBlob) {
    try {
        const formData = new FormData();
        formData.append('audio', audioBlob, 'recording.webm');

        const response = await fetch('/api/transcribe', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (result.error) {
            showSmartVoiceStatus('❌ ' + result.error, 'error');
            speakConfirmation(result.error);
            setTimeout(() => hideSmartVoiceStatus(), 4000);
            return;
        }

        const transcript = result.text;
        if (!transcript || transcript.trim() === '') {
            showSmartVoiceStatus('❌ No speech detected', 'error');
            speakConfirmation('I didn\'t catch that. Please try again.');
            setTimeout(() => hideSmartVoiceStatus(), 3000);
            return;
        }

        // Show transcript in input field
        const inputEl = document.getElementById('calendarVoiceInput');
        if (inputEl) inputEl.value = transcript;

        showSmartVoiceStatus('Processing: "' + transcript + '"', '');
        await processSmartVoiceCommand(transcript);

    } catch (err) {
        console.error('Transcription error:', err);
        showSmartVoiceStatus('❌ Failed to process audio', 'error');
        speakConfirmation('Sorry, I couldn\'t process that. Please try again.');
        setTimeout(() => hideSmartVoiceStatus(), 3000);
    }
}

function showSmartVoiceStatus(message, type) {
    let statusEl = document.getElementById('smartVoiceStatus');
    if (!statusEl) {
        statusEl = document.createElement('div');
        statusEl.id = 'smartVoiceStatus';
        statusEl.className = 'smart-voice-status';
        document.body.appendChild(statusEl);
    }
    statusEl.textContent = message;
    statusEl.className = 'smart-voice-status show ' + type;
}

function hideSmartVoiceStatus() {
    const statusEl = document.getElementById('smartVoiceStatus');
    if (statusEl) statusEl.classList.remove('show');
}

// ==============================================
// Smart Intent Detection & Routing - FIA BRAIN INTEGRATION
// ==============================================

// Use Fia's LLM brain for intelligent command processing
let useFiaBrain = true;  // Set to false to use legacy regex mode
let awaitingConfirmation = false;
let pendingAction = null;  // Store parsed action for direct execution

async function processWithFiaBrain(text) {
    /**
     * Send command to Fia's brain for intelligent processing.
     * Fia will:
     * 1. Understand complex multi-date/multi-item requests
     * 2. Fetch current family state for context
     * 3. Ask for confirmation before executing
     * 4. Return structured response
     */
    try {
        showSmartVoiceStatus('🧠 Thinking...', 'processing');

        // Use VPS proxy endpoint instead of localhost (avoids ad blocker issues)
        const response = await fetch('/api/fia-chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });

        if (!response.ok) {
            throw new Error('Fia unavailable');
        }

        const result = await response.json();
        const fiaResponse = result.response || '';

        console.log('[Fia Brain] Response:', fiaResponse);

        // Check if Fia is asking for confirmation
        if (fiaResponse.includes('confirm') || fiaResponse.includes('?')) {
            awaitingConfirmation = true;

            // Parse the action from the response
            pendingAction = parseActionFromResponse(fiaResponse);
            console.log('[Fia] Parsed action:', pendingAction);

            showFiaConfirmation(fiaResponse);
            speakConfirmation(extractSpokenPart(fiaResponse));
            return true;
        }

        // Check if action was completed
        if (fiaResponse.includes('Done!') || fiaResponse.includes('Added') || fiaResponse.includes('Set') || fiaResponse.includes('Marked')) {
            awaitingConfirmation = false;
            showSmartVoiceStatus(fiaResponse, 'success');
            speakConfirmation(fiaResponse);

            // Refresh the dashboard
            setTimeout(() => {
                hideSmartVoiceStatus();
                refreshAllData();
            }, 3000);
            return true;
        }

        // Check if cancelled
        if (fiaResponse.includes('cancelled') || fiaResponse.includes('Okay,')) {
            awaitingConfirmation = false;
            showSmartVoiceStatus(fiaResponse, 'info');
            speakConfirmation(fiaResponse);
            setTimeout(() => hideSmartVoiceStatus(), 3000);
            return true;
        }

        // Check for clarification or error
        if (fiaResponse.includes('trouble') || fiaResponse.includes('rephrase') || fiaResponse.includes('not sure')) {
            showSmartVoiceStatus('🤔 ' + fiaResponse, 'error');
            speakConfirmation(fiaResponse);
            setTimeout(() => hideSmartVoiceStatus(), 5000);
            return true;
        }

        // General response from Fia
        showSmartVoiceStatus(fiaResponse, 'info');
        speakConfirmation(fiaResponse);
        setTimeout(() => hideSmartVoiceStatus(), 5000);
        return true;

    } catch (err) {
        console.log('[Fia Brain] Error:', err.message, '- falling back to regex');
        return false;  // Fall back to regex mode
    }
}

function parseActionFromResponse(response) {
    /**
     * Parse the action from Fia's confirmation message.
     * Examples:
     * - "🍽️ Set Wednesday's dinner to 'Tacos'?" -> {type: 'meal', day: 'wednesday', meal: 'Tacos'}
     * - "📅 Add 'Swim Camp' on 2025-12-31?" -> {type: 'calendar', title: 'Swim Camp', dates: ['2025-12-31']}
     * - "🛒 Add 'Milk' to shopping list?" -> {type: 'shopping', items: ['Milk']}
     */
    const lower = response.toLowerCase();

    // MEAL: "Set Wednesday's dinner (2024-12-31) to 'Tacos'" or "Set Wednesday's dinner to 'Tacos'"
    const mealMatch = response.match(/Set (\w+)'s dinner(?: \((\d{4}-\d{2}-\d{2})\))? to ['"]([^'"]+)['"]/i);
    if (mealMatch) {
        let date = mealMatch[2] || null;
        const day = mealMatch[1].toLowerCase();

        // If no date, calculate from day name
        if (!date) {
            const days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
            const targetDay = days.indexOf(day);
            if (targetDay >= 0) {
                const now = new Date();
                const currentDay = now.getDay();
                let daysAhead = targetDay - currentDay;
                if (daysAhead <= 0) daysAhead += 7;
                const targetDate = new Date(now);
                targetDate.setDate(now.getDate() + daysAhead);
                date = targetDate.toISOString().split('T')[0];
            }
        }

        return {
            type: 'meal',
            day: day,
            date: date,
            meal: mealMatch[3]
        };
    }

    // CALENDAR: "Add 'Event Title' on 2025-12-31" or "Add 'Event' on 3 days"
    const calendarMatch = response.match(/Add ['"]([^'"]+)['"] on (\d{4}-\d{2}-\d{2})/i);
    if (calendarMatch) {
        return {
            type: 'calendar',
            title: calendarMatch[1],
            dates: [calendarMatch[2]]
        };
    }

    // CALENDAR with multiple dates: "Add 'Event' on 3 days"
    const multiCalMatch = response.match(/Add ['"]([^'"]+)['"] on (\d+) days/i);
    if (multiCalMatch) {
        // We need to extract dates from the original parsed data
        // For now, return what we can
        return {
            type: 'calendar',
            title: multiCalMatch[1],
            dates: []  // Will need to be filled in from context
        };
    }

    // SHOPPING: "Add 'Milk' to shopping list" or "Add 3 items to shopping"
    const shoppingMatch = response.match(/Add ['"]([^'"]+)['"] to shopping/i);
    if (shoppingMatch) {
        return {
            type: 'shopping',
            items: [shoppingMatch[1]]
        };
    }

    // SHOPPING multiple: "Add 3 items to shopping: Milk, Eggs, Bread"
    const multiShopMatch = response.match(/Add \d+ items to shopping[^:]*:\s*(.+)\?/i);
    if (multiShopMatch) {
        const itemsStr = multiShopMatch[1];
        const items = itemsStr.split(/,\s*/).map(s => s.trim());
        return {
            type: 'shopping',
            items: items
        };
    }

    console.log('[Parse] Could not parse action from:', response);
    return null;
}

function showFiaConfirmation(message) {
    /**
     * Show Fia's confirmation request in a nice UI.
     */
    // Create or update confirmation modal
    let modal = document.getElementById('fiaConfirmModal');
    if (!modal) {
        modal = document.createElement('div');
        modal.id = 'fiaConfirmModal';
        modal.className = 'fia-confirm-modal';
        modal.innerHTML = `
            <div class="fia-confirm-content">
                <div class="fia-confirm-message"></div>
                <div class="fia-confirm-buttons">
                    <button class="fia-confirm-yes" onclick="confirmFiaAction()">✓ Yes</button>
                    <button class="fia-confirm-mic" onclick="startConfirmMic()">🎤</button>
                    <button class="fia-confirm-no" onclick="cancelFiaAction()">✗ No</button>
                </div>
            </div>
        `;
        document.body.appendChild(modal);
    }

    // Format the message nicely
    const formattedMessage = message
        .replace(/\n/g, '<br>')
        .replace(/📋|📅|🛒|🍽️|✅/g, '<span class="fia-emoji">$&</span>');

    modal.querySelector('.fia-confirm-message').innerHTML = formattedMessage;
    modal.classList.add('show');
}

function hideFiaConfirmation() {
    const modal = document.getElementById('fiaConfirmModal');
    if (modal) {
        modal.classList.remove('show');
    }
}

async function confirmFiaAction() {
    hideFiaConfirmation();

    // Execute action directly on VPS instead of going through Fia again
    if (pendingAction) {
        showSmartVoiceStatus('⏳ Saving...', 'processing');
        try {
            const result = await executeActionDirectly(pendingAction);
            showSmartVoiceStatus(result, 'success');
            speakConfirmation(result);
            pendingAction = null;
            awaitingConfirmation = false;
            setTimeout(() => {
                hideSmartVoiceStatus();
                refreshAllData();
            }, 2000);
        } catch (err) {
            showSmartVoiceStatus('❌ ' + err.message, 'error');
            pendingAction = null;
            awaitingConfirmation = false;
        }
    } else {
        // Fallback to Fia
        await processWithFiaBrain('yes');
    }
}

async function executeActionDirectly(action) {
    /**
     * Execute the action directly on the VPS - no round trip to Mac needed.
     */
    console.log('[Execute] Action:', action);

    if (action.type === 'meal') {
        // Set the meal
        await fetch('/api/meals/set', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ day: action.day, meal: { name: action.meal, icon: '🍽️' } })
        });

        // Calculate date if not provided
        let mealDate = action.date;
        if (!mealDate && action.day) {
            const days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
            const targetDay = days.indexOf(action.day.toLowerCase());
            if (targetDay >= 0) {
                const now = new Date();
                const currentDay = now.getDay();
                let daysAhead = targetDay - currentDay;
                if (daysAhead <= 0) daysAhead += 7;
                const targetDate = new Date(now);
                targetDate.setDate(now.getDate() + daysAhead);
                mealDate = targetDate.toISOString().split('T')[0];
            }
        }

        console.log('[Execute] Meal date:', mealDate);

        // Add to calendar
        if (mealDate) {
            const calendarData = {
                title: '🍽️ ' + action.meal,
                date: mealDate,
                time: '18:00',
                person: 'family'
            };
            console.log('[Execute] Adding to calendar:', calendarData);
            const calRes = await fetch('/api/calendar/add', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(calendarData)
            });
            console.log('[Execute] Calendar response:', calRes.status);
        }

        return `✅ Set ${action.day}'s dinner to '${action.meal}' (+ calendar)`;
    }

    if (action.type === 'calendar') {
        for (const date of action.dates) {
            await fetch('/api/calendar/add', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ title: action.title, date: date, person: 'family', time: action.time || '' })
            });
        }
        return `✅ Added '${action.title}' to calendar`;
    }

    if (action.type === 'shopping') {
        for (const item of action.items) {
            await fetch('/api/shopping/add', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ item: item })
            });
        }
        return `✅ Added ${action.items.length} item(s) to shopping`;
    }

    throw new Error('Unknown action type');
}

async function cancelFiaAction() {
    hideFiaConfirmation();
    pendingAction = null;
    awaitingConfirmation = false;
    showSmartVoiceStatus('Cancelled', 'info');
    setTimeout(() => hideSmartVoiceStatus(), 2000);
}

async function startConfirmMic() {
    // Use speech recognition for confirmation
    if (!recognition) {
        alert('Speech recognition not available');
        return;
    }

    const micBtn = document.querySelector('.fia-confirm-mic');
    if (micBtn) {
        micBtn.classList.add('recording');
        micBtn.textContent = '🔴';
    }

    recognition.onresult = async (event) => {
        const transcript = event.results[event.results.length - 1][0].transcript.trim();
        console.log('[Confirm Mic] Heard:', transcript);

        if (micBtn) {
            micBtn.classList.remove('recording');
            micBtn.textContent = '🎤';
        }

        hideFiaConfirmation();
        await processWithFiaBrain(transcript);
    };

    recognition.onerror = () => {
        if (micBtn) {
            micBtn.classList.remove('recording');
            micBtn.textContent = '🎤';
        }
    };

    recognition.onend = () => {
        if (micBtn) {
            micBtn.classList.remove('recording');
            micBtn.textContent = '🎤';
        }
    };

    recognition.start();
}

function extractSpokenPart(text) {
    /**
     * Extract the key part for text-to-speech (remove formatting).
     */
    return text
        .replace(/📋|📅|🛒|🍽️|✅|\n/g, ' ')
        .replace(/\s+/g, ' ')
        .trim();
}

async function processSmartVoiceCommand(text) {
    console.log('[Voice] Processing:', text);

    // If we're awaiting confirmation, send directly to Fia
    if (awaitingConfirmation) {
        const success = await processWithFiaBrain(text);
        if (success) return;
    }

    // Try Fia brain first if enabled
    if (useFiaBrain) {
        const success = await processWithFiaBrain(text);
        if (success) return;
        console.log('[Voice] Fia brain unavailable, using legacy regex mode');
    }

    // Legacy regex-based processing (fallback)
    const intents = detectMultipleIntents(text);
    console.log('Detected intents:', intents.map(i => i.type), 'from:', text);

    if (intents.length === 0) {
        const msg = 'I\'m not sure what to do with that. Try saying something like: Add milk to the shopping list, or Liv brushed her teeth, or Dentist on Tuesday at 3 PM.';
        showSmartVoiceStatus('🤔 Not sure what to do with that. Try being more specific.', 'error');
        speakConfirmation(msg);
        setTimeout(() => hideSmartVoiceStatus(), 5000);
        return;
    }

    const results = [];
    for (const intent of intents) {
        try {
            switch (intent.type) {
                case 'chore':
                    await handleChoreIntent(intent);
                    results.push('chore');
                    break;
                case 'shopping':
                    await handleShoppingIntent(intent);
                    results.push('shopping');
                    break;
                case 'calendar':
                    await handleCalendarIntent(intent);
                    results.push('calendar');
                    break;
                case 'meal':
                    await handleMealIntent(intent);
                    results.push('meal');
                    break;
            }
        } catch (err) {
            console.error('Intent error:', intent.type, err);
        }
    }

    // If multiple intents were handled, show a summary
    if (results.length > 1) {
        setTimeout(() => {
            showSmartVoiceStatus('✅ Done! Updated ' + results.join(' & '), 'success');
            setTimeout(() => hideSmartVoiceStatus(), 3000);
        }, 500);
    }
}

// Detect multiple intents in a single sentence
function detectMultipleIntents(text) {
    const intents = [];

    // Split by common conjunctions that indicate multiple actions
    // "pork chops for Thursday and add milk to the shopping list"
    // "swim camp Dec 29-31 and also get towels"
    const parts = text.split(/\s+(?:and\s+)?(?:also\s+)?(?:then\s+)?(?:plus\s+)?/i)
        .map(p => p.trim())
        .filter(p => p.length > 2);

    // If we have multiple distinct parts, try each
    if (parts.length > 1) {
        for (const part of parts) {
            const intent = detectIntent(part);
            if (intent.type !== 'unknown') {
                intents.push(intent);
            }
        }
    }

    // If splitting didn't work well, check for compound intents
    if (intents.length < 2) {
        // Look for shopping keywords mixed with other content
        const shoppingMatch = text.match(/(?:add|put|get)\s+(.+?)\s+(?:to|on)\s+(?:the\s+)?(?:shopping|grocery)\s*list/i);
        const mealMatch = text.match(/(.+?)\s+(?:for|on)\s+(?:dinner|lunch|breakfast|tonight|monday|tuesday|wednesday|thursday|friday|saturday|sunday)/i);
        const calendarMatch = text.match(/(.+?)\s+(?:on|at)\s+(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|\d|tomorrow|monday|tuesday|wednesday|thursday|friday|saturday|sunday)/i);

        if (shoppingMatch && (mealMatch || calendarMatch)) {
            // We have both shopping and something else
            const shoppingText = shoppingMatch[0];
            const otherText = text.replace(shoppingText, '').replace(/^\s*and\s*/i, '').trim();

            if (otherText.length > 3) {
                const otherIntent = detectIntent(otherText);
                if (otherIntent.type !== 'unknown' && otherIntent.type !== 'shopping') {
                    intents.push(otherIntent);
                }
            }
            intents.push({ type: 'shopping', text: shoppingText });
        }
    }

    // If we still don't have intents, try single intent detection
    if (intents.length === 0) {
        const intent = detectIntent(text);
        if (intent.type !== 'unknown') {
            intents.push(intent);
        }
    }

    return intents;
}

function detectIntent(text) {
    const lower = text.toLowerCase();

    // CHORE PATTERNS - Kid completing a task
    // "Liv brushed her teeth", "Jane made her bed", "Liv did homework"
    const chorePatterns = [
        /\b(kid1|kid2)\s+(brushed|made|cleaned|did|finished|completed|set|cleared|helped|practiced|was kind)/i,
        /\b(kid1|kid2)('s)?\s+(teeth|bed|room|homework|reading|table|dishes)/i,
        /\b(teeth|bed|room|homework|reading|table|dishes).*(kid1|kid2)/i,
        /\bmark\s+(kid1|kid2).*(done|complete)/i
    ];

    for (const pattern of chorePatterns) {
        if (pattern.test(text)) {
            return { type: 'chore', text };
        }
    }

    // Check for chore keywords with kid names
    const hasKid = /\b(kid1|kid2)\b/i.test(text);
    const choreKeywords = ['brush', 'teeth', 'bed', 'room', 'homework', 'reading', 'table', 'dishes', 'kind', 'chore'];
    const hasChoreWord = choreKeywords.some(w => lower.includes(w));
    if (hasKid && hasChoreWord) {
        return { type: 'chore', text };
    }

    // SHOPPING PATTERNS
    // "Add milk to the shopping list", "We need eggs", "Put bread on the list"
    const shoppingPatterns = [
        /\b(add|put|get|buy|need|pick up).*(shopping|grocery|list|store)/i,
        /\b(shopping|grocery)\s*(list)?.*(add|need|get)/i,
        /\bwe need\b/i,
        /\bpick up\b/i,
        /\brun out of\b/i,
        /\bout of\s+\w+/i
    ];

    for (const pattern of shoppingPatterns) {
        if (pattern.test(text)) {
            return { type: 'shopping', text };
        }
    }

    // MEAL PATTERNS
    // "Tacos for dinner", "Let's have pizza tonight", "Plan spaghetti for Tuesday"
    const mealPatterns = [
        /\b(for|have|make|cook|plan)\s+.*(dinner|lunch|breakfast|tonight|supper)/i,
        /\b(dinner|lunch|breakfast|supper|tonight)\s+.*(is|will be|should be)/i,
        /\btonight.*(eat|have|make)/i,
        /\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday).*(dinner|eat|have)/i
    ];

    for (const pattern of mealPatterns) {
        if (pattern.test(text)) {
            return { type: 'meal', text };
        }
    }

    // CALENDAR PATTERNS (catch-all for events with dates/times)
    // "Dentist on Tuesday at 3pm", "Add soccer practice tomorrow"
    const calendarPatterns = [
        /\b(on|at|this|next)\s+(monday|tuesday|wednesday|thursday|friday|saturday|sunday)/i,
        /\btomorrow\b/i,
        /\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+\d/i,
        /\bat\s+\d{1,2}(:\d{2})?\s*(am|pm)?/i,
        /\b(appointment|meeting|practice|game|class|lesson|party|event)/i,
        /\b(schedule|add|create|set).*(event|appointment|reminder)/i
    ];

    for (const pattern of calendarPatterns) {
        if (pattern.test(text)) {
            return { type: 'calendar', text };
        }
    }

    // DEFAULT: If it mentions a day of week or time, assume calendar
    if (/\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b/i.test(text)) {
        return { type: 'calendar', text };
    }

    // If it starts with "add" and doesn't match other patterns, try shopping
    if (/^add\s+/i.test(text)) {
        return { type: 'shopping', text };
    }

    return { type: 'unknown', text };
}

// ==============================================
// Intent Handlers
// ==============================================
async function handleChoreIntent(intent) {
    const text = intent.text;
    let person = null;

    if (/\bkid1\b/i.test(text)) person = 'kid1';
    else if (/\bkid2\b/i.test(text)) person = 'kid2';

    if (!person) {
        const msg = 'Who completed the chore? Say Liv or Jane.';
        showSmartVoiceStatus('❌ ' + msg, 'error');
        speakConfirmation(msg);
        setTimeout(() => hideSmartVoiceStatus(), 3000);
        return;
    }

    // Find the best matching chore
    const choreMatch = findMatchingChore(text);

    if (!choreMatch) {
        const msg = 'I could not find that chore. Try saying something like Liv brushed her teeth.';
        showSmartVoiceStatus('❌ ' + msg, 'error');
        speakConfirmation(msg);
        setTimeout(() => hideSmartVoiceStatus(), 4000);
        return;
    }

    // Check if already completed today
    const today = new Date().toISOString().split('T')[0];
    const alreadyDone = data.chores.completed.some(c =>
        c.choreId === choreMatch.id && c.person === person && c.date === today
    );

    if (alreadyDone) {
        const personName = person.charAt(0).toUpperCase() + person.slice(1);
        const msg = personName + ' already did ' + choreMatch.name + ' today!';
        showSmartVoiceStatus('ℹ️ ' + msg, '');
        speakConfirmation(msg);
        setTimeout(() => hideSmartVoiceStatus(), 3000);
        return;
    }

    // Complete the chore
    const res = await fetch('/api/chores/complete', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ choreId: choreMatch.id, person })
    });

    if (res.ok) {
        // Update local data
        const pts = choreMatch.points || 0;
        if (data.rewards.points) {
            data.rewards.points[person] = (data.rewards.points[person] || 0) + pts;
        } else {
            data.rewards[person] = (data.rewards[person] || 0) + pts;
        }
        data.chores.completed.push({ choreId: choreMatch.id, person, date: today });

        const personName = person.charAt(0).toUpperCase() + person.slice(1);
        const msg = 'Great job ' + personName + '! ' + choreMatch.name + ' completed. Plus ' + pts + ' stars!';
        showSmartVoiceStatus('✅ ' + personName + ' completed "' + choreMatch.name + '" (+' + pts + '⭐)', 'success');
        speakConfirmation(msg);

        renderKids();
        renderTodayChores();
        if (typeof updateRewardsDisplay === 'function') updateRewardsDisplay();
        showRewardAnimation();

        setTimeout(() => hideSmartVoiceStatus(), 3000);
    }
}

function findMatchingChore(text) {
    const lower = text.toLowerCase();
    const chores = data.chores.chores;

    // Direct keyword matching
    const keywordMap = {
        'teeth': ['brush teeth', 'brushed teeth', 'tooth'],
        'bed': ['make bed', 'made bed'],
        'room': ['clean room', 'cleaned room', 'tidy'],
        'table': ['set table', 'clear table', 'cleared table'],
        'homework': ['homework'],
        'reading': ['reading', 'read', 'practice reading'],
        'dishes': ['dishes', 'help with dishes'],
        'kind': ['kind', 'nice', 'kind to sister']
    };

    for (const [key, keywords] of Object.entries(keywordMap)) {
        if (keywords.some(k => lower.includes(k)) || lower.includes(key)) {
            // Find matching chore
            for (const chore of chores) {
                const choreLower = chore.name.toLowerCase();
                if (choreLower.includes(key)) {
                    // For teeth, check morning vs night
                    if (key === 'teeth') {
                        if (lower.includes('morning') || lower.includes('am')) {
                            if (choreLower.includes('morning')) return chore;
                        } else if (lower.includes('night') || lower.includes('pm') || lower.includes('evening')) {
                            if (choreLower.includes('night')) return chore;
                        } else {
                            // Default to appropriate time of day
                            const hour = new Date().getHours();
                            if (hour < 12) {
                                if (choreLower.includes('morning')) return chore;
                            } else {
                                if (choreLower.includes('night')) return chore;
                            }
                        }
                    } else {
                        return chore;
                    }
                }
            }
        }
    }

    // Fuzzy match by checking if any chore name words appear
    for (const chore of chores) {
        const choreWords = chore.name.toLowerCase().split(' ');
        for (const word of choreWords) {
            if (word.length > 3 && lower.includes(word)) {
                return chore;
            }
        }
    }

    return null;
}

async function handleShoppingIntent(intent) {
    let text = intent.text;

    // Extract items by removing common phrases
    text = text.replace(/\b(add|put|get|buy|need|pick up|we need|to the|on the|shopping|grocery|list|store|please)\b/gi, '');
    text = text.replace(/\s+/g, ' ').trim();

    if (!text) {
        const msg = 'What should I add to the shopping list?';
        showSmartVoiceStatus('❌ ' + msg, 'error');
        speakConfirmation(msg);
        setTimeout(() => hideSmartVoiceStatus(), 3000);
        return;
    }

    // Split by "and" or commas
    const items = text.split(/,|\band\b/).map(s => s.trim()).filter(s => s.length > 0);

    for (const item of items) {
        await fetch('/api/shopping/add', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: item.charAt(0).toUpperCase() + item.slice(1) })
        });
    }

    // Reload shopping data
    const shopData = await fetch('/api/shopping').then(r => r.json());
    data.shopping = shopData;
    renderShopping();

    const itemList = items.join(', ');
    const msg = items.length === 1
        ? 'Added ' + items[0] + ' to the shopping list.'
        : 'Added ' + items.length + ' items to shopping list: ' + itemList;
    showSmartVoiceStatus('🛒 Added: ' + itemList, 'success');
    speakConfirmation(msg);
    setTimeout(() => hideSmartVoiceStatus(), 3000);
}

async function handleCalendarIntent(intent) {
    const events = parseEventsWithDateRange(intent.text);

    // Add all events
    let successCount = 0;
    for (const eventData of events) {
        const res = await fetch('/api/calendar/add', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(eventData)
        });
        if (res.ok) successCount++;
    }

    if (successCount > 0) {
        const calData = await fetch('/api/calendar').then(r => r.json());
        data.calendar = calData;
        renderCalendar();

        const firstEvent = events[0];
        const lastEvent = events[events.length - 1];
        const title = firstEvent.title;
        const timeStr = firstEvent.time ? ' at ' + formatTimeForSpeech(firstEvent.time) : '';

        let msg, statusMsg;
        if (events.length === 1) {
            const dateObj = new Date(firstEvent.date + 'T12:00:00');
            const dateStr = dateObj.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric' });
            msg = 'Added ' + title + ' on ' + dateStr + timeStr + '.';
            statusMsg = '📅 Added "' + title + '" on ' + dateStr + timeStr;
        } else {
            const startDate = new Date(firstEvent.date + 'T12:00:00');
            const endDate = new Date(lastEvent.date + 'T12:00:00');
            const startStr = startDate.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
            const endStr = endDate.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
            msg = 'Added ' + title + ' for ' + events.length + ' days, ' + startStr + ' through ' + endStr + timeStr + '.';
            statusMsg = '📅 Added "' + title + '" for ' + events.length + ' days (' + startStr + ' - ' + endStr + ')' + timeStr;
        }

        showSmartVoiceStatus(statusMsg, 'success');
        speakConfirmation(msg);
        setTimeout(() => hideSmartVoiceStatus(), 4000);
    }
}

function formatTimeForSpeech(time) {
    if (!time) return '';
    const [hours, mins] = time.split(':').map(Number);
    const ampm = hours >= 12 ? 'PM' : 'AM';
    const hour12 = hours % 12 || 12;
    if (mins === 0) return hour12 + ' ' + ampm;
    return hour12 + ':' + mins.toString().padStart(2, '0') + ' ' + ampm;
}

async function handleMealIntent(intent) {
    const mealData = parseMealText(intent.text);

    await fetch('/api/meals/set', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(mealData)
    });

    const mealsData = await fetch('/api/meals').then(r => r.json());
    data.meals = mealsData;
    renderMeals();

    const dayName = mealData.day.charAt(0).toUpperCase() + mealData.day.slice(1);
    const msg = dayName + ' dinner is now ' + mealData.meal + '.';
    showSmartVoiceStatus('🍽️ ' + dayName + ' dinner: ' + mealData.meal, 'success');
    speakConfirmation(msg);
    setTimeout(() => hideSmartVoiceStatus(), 3000);
}

// ==============================================
// Fia Chat Configuration
// ==============================================
// Set this to your Mac's public URL if using ngrok or port forwarding
// Example: 'https://abc123.ngrok.io' or 'http://your-mac-ip:8765'
// Leave as empty string to use same host as dashboard
const FIA_SERVER_URL = '';  // Will be fetched from /api/fia-config or default to localhost

let fiaEndpoint = 'http://localhost:8765/api/chat';

// Try to get Fia config from server
fetch('/api/fia-config')
    .then(r => r.json())
    .then(config => {
        if (config.url) {
            fiaEndpoint = config.url + '/api/chat';
            console.log('[Fia] Configured endpoint:', fiaEndpoint);
        }
    })
    .catch(() => {
        console.log('[Fia] Using default endpoint:', fiaEndpoint);
    });

// ==============================================
// Fia Chat
// ==============================================
function toggleFiaChat() {
    document.getElementById('fiaModal').classList.toggle('show');
}

async function sendFiaMessage() {
    const input = document.getElementById('fiaInput');
    const msg = input.value.trim();
    if (!msg) return;

    const messages = document.getElementById('fiaMessages');
    messages.innerHTML += `
        <div class="fia-message user-message">
            <div class="message-avatar">\uD83D\uDC64</div>
            <div class="message-bubble">${msg}</div>
        </div>
    `;
    input.value = '';
    messages.scrollTop = messages.scrollHeight;

    try {
        const res = await fetch(fiaEndpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: msg })
        });
        const result = await res.json();
        messages.innerHTML += `
            <div class="fia-message fia-response">
                <div class="message-avatar">\uD83E\uDD16</div>
                <div class="message-bubble">${result.response || 'No response'}</div>
            </div>
        `;
    } catch (e) {
        messages.innerHTML += `
            <div class="fia-message fia-response">
                <div class="message-avatar">\uD83E\uDD16</div>
                <div class="message-bubble">I'm having trouble connecting to Fia. Check that Fia is running and accessible.</div>
            </div>
        `;
    }
    messages.scrollTop = messages.scrollHeight;
}

function sendQuickFia(msg) {
    document.getElementById('fiaInput').value = msg;
    sendFiaMessage();
}

// ==============================================
// Fia Microphone
// ==============================================
let fiaMicRecorder = null;
let fiaMicChunks = [];

async function toggleFiaMic() {
    const btn = document.getElementById('fiaChatMic');

    if (btn.classList.contains('recording')) {
        if (fiaMicRecorder && fiaMicRecorder.state === 'recording') {
            fiaMicRecorder.stop();
        }
        btn.classList.remove('recording');
        btn.querySelector('.mic-icon').textContent = '\uD83C\uDFA4';
        return;
    }

    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        fiaMicRecorder = new MediaRecorder(stream);
        fiaMicChunks = [];

        fiaMicRecorder.ondataavailable = e => fiaMicChunks.push(e.data);

        fiaMicRecorder.onstop = async () => {
            stream.getTracks().forEach(track => track.stop());
            document.getElementById('fiaInput').placeholder = 'Voice recorded! Type your message for now...';
        };

        fiaMicRecorder.start();
        btn.classList.add('recording');
        btn.querySelector('.mic-icon').textContent = '\u23F9\uFE0F';

        setTimeout(() => {
            if (fiaMicRecorder && fiaMicRecorder.state === 'recording') {
                toggleFiaMic();
            }
        }, 10000);

    } catch (err) {
        console.error('Mic error:', err);
        alert('Could not access microphone. Please allow microphone access.');
    }
}
