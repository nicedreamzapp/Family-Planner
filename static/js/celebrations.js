/* ==============================================
   Celebrations.js - FUN Interactive Games!
   Family Planner Application
   ============================================== */

// ==============================================
// SOUND EFFECTS using Web Audio API
// ==============================================
let audioCtx = null;

function getAudioContext() {
    if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    return audioCtx;
}

function playSound(type) {
    try {
        const ctx = getAudioContext();
        const oscillator = ctx.createOscillator();
        const gainNode = ctx.createGain();

        oscillator.connect(gainNode);
        gainNode.connect(ctx.destination);

        switch(type) {
            case 'pop':
                oscillator.frequency.setValueAtTime(600, ctx.currentTime);
                oscillator.frequency.exponentialRampToValueAtTime(200, ctx.currentTime + 0.1);
                gainNode.gain.setValueAtTime(0.3, ctx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.1);
                oscillator.start(ctx.currentTime);
                oscillator.stop(ctx.currentTime + 0.1);
                break;
            case 'spin':
                oscillator.frequency.setValueAtTime(300, ctx.currentTime);
                oscillator.frequency.exponentialRampToValueAtTime(800, ctx.currentTime + 0.15);
                gainNode.gain.setValueAtTime(0.2, ctx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.15);
                oscillator.start(ctx.currentTime);
                oscillator.stop(ctx.currentTime + 0.15);
                break;
            case 'win':
                // Play a happy jingle
                const notes = [523, 659, 784, 1047]; // C5, E5, G5, C6
                notes.forEach((freq, i) => {
                    const osc = ctx.createOscillator();
                    const gain = ctx.createGain();
                    osc.connect(gain);
                    gain.connect(ctx.destination);
                    osc.frequency.value = freq;
                    gain.gain.setValueAtTime(0.2, ctx.currentTime + i * 0.1);
                    gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + i * 0.1 + 0.2);
                    osc.start(ctx.currentTime + i * 0.1);
                    osc.stop(ctx.currentTime + i * 0.1 + 0.2);
                });
                break;
            case 'click':
                oscillator.frequency.setValueAtTime(800, ctx.currentTime);
                gainNode.gain.setValueAtTime(0.15, ctx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.05);
                oscillator.start(ctx.currentTime);
                oscillator.stop(ctx.currentTime + 0.05);
                break;
            case 'confetti':
                oscillator.type = 'triangle';
                oscillator.frequency.setValueAtTime(1200, ctx.currentTime);
                oscillator.frequency.exponentialRampToValueAtTime(400, ctx.currentTime + 0.15);
                gainNode.gain.setValueAtTime(0.15, ctx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.15);
                oscillator.start(ctx.currentTime);
                oscillator.stop(ctx.currentTime + 0.15);
                break;
            case 'celebrate':
                // Fanfare!
                const fanfare = [392, 523, 659, 784, 1047];
                fanfare.forEach((freq, i) => {
                    const osc = ctx.createOscillator();
                    const gain = ctx.createGain();
                    osc.connect(gain);
                    gain.connect(ctx.destination);
                    osc.type = 'square';
                    osc.frequency.value = freq;
                    gain.gain.setValueAtTime(0.15, ctx.currentTime + i * 0.08);
                    gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + i * 0.08 + 0.3);
                    osc.start(ctx.currentTime + i * 0.08);
                    osc.stop(ctx.currentTime + i * 0.08 + 0.3);
                });
                break;
        }
    } catch(e) {
        // Audio not supported, continue silently
    }
}

// ==============================================
// MAIN CELEBRATION - Called when task completed
// ==============================================
function showCelebration(kidName) {
    playSound('celebrate');
    // Create full-screen celebration overlay
    const overlay = document.createElement('div');
    overlay.id = 'celebrationOverlay';
    overlay.innerHTML = `
        <div class="celeb-container">
            <div class="celeb-header">
                <div class="celeb-stars">⭐ ✨ 🌟 ✨ ⭐</div>
                <h1 class="celeb-title">AMAZING JOB, ${kidName.toUpperCase()}!</h1>
                <div class="celeb-subtitle">Pick a celebration game!</div>
            </div>

            <div class="celeb-games">
                <button class="celeb-game-btn" onclick="playSlotMachine()">
                    <div class="game-icon">🎰</div>
                    <div class="game-name">Spin to Win!</div>
                </button>
                <button class="celeb-game-btn" onclick="playConfettiCannon()">
                    <div class="game-icon">🎊</div>
                    <div class="game-name">Confetti Blast!</div>
                </button>
                <button class="celeb-game-btn" onclick="playBubblePop()">
                    <div class="game-icon">🫧</div>
                    <div class="game-name">Pop Bubbles!</div>
                </button>
            </div>
            <div class="celeb-games" style="margin-top:10px;">
                <button class="celeb-game-btn" onclick="closeCelebration();openGame('memory')">
                    <div class="game-icon">🧠</div>
                    <div class="game-name">Memory</div>
                </button>
                <button class="celeb-game-btn" onclick="closeCelebration();openGame('trivia')">
                    <div class="game-icon">🤔</div>
                    <div class="game-name">Trivia</div>
                </button>
                <button class="celeb-game-btn" onclick="closeCelebration();openGame('math')">
                    <div class="game-icon">🔢</div>
                    <div class="game-name">Math</div>
                </button>
            </div>
            <div class="celeb-games" style="margin-top:10px;">
                <button class="celeb-game-btn" onclick="closeCelebration();openGame('wordscramble')">
                    <div class="game-icon">🔎</div>
                    <div class="game-name">Words</div>
                </button>
                <button class="celeb-game-btn" onclick="closeCelebration();openGame('colorMatch')">
                    <div class="game-icon">🎨</div>
                    <div class="game-name">Colors</div>
                </button>
                <button class="celeb-game-btn" onclick="closeCelebration();openGame('reaction')">
                    <div class="game-icon">⚡</div>
                    <div class="game-name">Reaction</div>
                </button>
            </div>

            <div class="celeb-play-area" id="celebPlayArea">
                <div class="play-prompt">👆 Tap a game to play! 👆</div>
            </div>

            <button class="celeb-close-btn" onclick="closeCelebration()">✓ All Done!</button>
        </div>
    `;
    document.body.appendChild(overlay);

    // Trigger confetti burst
    createConfettiBurst();

    // Add entrance animation
    requestAnimationFrame(() => {
        overlay.classList.add('show');
    });
}

function closeCelebration() {
    const overlay = document.getElementById('celebrationOverlay');
    if (overlay) {
        overlay.classList.remove('show');
        setTimeout(() => overlay.remove(), 300);
    }
    // Stop any ongoing games
    stopAllGames();
}

// ==============================================
// 🎰 SLOT MACHINE GAME
// ==============================================
const slotSymbols = ['🌟', '⭐', '✨', '💫', '🎉', '🦄', '🌈', '🎈', '🎊', '💖', '🔥', '🍀', '🎁', '🏆'];
const winMessages = ['SUPER STAR!', 'AMAZING!', 'WOW!', 'INCREDIBLE!', 'FANTASTIC!', 'AWESOME!', 'CHAMPION!', 'ROCKSTAR!'];
let slotInterval = null;

function playSlotMachine() {
    const area = document.getElementById('celebPlayArea');
    area.innerHTML = `
        <div class="slot-machine">
            <div class="slot-header">🎰 SPIN TO WIN! 🎰</div>
            <div class="slot-reels">
                <div class="slot-reel" id="reel1">🌟</div>
                <div class="slot-reel" id="reel2">⭐</div>
                <div class="slot-reel" id="reel3">✨</div>
            </div>
            <div class="slot-result" id="slotResult">Tap SPIN!</div>
            <button class="slot-spin-btn" onclick="spinTheSlots()">🎰 SPIN! 🎰</button>
        </div>
    `;
}

function spinTheSlots() {
    if (slotInterval) return; // Already spinning
    playSound('spin');

    const btn = document.querySelector('.slot-spin-btn');
    const result = document.getElementById('slotResult');
    btn.disabled = true;
    btn.textContent = '🎰 SPINNING... 🎰';
    result.textContent = '...';
    result.classList.remove('winner');

    const reel1 = document.getElementById('reel1');
    const reel2 = document.getElementById('reel2');
    const reel3 = document.getElementById('reel3');

    // Add spinning class
    reel1.classList.add('spinning');
    reel2.classList.add('spinning');
    reel3.classList.add('spinning');

    // Spin animation
    slotInterval = setInterval(() => {
        reel1.textContent = slotSymbols[Math.floor(Math.random() * slotSymbols.length)];
        reel2.textContent = slotSymbols[Math.floor(Math.random() * slotSymbols.length)];
        reel3.textContent = slotSymbols[Math.floor(Math.random() * slotSymbols.length)];
    }, 80);

    // Stop reel 1
    setTimeout(() => {
        reel1.classList.remove('spinning');
        reel1.classList.add('stopped');
    }, 800);

    // Stop reel 2
    setTimeout(() => {
        reel2.classList.remove('spinning');
        reel2.classList.add('stopped');
    }, 1300);

    // Stop reel 3 and show result
    setTimeout(() => {
        clearInterval(slotInterval);
        slotInterval = null;
        reel3.classList.remove('spinning');
        reel3.classList.add('stopped');

        // Always a winner!
        playSound('win');
        result.textContent = winMessages[Math.floor(Math.random() * winMessages.length)];
        result.classList.add('winner');

        btn.disabled = false;
        btn.textContent = '🎰 SPIN AGAIN! 🎰';

        createConfettiBurst();

        setTimeout(() => {
            reel1.classList.remove('stopped');
            reel2.classList.remove('stopped');
            reel3.classList.remove('stopped');
        }, 1500);
    }, 1800);
}

// ==============================================
// 🎊 CONFETTI CANNON GAME
// ==============================================
let confettiCount = 0;

function playConfettiCannon() {
    confettiCount = 0;
    const area = document.getElementById('celebPlayArea');
    area.innerHTML = `
        <div class="confetti-game">
            <div class="confetti-header">🎊 TAP ANYWHERE FOR CONFETTI! 🎊</div>
            <div class="confetti-area" id="confettiArea">
                <div class="tap-hint">👆 TAP ME! 👆</div>
            </div>
            <div class="confetti-score">Confetti Launched: <span id="confettiScore">0</span> 🎉</div>
        </div>
    `;

    document.getElementById('confettiArea').addEventListener('click', fireConfetti);
    document.getElementById('confettiArea').addEventListener('touchstart', fireConfetti);
}

function fireConfetti(e) {
    e.preventDefault();
    e.stopPropagation();
    playSound('confetti');

    const area = document.getElementById('confettiArea');
    const rect = area.getBoundingClientRect();
    const touch = e.touches ? e.touches[0] : e;
    const x = touch.clientX - rect.left;
    const y = touch.clientY - rect.top;

    const colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#F7DC6F', '#BB8FCE', '#85C1E9', '#FF69B4'];

    // Create explosion of confetti
    for (let i = 0; i < 25; i++) {
        const piece = document.createElement('div');
        piece.className = 'confetti-piece';
        piece.style.left = x + 'px';
        piece.style.top = y + 'px';
        piece.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        piece.style.setProperty('--angle', (Math.random() * 360) + 'deg');
        piece.style.setProperty('--distance', (60 + Math.random() * 120) + 'px');
        area.appendChild(piece);
        setTimeout(() => piece.remove(), 1000);
    }

    confettiCount++;
    document.getElementById('confettiScore').textContent = confettiCount;

    // Bounce effect
    area.style.transform = 'scale(0.98)';
    setTimeout(() => area.style.transform = 'scale(1)', 100);
}

// ==============================================
// 🫧 BUBBLE POP GAME - Easy Touch Version
// ==============================================
let bubbleScore = 0;
let bubbleTimer = null;
let bubbleSpawner = null;
let bubbleGameRunning = false;

function playBubblePop() {
    bubbleScore = 0;
    playSound('click');
    const area = document.getElementById('celebPlayArea');
    area.innerHTML = `
        <div class="bubble-game">
            <div class="bubble-header">
                <span>🫧 POP THE BUBBLES! 🫧</span>
                <div class="bubble-stats">
                    <span>Score: <span id="bubbleScore">0</span></span>
                    <span>Time: <span id="bubbleTime">15</span>s</span>
                </div>
            </div>
            <div class="bubble-area" id="bubbleArea"></div>
            <button class="bubble-start-btn" id="bubbleStartBtn" ontouchstart="startBubbleRound()" onclick="startBubbleRound()">🫧 START! 🫧</button>
        </div>
    `;
}

function startBubbleRound() {
    playSound('click');
    bubbleGameRunning = true;
    bubbleScore = 0;
    document.getElementById('bubbleScore').textContent = '0';
    document.getElementById('bubbleStartBtn').style.display = 'none';
    document.getElementById('bubbleArea').innerHTML = '';

    let timeLeft = 15;
    document.getElementById('bubbleTime').textContent = timeLeft;

    // Countdown timer
    bubbleTimer = setInterval(() => {
        timeLeft--;
        const timeEl = document.getElementById('bubbleTime');
        if (timeEl) timeEl.textContent = timeLeft;
        if (timeLeft <= 0) endBubbleRound();
    }, 1000);

    // Spawn bubbles faster
    bubbleSpawner = setInterval(() => {
        if (bubbleGameRunning) spawnBubble();
    }, 300);

    // Initial bubbles
    for (let i = 0; i < 6; i++) {
        setTimeout(() => spawnBubble(), i * 100);
    }
}

function spawnBubble() {
    const area = document.getElementById('bubbleArea');
    if (!area || !bubbleGameRunning) return;

    const bubble = document.createElement('div');
    bubble.className = 'bubble';

    // BIGGER bubbles for easier tapping
    const size = 55 + Math.random() * 30;
    bubble.style.width = size + 'px';
    bubble.style.height = size + 'px';
    bubble.style.left = (10 + Math.random() * (area.offsetWidth - size - 20)) + 'px';
    bubble.style.bottom = '-70px';

    // Colorful rainbow bubbles
    const hue = Math.random() * 360;
    bubble.style.background = `radial-gradient(circle at 30% 30%,
        rgba(255,255,255,0.9),
        hsla(${hue}, 80%, 65%, 0.7))`;
    bubble.style.border = `3px solid hsla(${hue}, 90%, 50%, 0.5)`;

    // Touch AND click handlers for reliability
    const popThis = (e) => {
        e.preventDefault();
        e.stopPropagation();
        if (bubble.dataset.popped) return;
        bubble.dataset.popped = 'true';
        popBubble(bubble);
    };

    bubble.addEventListener('touchstart', popThis, { passive: false });
    bubble.addEventListener('click', popThis);
    bubble.addEventListener('mousedown', popThis);

    area.appendChild(bubble);

    // Slower float for easier popping
    const duration = 3500 + Math.random() * 1500;
    bubble.style.animation = `floatUp ${duration}ms linear forwards`;

    setTimeout(() => {
        if (bubble.parentNode && !bubble.dataset.popped) bubble.remove();
    }, duration);
}

function popBubble(bubble) {
    if (!bubbleGameRunning || bubble.dataset.popped === 'done') return;
    bubble.dataset.popped = 'done';

    playSound('pop');
    bubbleScore++;
    const scoreEl = document.getElementById('bubbleScore');
    if (scoreEl) scoreEl.textContent = bubbleScore;

    // Fun pop effect
    bubble.innerHTML = '💥';
    bubble.style.fontSize = '30px';
    bubble.style.display = 'flex';
    bubble.style.alignItems = 'center';
    bubble.style.justifyContent = 'center';
    bubble.classList.add('popped');

    setTimeout(() => bubble.remove(), 150);
}

function endBubbleRound() {
    bubbleGameRunning = false;
    clearInterval(bubbleTimer);
    clearInterval(bubbleSpawner);
    bubbleTimer = null;
    bubbleSpawner = null;

    playSound('win');
    const area = document.getElementById('bubbleArea');
    if (area) {
        area.innerHTML = `
            <div class="bubble-result">
                <div class="bubble-final">🎉 ${bubbleScore} Bubbles! 🎉</div>
                <div class="bubble-msg">${bubbleScore >= 20 ? 'INCREDIBLE!' : bubbleScore >= 12 ? 'AMAZING!' : bubbleScore >= 6 ? 'GREAT JOB!' : 'NICE TRY!'}</div>
            </div>
        `;
    }

    const btn = document.getElementById('bubbleStartBtn');
    if (btn) {
        btn.style.display = 'block';
        btn.textContent = '🫧 PLAY AGAIN! 🫧';
    }

    createConfettiBurst();
}

function stopAllGames() {
    bubbleGameRunning = false;
    if (bubbleTimer) clearInterval(bubbleTimer);
    if (bubbleSpawner) clearInterval(bubbleSpawner);
    if (slotInterval) clearInterval(slotInterval);
}

// ==============================================
// CONFETTI BURST (Background effect)
// ==============================================
function createConfettiBurst() {
    const colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#F7DC6F', '#BB8FCE', '#85C1E9', '#FF69B4', '#FFD700'];

    for (let i = 0; i < 60; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'bg-confetti';
        confetti.style.left = (Math.random() * 100) + 'vw';
        confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.animationDelay = (Math.random() * 0.5) + 's';
        confetti.style.animationDuration = (2 + Math.random() * 2) + 's';
        document.body.appendChild(confetti);
        setTimeout(() => confetti.remove(), 4000);
    }
}

// ==============================================
// INJECT CELEBRATION STYLES
// ==============================================
const celebStyles = document.createElement('style');
celebStyles.textContent = `
/* Celebration Overlay */
#celebrationOverlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    z-index: 99999;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.3s;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
}

#celebrationOverlay.show {
    opacity: 1;
}

.celeb-container {
    width: 95%;
    max-width: 550px;
    text-align: center;
    padding: 15px 10px;
    margin: auto 0;
}

.celeb-header {
    margin-bottom: 12px;
}

.celeb-stars {
    font-size: clamp(24px, 4vw, 32px);
    margin-bottom: 8px;
    animation: starPulse 1s ease-in-out infinite;
}

@keyframes starPulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
}

.celeb-title {
    font-size: clamp(22px, 5vw, 40px);
    font-weight: 800;
    color: #FFD700;
    text-shadow: 0 4px 20px rgba(0,0,0,0.3);
    margin: 0 0 6px 0;
}

.celeb-subtitle {
    font-size: clamp(14px, 2.5vw, 18px);
    color: rgba(255,255,255,0.9);
}

/* Game Selection Buttons */
.celeb-games {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-bottom: 12px;
}

.celeb-game-btn {
    width: clamp(70px, 12vw, 90px);
    height: clamp(70px, 12vw, 90px);
    border-radius: 16px;
    border: 3px solid rgba(255,255,255,0.4);
    background: rgba(255,255,255,0.15);
    cursor: pointer;
    transition: all 0.2s;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 4px;
}

.celeb-game-btn:hover, .celeb-game-btn:active {
    transform: scale(1.1);
    background: rgba(255,255,255,0.25);
    border-color: #FFD700;
    box-shadow: 0 0 30px rgba(255,215,0,0.5);
}

.game-icon {
    font-size: clamp(28px, 5vw, 38px);
}

.game-name {
    font-size: clamp(9px, 1.5vw, 11px);
    color: white;
    font-weight: 600;
}

/* Play Area */
.celeb-play-area {
    background: rgba(0,0,0,0.2);
    border-radius: 16px;
    min-height: clamp(180px, 30vh, 260px);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 12px;
    overflow: hidden;
}

.play-prompt {
    font-size: clamp(16px, 3vw, 22px);
    color: rgba(255,255,255,0.6);
}

/* Close Button */
.celeb-close-btn {
    padding: 12px 40px;
    font-size: clamp(16px, 2.5vw, 20px);
    font-weight: 700;
    background: rgba(255,255,255,0.2);
    border: 2px solid rgba(255,255,255,0.5);
    border-radius: 50px;
    color: white;
    cursor: pointer;
    transition: all 0.2s;
}

.celeb-close-btn:hover {
    background: rgba(255,255,255,0.3);
    transform: scale(1.05);
}

/* SLOT MACHINE */
.slot-machine {
    text-align: center;
    padding: 20px;
}

.slot-header {
    font-size: 24px;
    color: white;
    margin-bottom: 20px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.3);
}

.slot-reels {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-bottom: 20px;
}

.slot-reel {
    width: 80px;
    height: 100px;
    background: white;
    border-radius: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 50px;
    box-shadow: inset 0 5px 15px rgba(0,0,0,0.2), 0 8px 25px rgba(0,0,0,0.3);
}

.slot-reel.spinning {
    animation: reelShake 0.1s linear infinite;
}

.slot-reel.stopped {
    animation: reelBounce 0.3s ease-out;
}

@keyframes reelShake {
    0%, 100% { transform: translateY(-2px); }
    50% { transform: translateY(2px); }
}

@keyframes reelBounce {
    0% { transform: scale(1.15); }
    50% { transform: scale(0.95); }
    100% { transform: scale(1); }
}

.slot-result {
    font-size: 28px;
    color: white;
    margin-bottom: 20px;
    min-height: 40px;
}

.slot-result.winner {
    color: #FFD700;
    text-shadow: 0 0 20px #FFD700;
    animation: winPulse 0.4s ease-in-out 3;
}

@keyframes winPulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.2); }
}

.slot-spin-btn {
    padding: 15px 40px;
    font-size: 22px;
    font-weight: 800;
    background: linear-gradient(135deg, #FFD700, #FFA500);
    border: none;
    border-radius: 50px;
    color: #333;
    cursor: pointer;
    box-shadow: 0 6px 20px rgba(255,165,0,0.5);
    transition: all 0.2s;
}

.slot-spin-btn:hover:not(:disabled) {
    transform: scale(1.05);
}

.slot-spin-btn:disabled {
    opacity: 0.7;
}

/* CONFETTI CANNON */
.confetti-game {
    text-align: center;
    padding: 10px;
}

.confetti-header {
    font-size: 20px;
    color: white;
    margin-bottom: 15px;
}

.confetti-area {
    width: 100%;
    height: 220px;
    background: rgba(255,255,255,0.1);
    border-radius: 20px;
    position: relative;
    overflow: hidden;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: transform 0.1s;
}

.tap-hint {
    font-size: 28px;
    color: rgba(255,255,255,0.4);
    pointer-events: none;
}

.confetti-piece {
    position: absolute;
    width: 10px;
    height: 10px;
    border-radius: 2px;
    animation: confettiExplode 1s ease-out forwards;
    pointer-events: none;
}

@keyframes confettiExplode {
    0% { transform: translate(0,0) rotate(0) scale(1); opacity: 1; }
    100% {
        transform: translate(
            calc(cos(var(--angle)) * var(--distance)),
            calc(sin(var(--angle)) * var(--distance) - 80px)
        ) rotate(720deg) scale(0);
        opacity: 0;
    }
}

.confetti-score {
    margin-top: 15px;
    font-size: 18px;
    color: white;
}

/* BUBBLE POP */
.bubble-game {
    text-align: center;
    padding: 10px;
}

.bubble-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: white;
    font-size: 18px;
    margin-bottom: 10px;
    padding: 0 10px;
}

.bubble-stats {
    display: flex;
    gap: 20px;
    font-weight: 600;
}

.bubble-area {
    width: 100%;
    height: 220px;
    background: rgba(255,255,255,0.1);
    border-radius: 20px;
    position: relative;
    overflow: hidden;
}

.bubble {
    position: absolute;
    border-radius: 50%;
    cursor: pointer;
    box-shadow:
        inset -8px -8px 20px rgba(255,255,255,0.6),
        inset 8px 8px 20px rgba(0,0,0,0.1),
        0 4px 15px rgba(0,0,0,0.2);
    touch-action: manipulation;
    -webkit-tap-highlight-color: transparent;
    user-select: none;
    z-index: 10;
}

.bubble:active {
    transform: scale(0.9);
}

.bubble.popped {
    animation: bubblePop 0.15s ease-out forwards;
    pointer-events: none;
}

@keyframes bubblePop {
    0% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.3); }
    100% { transform: scale(0); opacity: 0; }
}

@keyframes floatUp {
    0% { bottom: -70px; opacity: 0; }
    5% { opacity: 1; }
    95% { opacity: 1; }
    100% { bottom: 105%; opacity: 0; }
}

.bubble-start-btn {
    margin-top: 15px;
    padding: 12px 35px;
    font-size: 18px;
    font-weight: 700;
    background: linear-gradient(135deg, #4ECDC4, #45B7D1);
    border: none;
    border-radius: 30px;
    color: white;
    cursor: pointer;
    box-shadow: 0 5px 20px rgba(78,205,196,0.5);
}

.bubble-result {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
}

.bubble-final {
    font-size: 32px;
    color: white;
}

.bubble-msg {
    font-size: 24px;
    color: #FFD700;
    font-weight: 700;
}

/* Background Confetti */
.bg-confetti {
    position: fixed;
    top: -20px;
    width: 12px;
    height: 12px;
    border-radius: 2px;
    z-index: 999999;
    pointer-events: none;
    animation: confettiFall linear forwards;
}

@keyframes confettiFall {
    0% { transform: translateY(0) rotate(0); opacity: 1; }
    100% { transform: translateY(100vh) rotate(720deg); opacity: 0; }
}
`;
document.head.appendChild(celebStyles);
