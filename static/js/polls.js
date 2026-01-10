/* ==============================================
   Polls.js - Family Voting System
   Family Planner Application
   ============================================== */

// Current voting person (cycles through family)
let currentVoter = 'kid1';
const voters = ['kid1', 'kid2', 'mom', 'dad'];
const voterNames = { kid1: 'Liv', kid2: 'Jane', mom: 'Mom', dad: 'Dad' };

// ==============================================
// Render Polls
// ==============================================
function renderPolls() {
    const pollsData = data.polls || { polls: [], votes: [] };
    const activePolls = pollsData.polls.filter(p => !p.closed);
    const closedPolls = pollsData.polls.filter(p => p.closed);

    // Render active polls
    const activeGrid = document.getElementById('pollsGrid');
    if (activeGrid) {
        if (activePolls.length === 0) {
            activeGrid.innerHTML = '<div class="empty-state"><div class="icon">🗳️</div>No active polls. Create one!</div>';
        } else {
            activeGrid.innerHTML = activePolls.map(poll => renderPollCard(poll, pollsData.votes)).join('');
        }
    }

    // Render closed polls
    const historyGrid = document.getElementById('pollsHistory');
    if (historyGrid) {
        if (closedPolls.length === 0) {
            historyGrid.innerHTML = '<div class="empty-state" style="padding:15px;"><div class="icon">📊</div>No closed polls yet</div>';
        } else {
            historyGrid.innerHTML = closedPolls.map(poll => renderPollCard(poll, pollsData.votes, true)).join('');
        }
    }
}

function renderPollCard(poll, allVotes, isClosed = false) {
    const pollVotes = allVotes.filter(v => v.pollId === poll.id);
    const totalVotes = pollVotes.length;
    const myVote = pollVotes.find(v => v.person === currentVoter);

    // Count votes per option
    const voteCounts = {};
    poll.options.forEach(opt => voteCounts[opt] = 0);
    pollVotes.forEach(v => {
        if (voteCounts[v.option] !== undefined) voteCounts[v.option]++;
    });

    const optionsHtml = poll.options.map(option => {
        const count = voteCounts[option] || 0;
        const percent = totalVotes > 0 ? Math.round((count / totalVotes) * 100) : 0;
        const isMyVote = myVote && myVote.option === option;
        const voters = pollVotes.filter(v => v.option === option).map(v => voterNames[v.person] || v.person);

        return `
            <div class="poll-option ${isMyVote ? 'my-vote' : ''} ${isClosed ? 'closed' : ''}"
                 onclick="${isClosed ? '' : `votePoll(${poll.id}, '${option.replace(/'/g, "\\'")}')`}">
                <div class="option-bar" style="width: ${percent}%"></div>
                <span class="option-text">${option}</span>
                <span class="option-count">${count} ${isMyVote ? '✓' : ''}</span>
                ${voters.length > 0 ? `<div class="option-voters">${voters.join(', ')}</div>` : ''}
            </div>
        `;
    }).join('');

    return `
        <div class="poll-card ${isClosed ? 'closed' : ''}">
            <div class="poll-question">${poll.question}</div>
            <div class="poll-meta">Created by ${voterNames[poll.createdBy] || poll.createdBy}</div>
            <div class="poll-options">${optionsHtml}</div>
            <div class="poll-footer">
                <span class="vote-count">${totalVotes} vote${totalVotes !== 1 ? 's' : ''}</span>
                <div class="poll-actions">
                    ${!isClosed ? `
                        <button class="poll-action-btn" onclick="closePoll(${poll.id})">Close</button>
                    ` : ''}
                    <button class="poll-action-btn delete" onclick="deletePoll(${poll.id})">Delete</button>
                </div>
            </div>
            <div class="voter-selector">
                Voting as:
                ${voters.map(v => `
                    <button class="voter-btn ${v === currentVoter ? 'active' : ''}" onclick="setVoter('${v}')">${voterNames[v]}</button>
                `).join('')}
            </div>
        </div>
    `;
}

// ==============================================
// Poll Actions
// ==============================================
function setVoter(person) {
    currentVoter = person;
    renderPolls();
}

function openCreatePollModal() {
    document.getElementById('pollQuestion').value = '';
    document.getElementById('pollOptionsInputs').innerHTML = `
        <input type="text" class="poll-option-input" placeholder="Option 1">
        <input type="text" class="poll-option-input" placeholder="Option 2">
    `;
    document.getElementById('createPollModal').classList.add('show');
}

function addPollOption() {
    const container = document.getElementById('pollOptionsInputs');
    const count = container.querySelectorAll('input').length + 1;
    const input = document.createElement('input');
    input.type = 'text';
    input.className = 'poll-option-input';
    input.placeholder = `Option ${count}`;
    container.appendChild(input);
}

async function createPoll() {
    const question = document.getElementById('pollQuestion').value.trim();
    const optionInputs = document.querySelectorAll('.poll-option-input');
    const options = Array.from(optionInputs).map(i => i.value.trim()).filter(v => v);

    if (!question || options.length < 2) {
        alert('Please enter a question and at least 2 options');
        return;
    }

    const response = await fetch('/api/polls/create', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question, options, person: currentVoter })
    });

    const result = await response.json();
    if (result.success) {
        data.polls.polls.push(result.poll);
        closeModal('createPollModal');
        renderPolls();
    }
}

async function votePoll(pollId, option) {
    const response = await fetch('/api/polls/vote', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pollId, option, person: currentVoter })
    });

    const result = await response.json();
    if (result.success) {
        // Update local data
        data.polls.votes = data.polls.votes.filter(v => !(v.pollId === pollId && v.person === currentVoter));
        data.polls.votes.push(result.vote);
        renderPolls();
    }
}

async function closePoll(pollId) {
    const response = await fetch('/api/polls/close', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: pollId })
    });

    const result = await response.json();
    if (result.success) {
        const poll = data.polls.polls.find(p => p.id === pollId);
        if (poll) poll.closed = true;
        renderPolls();
    }
}

async function deletePoll(pollId) {
    if (!confirm('Delete this poll?')) return;

    const response = await fetch('/api/polls/delete', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: pollId })
    });

    const result = await response.json();
    if (result.success) {
        data.polls.polls = data.polls.polls.filter(p => p.id !== pollId);
        data.polls.votes = data.polls.votes.filter(v => v.pollId !== pollId);
        renderPolls();
    }
}
