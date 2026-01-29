// Kids Fun Games Module
// Six interactive games for Liv and Jane

let currentGame = null;
let gameScore = 0;
let gameTimer = null;
let gameTimeLeft = 0;

// ==================
// GAME CONTROLLER
// ==================

// Open game from celebration modal (closes celebration first)
function openGameFromCelebration(gameType) {
    // Close celebration modal
    document.getElementById('celebrationModal').classList.remove('active');
    // Open the game
    openGame(gameType);
}

function openGame(gameType) {
    currentGame = gameType;
    gameScore = 0;
    document.getElementById('gameScore').textContent = '0';
    document.getElementById('gameTimer').textContent = '';
    document.getElementById('gamesModal').classList.add('active');

    const titles = {
        'memory': '🧠 Memory Match',
        'trivia': '🤔 Trivia Quiz',
        'math': '🔢 Math Challenge',
        'wordscramble': '🔎 Word Scramble',
        'colorMatch': '🎨 Color Match',
        'reaction': '⚡ Reaction Time'
    };

    document.getElementById('gameTitle').textContent = titles[gameType] || '🎮 Game';
    document.getElementById('gameStartBtn').style.display = 'block';
    document.getElementById('gameStartBtn').textContent = 'Start Game!';

    // Show instructions
    showGameInstructions(gameType);
}

function closeGame() {
    document.getElementById('gamesModal').classList.remove('active');
    if (gameTimer) {
        clearInterval(gameTimer);
        gameTimer = null;
    }
    currentGame = null;
}

function startCurrentGame() {
    document.getElementById('gameStartBtn').style.display = 'none';

    switch(currentGame) {
        case 'memory': startMemoryGame(); break;
        case 'trivia': startTriviaGame(); break;
        case 'math': startMathGame(); break;
        case 'wordscramble': startWordScramble(); break;
        case 'colorMatch': startColorMatch(); break;
        case 'reaction': startReactionGame(); break;
    }
}

function showGameInstructions(gameType) {
    const instructions = {
        'memory': `
            <div style="text-align:center; color:white; padding:20px;">
                <div style="font-size:60px; margin-bottom:20px;">🧠</div>
                <h3 style="margin-bottom:12px;">Memory Match</h3>
                <p style="color:rgba(255,255,255,0.7);">Flip cards and find matching pairs!<br>Match all pairs to win.</p>
            </div>`,
        'trivia': `
            <div style="text-align:center; color:white; padding:20px;">
                <div style="font-size:60px; margin-bottom:20px;">🤔</div>
                <h3 style="margin-bottom:12px;">Trivia Quiz</h3>
                <p style="color:rgba(255,255,255,0.7);">Answer fun questions!<br>Get as many right as you can.</p>
            </div>`,
        'math': `
            <div style="text-align:center; color:white; padding:20px;">
                <div style="font-size:60px; margin-bottom:20px;">🔢</div>
                <h3 style="margin-bottom:12px;">Math Challenge</h3>
                <p style="color:rgba(255,255,255,0.7);">Solve math problems fast!<br>30 seconds on the clock.</p>
            </div>`,
        'wordscramble': `
            <div style="text-align:center; color:white; padding:20px;">
                <div style="font-size:60px; margin-bottom:20px;">🔎</div>
                <h3 style="margin-bottom:12px;">Word Scramble</h3>
                <p style="color:rgba(255,255,255,0.7);">Unscramble the letters!<br>Figure out the hidden word.</p>
            </div>`,
        'colorMatch': `
            <div style="text-align:center; color:white; padding:20px;">
                <div style="font-size:60px; margin-bottom:20px;">🎨</div>
                <h3 style="margin-bottom:12px;">Color Match</h3>
                <p style="color:rgba(255,255,255,0.7);">Match the COLOR of the word, not the word itself!<br>It's trickier than you think.</p>
            </div>`,
        'reaction': `
            <div style="text-align:center; color:white; padding:20px;">
                <div style="font-size:60px; margin-bottom:20px;">⚡</div>
                <h3 style="margin-bottom:12px;">Reaction Time</h3>
                <p style="color:rgba(255,255,255,0.7);">Wait for green, then tap as fast as you can!<br>Test your reflexes.</p>
            </div>`
    };

    document.getElementById('gameArea').innerHTML = instructions[gameType] || '';
}

function updateScore(points) {
    gameScore += points;
    document.getElementById('gameScore').textContent = gameScore;
}

function showGameResult(title, message, emoji = '🎉') {
    document.getElementById('gameArea').innerHTML = `
        <div class="game-result">
            <div class="result-emoji">${emoji}</div>
            <h3>${title}</h3>
            <p>${message}</p>
            <button class="play-again-btn" onclick="startCurrentGame()">Play Again!</button>
        </div>
    `;
    document.getElementById('gameStartBtn').style.display = 'none';
}

// ==================
// MEMORY MATCH GAME
// ==================

let memoryCards = [];
let flippedCards = [];
let matchedPairs = 0;

function startMemoryGame() {
    const emojis = ['🐶', '🐱', '🐰', '🦊', '🐻', '🐼', '🐨', '🦁'];
    memoryCards = [...emojis, ...emojis].sort(() => Math.random() - 0.5);
    flippedCards = [];
    matchedPairs = 0;
    gameScore = 0;
    document.getElementById('gameScore').textContent = '0';

    let html = '<div class="memory-grid">';
    memoryCards.forEach((emoji, index) => {
        html += `<div class="memory-card" data-index="${index}" onclick="flipMemoryCard(${index})">❓</div>`;
    });
    html += '</div>';

    document.getElementById('gameArea').innerHTML = html;
}

function flipMemoryCard(index) {
    const cards = document.querySelectorAll('.memory-card');
    const card = cards[index];

    if (card.classList.contains('flipped') || card.classList.contains('matched') || flippedCards.length >= 2) {
        return;
    }

    card.classList.add('flipped');
    card.textContent = memoryCards[index];
    flippedCards.push({ index, emoji: memoryCards[index] });

    if (flippedCards.length === 2) {
        setTimeout(checkMemoryMatch, 600);
    }
}

function checkMemoryMatch() {
    const cards = document.querySelectorAll('.memory-card');
    const [first, second] = flippedCards;

    if (first.emoji === second.emoji) {
        cards[first.index].classList.add('matched');
        cards[second.index].classList.add('matched');
        matchedPairs++;
        updateScore(10);

        if (matchedPairs === 8) {
            setTimeout(() => {
                showGameResult('Amazing!', `You matched all pairs with ${gameScore} points!`, '🏆');
            }, 500);
        }
    } else {
        cards[first.index].classList.remove('flipped');
        cards[second.index].classList.remove('flipped');
        cards[first.index].textContent = '❓';
        cards[second.index].textContent = '❓';
    }

    flippedCards = [];
}

// ==================
// TRIVIA QUIZ GAME
// ==================

const triviaQuestions = [
    { q: "What planet is known as the Red Planet?", answers: ["Mars", "Venus", "Jupiter", "Saturn"], correct: 0 },
    { q: "How many legs does a spider have?", answers: ["6", "8", "10", "4"], correct: 1 },
    { q: "What is the largest ocean?", answers: ["Atlantic", "Indian", "Pacific", "Arctic"], correct: 2 },
    { q: "What color do you get mixing blue and yellow?", answers: ["Purple", "Orange", "Green", "Pink"], correct: 2 },
    { q: "How many days are in a week?", answers: ["5", "6", "7", "8"], correct: 2 },
    { q: "What animal says 'moo'?", answers: ["Pig", "Cow", "Sheep", "Horse"], correct: 1 },
    { q: "What is frozen water called?", answers: ["Steam", "Ice", "Snow", "Fog"], correct: 1 },
    { q: "How many colors are in a rainbow?", answers: ["5", "6", "7", "8"], correct: 2 },
    { q: "What do bees make?", answers: ["Milk", "Honey", "Sugar", "Jam"], correct: 1 },
    { q: "Which animal is the tallest?", answers: ["Elephant", "Giraffe", "Horse", "Bear"], correct: 1 },
];

let triviaIndex = 0;
let triviaAnswered = false;

function startTriviaGame() {
    triviaIndex = 0;
    gameScore = 0;
    document.getElementById('gameScore').textContent = '0';
    showTriviaQuestion();
}

function showTriviaQuestion() {
    if (triviaIndex >= 5) {
        const rating = gameScore >= 40 ? '🌟 Super Star!' : gameScore >= 20 ? '👍 Good Job!' : '💪 Keep Trying!';
        showGameResult(rating, `You scored ${gameScore} points!`, gameScore >= 40 ? '🏆' : '⭐');
        return;
    }

    triviaAnswered = false;
    const q = triviaQuestions[Math.floor(Math.random() * triviaQuestions.length)];

    let html = `
        <div class="trivia-question">
            <h3>${q.q}</h3>
        </div>
        <div class="trivia-answers">
    `;

    q.answers.forEach((answer, i) => {
        html += `<button class="trivia-btn" onclick="checkTriviaAnswer(${i}, ${q.correct}, this)">${answer}</button>`;
    });

    html += '</div>';
    document.getElementById('gameArea').innerHTML = html;
}

function checkTriviaAnswer(selected, correct, btn) {
    if (triviaAnswered) return;
    triviaAnswered = true;

    const buttons = document.querySelectorAll('.trivia-btn');
    buttons[correct].classList.add('correct');

    if (selected === correct) {
        updateScore(10);
    } else {
        btn.classList.add('wrong');
    }

    setTimeout(() => {
        triviaIndex++;
        showTriviaQuestion();
    }, 1000);
}

// ==================
// MATH CHALLENGE GAME
// ==================

let mathTimeLeft = 30;

function startMathGame() {
    gameScore = 0;
    mathTimeLeft = 30;
    document.getElementById('gameScore').textContent = '0';

    gameTimer = setInterval(() => {
        mathTimeLeft--;
        document.getElementById('gameTimer').textContent = `⏱️ ${mathTimeLeft}s`;

        if (mathTimeLeft <= 0) {
            clearInterval(gameTimer);
            gameTimer = null;
            const rating = gameScore >= 80 ? '🧮 Math Genius!' : gameScore >= 40 ? '📐 Great Work!' : '🔢 Good Try!';
            showGameResult(rating, `You scored ${gameScore} points in 30 seconds!`, '🏆');
        }
    }, 1000);

    showMathProblem();
}

function showMathProblem() {
    const ops = ['+', '-'];
    const op = ops[Math.floor(Math.random() * ops.length)];
    let num1, num2, answer;

    if (op === '+') {
        num1 = Math.floor(Math.random() * 20) + 1;
        num2 = Math.floor(Math.random() * 20) + 1;
        answer = num1 + num2;
    } else {
        num1 = Math.floor(Math.random() * 20) + 10;
        num2 = Math.floor(Math.random() * num1);
        answer = num1 - num2;
    }

    // Generate wrong answers
    const answers = [answer];
    while (answers.length < 4) {
        const wrong = answer + (Math.floor(Math.random() * 10) - 5);
        if (wrong !== answer && wrong >= 0 && !answers.includes(wrong)) {
            answers.push(wrong);
        }
    }
    answers.sort(() => Math.random() - 0.5);

    let html = `
        <div class="math-problem">
            <div class="equation">${num1} ${op} ${num2} = ?</div>
        </div>
        <div class="math-answers">
    `;

    answers.forEach(ans => {
        html += `<button class="math-btn" onclick="checkMathAnswer(${ans}, ${answer}, this)">${ans}</button>`;
    });

    html += '</div>';
    document.getElementById('gameArea').innerHTML = html;
}

function checkMathAnswer(selected, correct, btn) {
    if (selected === correct) {
        btn.classList.add('correct');
        updateScore(10);
    } else {
        btn.classList.add('wrong');
    }

    setTimeout(() => {
        if (mathTimeLeft > 0) {
            showMathProblem();
        }
    }, 300);
}

// ==================
// WORD SCRAMBLE GAME
// ==================

const scrambleWords = [
    { word: 'HAPPY', hint: 'Feeling of joy' },
    { word: 'BEACH', hint: 'Sandy place by the ocean' },
    { word: 'MUSIC', hint: 'Songs and melodies' },
    { word: 'PIZZA', hint: 'Yummy Italian food' },
    { word: 'DANCE', hint: 'Moving to music' },
    { word: 'SUNNY', hint: 'Bright weather' },
    { word: 'CANDY', hint: 'Sweet treat' },
    { word: 'PUPPY', hint: 'Baby dog' },
    { word: 'SLEEP', hint: 'Rest at night' },
    { word: 'SMILE', hint: 'Happy face expression' },
];

let scrambleIndex = 0;
let currentWord = '';

function startWordScramble() {
    scrambleIndex = 0;
    gameScore = 0;
    document.getElementById('gameScore').textContent = '0';
    showScrambleWord();
}

function showScrambleWord() {
    if (scrambleIndex >= 5) {
        const rating = gameScore >= 40 ? '📚 Word Wizard!' : gameScore >= 20 ? '✏️ Nice Work!' : '📖 Keep Reading!';
        showGameResult(rating, `You unscrambled ${gameScore / 10} words!`, '🎓');
        return;
    }

    const wordObj = scrambleWords[Math.floor(Math.random() * scrambleWords.length)];
    currentWord = wordObj.word;
    const scrambled = currentWord.split('').sort(() => Math.random() - 0.5).join('');

    document.getElementById('gameArea').innerHTML = `
        <div class="scramble-word">
            <div class="letters">${scrambled}</div>
            <div class="hint">Hint: ${wordObj.hint}</div>
        </div>
        <input type="text" class="scramble-input" id="scrambleInput" placeholder="Type the word..." maxlength="${currentWord.length}" onkeyup="checkScrambleInput(event)">
        <button class="btn-primary" style="width:100%;" onclick="submitScramble()">Submit</button>
    `;

    document.getElementById('scrambleInput').focus();
}

function checkScrambleInput(event) {
    if (event.key === 'Enter') {
        submitScramble();
    }
}

function submitScramble() {
    const input = document.getElementById('scrambleInput').value.toUpperCase();

    if (input === currentWord) {
        updateScore(10);
        scrambleIndex++;
        setTimeout(showScrambleWord, 500);
    } else {
        document.getElementById('scrambleInput').style.borderColor = '#ff6b6b';
        setTimeout(() => {
            document.getElementById('scrambleInput').style.borderColor = '#667eea';
        }, 500);
    }
}

// ==================
// COLOR MATCH GAME
// ==================

const colors = [
    { name: 'RED', color: '#e74c3c' },
    { name: 'BLUE', color: '#3498db' },
    { name: 'GREEN', color: '#2ecc71' },
    { name: 'YELLOW', color: '#f1c40f' },
];

let colorRound = 0;
let correctColor = '';

function startColorMatch() {
    colorRound = 0;
    gameScore = 0;
    document.getElementById('gameScore').textContent = '0';
    showColorRound();
}

function showColorRound() {
    if (colorRound >= 10) {
        const rating = gameScore >= 80 ? '🎨 Color Master!' : gameScore >= 50 ? '🌈 Great Eyes!' : '👀 Keep Trying!';
        showGameResult(rating, `You scored ${gameScore} points!`, '🎨');
        return;
    }

    // Pick random word and random display color
    const wordColor = colors[Math.floor(Math.random() * colors.length)];
    const displayColor = colors[Math.floor(Math.random() * colors.length)];
    correctColor = displayColor.name;

    let html = `
        <div class="color-display">
            <div class="color-word" style="background:${displayColor.color}; color:white;">${wordColor.name}</div>
            <div class="color-instruction">Tap the COLOR you see (not the word!)</div>
        </div>
        <div class="color-buttons">
    `;

    colors.forEach(c => {
        html += `<button class="color-btn" style="background:${c.color};" onclick="checkColorAnswer('${c.name}')">${c.name}</button>`;
    });

    html += '</div>';
    document.getElementById('gameArea').innerHTML = html;
}

function checkColorAnswer(selected) {
    if (selected === correctColor) {
        updateScore(10);
    }
    colorRound++;
    setTimeout(showColorRound, 300);
}

// ==================
// REACTION TIME GAME
// ==================

let reactionStart = 0;
let reactionTimeout = null;
let reactionState = 'waiting';
let reactionTimes = [];

function startReactionGame() {
    reactionTimes = [];
    gameScore = 0;
    document.getElementById('gameScore').textContent = '0';
    showReactionRound();
}

function showReactionRound() {
    if (reactionTimes.length >= 5) {
        const avgTime = Math.round(reactionTimes.reduce((a, b) => a + b, 0) / reactionTimes.length);
        const rating = avgTime < 300 ? '⚡ Lightning Fast!' : avgTime < 500 ? '🏃 Quick Reflexes!' : '🐢 Keep Practicing!';
        showGameResult(rating, `Average reaction time: ${avgTime}ms`, '⚡');
        return;
    }

    reactionState = 'waiting';
    document.getElementById('gameArea').innerHTML = `
        <div class="reaction-area">
            <div class="reaction-box waiting" onclick="handleReactionClick()">Wait for green...</div>
            <div class="reaction-message">Round ${reactionTimes.length + 1} of 5</div>
        </div>
    `;

    // Random delay between 1-4 seconds
    const delay = 1000 + Math.random() * 3000;
    reactionTimeout = setTimeout(() => {
        if (reactionState === 'waiting') {
            reactionState = 'ready';
            reactionStart = Date.now();
            const box = document.querySelector('.reaction-box');
            box.classList.remove('waiting');
            box.classList.add('ready');
            box.textContent = 'TAP NOW!';
        }
    }, delay);
}

function handleReactionClick() {
    if (reactionState === 'waiting') {
        // Clicked too early
        clearTimeout(reactionTimeout);
        document.getElementById('gameArea').innerHTML = `
            <div class="reaction-area">
                <div class="reaction-result" style="color:#ff6b6b;">Too Early!</div>
                <div class="reaction-message">Wait for green before tapping!</div>
                <button class="play-again-btn" onclick="showReactionRound()" style="margin-top:20px;">Try Again</button>
            </div>
        `;
    } else if (reactionState === 'ready') {
        const reactionTime = Date.now() - reactionStart;
        reactionTimes.push(reactionTime);
        reactionState = 'clicked';

        updateScore(Math.max(0, 100 - Math.floor(reactionTime / 10)));

        document.getElementById('gameArea').innerHTML = `
            <div class="reaction-area">
                <div class="reaction-result">${reactionTime}ms</div>
                <div class="reaction-message">${reactionTime < 250 ? '⚡ Amazing!' : reactionTime < 400 ? '👍 Good!' : '😊 Nice try!'}</div>
            </div>
        `;

        setTimeout(showReactionRound, 1500);
    }
}
