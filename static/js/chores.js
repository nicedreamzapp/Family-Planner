/* ==============================================
   Chores.js - Kids Task Management
   Family Planner Application
   No points - just celebrations!
   ============================================== */

// Track last known date for auto-reset
let lastKnownDate = getLocalDateString();

// ==============================================
// Check for Day Change (Auto-Reset)
// ==============================================
function checkDayChange() {
    const today = getLocalDateString();
    if (today !== lastKnownDate) {
        lastKnownDate = today;
        // New day! Reload the data which will only show today's completed chores
        // (The chores completed array stores dates, so old completions won't show)
        if (data && data.chores) {
            renderKids();
            renderTodayChores();
        }
    }
}

// Check for day change every minute
setInterval(checkDayChange, 60000);

// ==============================================
// Reset Chores (Manual)
// ==============================================
async function resetChores() {
    if (!confirm('Reset all chores for today?')) return;

    try {
        const res = await fetch('/api/chores/reset', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({})
        });
        const result = await res.json();
        if (result.success) {
            // Clear local completed array
            if (data && data.chores) {
                data.chores.completed = [];
            }
            renderKids();
            renderTodayChores();
        }
    } catch (err) {
        console.error('Failed to reset chores:', err);
    }
}

// ==============================================
// Kids Selection
// ==============================================
function selectKid(kid) {
    selectedKid = kid;
    document.getElementById('kid1Card').classList.toggle('selected', kid === 'kid1');
    document.getElementById('kid2Card').classList.toggle('selected', kid === 'kid2');
    renderKids();
}

// ==============================================
// Kids Panel Rendering
// ==============================================
function renderKids() {
    const today = getLocalDateString();

    // Calculate completed tasks for each kid today
    const kid1Completed = data.chores.completed.filter(c => c.person === 'kid1' && c.date === today).length;
    const kid2Completed = data.chores.completed.filter(c => c.person === 'kid2' && c.date === today).length;
    const kid1Total = data.chores.chores.filter(c => c.assignedTo.includes('kid1')).length;
    const kid2Total = data.chores.chores.filter(c => c.assignedTo.includes('kid2')).length;

    // Update status displays
    const kid1Status = document.getElementById('kid1TaskStatus');
    const kid2Status = document.getElementById('kid2TaskStatus');
    const kid1SidebarStatus = document.getElementById('kid1Status');
    const kid2SidebarStatus = document.getElementById('kid2Status');

    if (kid1Status) {
        if (kid1Completed === kid1Total && kid1Total > 0) {
            kid1Status.textContent = 'All done! \u2728';
            kid1Status.classList.add('all-done');
        } else {
            kid1Status.textContent = `${kid1Completed}/${kid1Total} done`;
            kid1Status.classList.remove('all-done');
        }
    }

    if (kid2Status) {
        if (kid2Completed === kid2Total && kid2Total > 0) {
            kid2Status.textContent = 'All done! \u2728';
            kid2Status.classList.add('all-done');
        } else {
            kid2Status.textContent = `${kid2Completed}/${kid2Total} done`;
            kid2Status.classList.remove('all-done');
        }
    }

    // Update sidebar statuses too
    if (kid1SidebarStatus) {
        kid1SidebarStatus.textContent = kid1Completed === kid1Total && kid1Total > 0 ? 'All done! \u2728' : `${kid1Completed}/${kid1Total} tasks`;
    }
    if (kid2SidebarStatus) {
        kid2SidebarStatus.textContent = kid2Completed === kid2Total && kid2Total > 0 ? 'All done! \u2728' : `${kid2Completed}/${kid2Total} tasks`;
    }

    const completedToday = data.chores.completed.filter(c => c.person === selectedKid && c.date === today);
    const completedIds = completedToday.map(c => c.choreId);

    const chores = data.chores.chores.filter(c => c.assignedTo.includes(selectedKid));
    document.getElementById('choreGrid').innerHTML = chores.map(c => `
        <button class="chore-btn ${completedIds.includes(c.id) ? 'done' : ''}" onclick="toggleChore(${c.id})">
            <div class="icon">${c.icon}</div>
            <div class="name">${c.name}</div>
            <div class="chore-check">${completedIds.includes(c.id) ? '\u2713' : ''}</div>
        </button>
    `).join('');
}

// ==============================================
// Chore Toggle
// ==============================================
async function toggleChore(choreId) {
    const today = getLocalDateString();
    const isCompleted = data.chores.completed.some(c =>
        c.choreId === choreId && c.person === selectedKid && c.date === today
    );

    // Update data FIRST
    if (!isCompleted) {
        data.chores.completed.push({ choreId, person: selectedKid, date: today });
    } else {
        data.chores.completed = data.chores.completed.filter(c =>
            !(c.choreId === choreId && c.person === selectedKid && c.date === today)
        );
    }

    // Re-render immediately (this keeps button green/white based on data)
    renderKids();
    renderTodayChores();

    // Show celebration for completed tasks
    if (!isCompleted) {
        const kidName = selectedKid === 'kid1' ? 'Liv' : 'Jane';
        showCelebration(kidName);
    }

    // Send to server in background
    try {
        const endpoint = isCompleted ? '/api/chores/uncomplete' : '/api/chores/complete';
        await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ choreId, person: selectedKid })
        });
    } catch (err) {
        console.error('Error saving chore:', err);
    }
}

// ==============================================
// Today's Chores in Calendar Cell
// ==============================================
function renderTodayChores() {
    const today = getLocalDateString();
    const kid1Container = document.getElementById('kid1Chores');
    const kid2Container = document.getElementById('kid2Chores');
    if (!kid1Container || !kid2Container) return;

    const completedToday = data.chores.completed.filter(c => c.date === today);

    // Render Liv's chores
    const kid1Chores = data.chores.chores.filter(c => c.assignedTo.includes('kid1'));
    const kid1CompletedIds = completedToday.filter(c => c.person === 'kid1').map(c => c.choreId);
    kid1Container.innerHTML = kid1Chores.slice(0, 5).map(c => `
        <div class="chore-item ${kid1CompletedIds.includes(c.id) ? 'done' : ''}"
             onclick="event.stopPropagation(); toggleCalendarChore(${c.id}, 'kid1')">
            <div class="chore-checkbox">${kid1CompletedIds.includes(c.id) ? '\u2713' : ''}</div>
            <span>${c.icon} ${c.name.split(' ')[0]}</span>
        </div>
    `).join('');

    // Render Jane's chores
    const kid2Chores = data.chores.chores.filter(c => c.assignedTo.includes('kid2'));
    const kid2CompletedIds = completedToday.filter(c => c.person === 'kid2').map(c => c.choreId);
    kid2Container.innerHTML = kid2Chores.slice(0, 5).map(c => `
        <div class="chore-item ${kid2CompletedIds.includes(c.id) ? 'done' : ''}"
             onclick="event.stopPropagation(); toggleCalendarChore(${c.id}, 'kid2')">
            <div class="chore-checkbox">${kid2CompletedIds.includes(c.id) ? '\u2713' : ''}</div>
            <span>${c.icon} ${c.name.split(' ')[0]}</span>
        </div>
    `).join('');
}

// ==============================================
// Toggle Chore from Calendar View
// ==============================================
async function toggleCalendarChore(choreId, person) {
    const today = getLocalDateString();
    const isCompleted = data.chores.completed.some(c =>
        c.choreId === choreId && c.person === person && c.date === today
    );

    const endpoint = isCompleted ? '/api/chores/uncomplete' : '/api/chores/complete';
    const res = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ choreId, person })
    });

    const result = await res.json();
    if (result.success) {
        if (!isCompleted) {
            // Task completed
            data.chores.completed.push({ choreId, person, date: today });

            // Show celebration!
            const kidName = person === 'kid1' ? 'Liv' : 'Jane';
            showCelebration(kidName);
        } else {
            // Task uncompleted
            data.chores.completed = data.chores.completed.filter(c =>
                !(c.choreId === choreId && c.person === person && c.date === today)
            );
        }
        renderTodayChores();
        renderKids();
    }
}
