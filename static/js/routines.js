/* ==============================================
   Routines.js - Bedtime Routine System
   Family Planner Application
   ============================================== */

// Current selected kid for bedtime
let bedtimeKid = 'kid1';
const kidNames = { kid1: 'Liv', kid2: 'Jane' };

// ==============================================
// Render Bedtime Routine
// ==============================================
function renderBedtime() {
    const routinesData = data.routines || { routines: {}, progress: {} };
    const choresData = data.chores || { chores: [] };

    // Update kid selection UI
    document.getElementById('bedtimeKid1')?.classList.toggle('selected', bedtimeKid === 'kid1');
    document.getElementById('bedtimeKid2')?.classList.toggle('selected', bedtimeKid === 'kid2');

    // Get this kid's routine
    const routine = routinesData.routines[bedtimeKid] || { tasks: [], name: 'Bedtime' };
    const today = new Date().toISOString().split('T')[0];

    // Get/reset progress
    let progress = routinesData.progress[bedtimeKid] || { date: '', completed: [] };
    if (progress.date !== today) {
        progress = { date: today, completed: [] };
    }

    // Render steps
    const stepsContainer = document.getElementById('routineSteps');
    if (stepsContainer) {
        if (routine.tasks.length === 0) {
            stepsContainer.innerHTML = `
                <div class="empty-state">
                    <div class="icon">🌙</div>
                    <p>No bedtime tasks set up yet!</p>
                    <button onclick="openRoutineSetupModal()" class="setup-btn">Set Up Routine</button>
                </div>
            `;
        } else {
            stepsContainer.innerHTML = routine.tasks.map((taskId, index) => {
                const chore = choresData.chores.find(c => c.id === taskId);
                if (!chore) return '';

                const isDone = progress.completed.includes(taskId);
                return `
                    <div class="routine-step ${isDone ? 'done' : ''}" onclick="toggleRoutineTask(${taskId})">
                        <div class="step-number">${index + 1}</div>
                        <div class="step-icon">${chore.icon || '✨'}</div>
                        <div class="step-name">${chore.name}</div>
                        <div class="step-check">${isDone ? '✓' : ''}</div>
                    </div>
                `;
            }).join('');
        }
    }

    // Update progress bar
    const total = routine.tasks.length;
    const done = progress.completed.length;
    const percent = total > 0 ? Math.round((done / total) * 100) : 0;

    const progressFill = document.getElementById('bedtimeProgressFill');
    const progressText = document.getElementById('bedtimeProgressText');

    if (progressFill) progressFill.style.width = percent + '%';
    if (progressText) progressText.textContent = `${done} of ${total} done`;

    // Check if all done - celebrate!
    if (total > 0 && done === total) {
        progressFill?.classList.add('complete');
    } else {
        progressFill?.classList.remove('complete');
    }
}

function selectBedtimeKid(kid) {
    bedtimeKid = kid;
    renderBedtime();
}

// ==============================================
// Toggle Task Completion
// ==============================================
async function toggleRoutineTask(taskId) {
    const response = await fetch('/api/routines/complete', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ kid: bedtimeKid, taskId })
    });

    const result = await response.json();
    if (result.success) {
        // Update local data
        const today = new Date().toISOString().split('T')[0];
        data.routines.progress[bedtimeKid] = {
            date: today,
            completed: result.completed
        };

        renderBedtime();

        // Celebrate if all done!
        if (result.allDone) {
            celebrateBedtime();
        }
    }
}

function celebrateBedtime() {
    // Simple celebration - could integrate with celebrations.js
    const overlay = document.createElement('div');
    overlay.className = 'bedtime-celebration';
    overlay.innerHTML = `
        <div class="celebration-content">
            <div class="celebration-emoji">🌟</div>
            <h2>Great Job, ${kidNames[bedtimeKid]}!</h2>
            <p>All bedtime tasks complete!</p>
            <button onclick="this.parentElement.parentElement.remove()">Sweet Dreams! 😴</button>
        </div>
    `;
    document.body.appendChild(overlay);

    // Auto-remove after 5 seconds
    setTimeout(() => overlay.remove(), 5000);
}

// ==============================================
// Routine Setup Modal
// ==============================================
function openRoutineSetupModal() {
    const choresData = data.chores || { chores: [] };
    const routinesData = data.routines || { routines: {} };
    const currentRoutine = routinesData.routines[bedtimeKid] || { tasks: [] };

    // Update kid name in modal
    document.getElementById('routineSetupKidName').textContent = kidNames[bedtimeKid] + "'s";

    // Render task picker
    const picker = document.getElementById('routineTaskPicker');
    picker.innerHTML = choresData.chores.map(chore => {
        const isSelected = currentRoutine.tasks.includes(chore.id);
        return `
            <label class="task-picker-item ${isSelected ? 'selected' : ''}">
                <input type="checkbox" value="${chore.id}" ${isSelected ? 'checked' : ''} onchange="this.parentElement.classList.toggle('selected', this.checked)">
                <span class="task-icon">${chore.icon || '✨'}</span>
                <span class="task-name">${chore.name}</span>
            </label>
        `;
    }).join('');

    document.getElementById('routineSetupModal').classList.add('show');
}

async function saveRoutineSetup() {
    const checkboxes = document.querySelectorAll('#routineTaskPicker input:checked');
    const tasks = Array.from(checkboxes).map(cb => parseInt(cb.value));

    const response = await fetch('/api/routines/setup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            kid: bedtimeKid,
            tasks,
            name: kidNames[bedtimeKid] + "'s Bedtime"
        })
    });

    const result = await response.json();
    if (result.success) {
        data.routines.routines[bedtimeKid] = result.routine;
        closeModal('routineSetupModal');
        renderBedtime();
    }
}
