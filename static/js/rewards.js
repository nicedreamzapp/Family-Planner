/* ==============================================
   Rewards.js - Kids Star Rewards System
   Family Planner Application
   ============================================== */

// Currently selected kid for rewards modal (uses global selectedKid from app.js)

// ==============================================
// Initialize Rewards
// ==============================================
function initRewards() {
    updateRewardsDisplay();
}

// ==============================================
// Update Sidebar Display
// ==============================================
function updateRewardsDisplay() {
    const kid1Points = data.rewards?.kid1 || 0;
    const kid2Points = data.rewards?.kid2 || 0;

    // Update sidebar widget
    const kid1StarsEl = document.getElementById('kid1Stars');
    const kid2StarsEl = document.getElementById('kid2Stars');

    if (kid1StarsEl) kid1StarsEl.textContent = kid1Points;
    if (kid2StarsEl) kid2StarsEl.textContent = kid2Points;

    // Also update kids panel if it exists
    const kid1PointsEl = document.getElementById('kid1Points');
    const kid2PointsEl = document.getElementById('kid2Points');

    if (kid1PointsEl) kid1PointsEl.textContent = kid1Points + ' ⭐';
    if (kid2PointsEl) kid2PointsEl.textContent = kid2Points + ' ⭐';
}

// ==============================================
// Show Rewards Modal
// ==============================================
function showRewardsModal(kid) {
    selectedKid = kid;
    const points = data.rewards?.[kid] || 0;
    const name = kid === 'kid1' ? 'Liv' : 'Jane';

    document.getElementById('rewardsModalTitle').textContent = `⭐ ${name}'s Stars ⭐`;
    document.getElementById('rewardsAvatar').textContent = '👧';
    document.getElementById('rewardsPoints').textContent = points;

    // Update redeem buttons based on available points
    updateRedeemButtons(points);

    document.getElementById('rewardsModal').classList.add('show');
}

// ==============================================
// Update Redeem Button States
// ==============================================
function updateRedeemButtons(points) {
    document.querySelectorAll('.prize-item').forEach(item => {
        const cost = parseInt(item.dataset.cost);
        const btn = item.querySelector('.redeem-btn');
        if (btn) {
            btn.disabled = points < cost;
        }
    });
}

// ==============================================
// Add/Remove Points
// ==============================================
async function addPoints(amount) {
    if (!selectedKid) return;

    // Initialize rewards if not exists
    if (!data.rewards) data.rewards = { kid1: 0, kid2: 0 };

    // Update points (don't go below 0)
    data.rewards[selectedKid] = Math.max(0, (data.rewards[selectedKid] || 0) + amount);

    // Update modal display
    const newPoints = data.rewards[selectedKid];
    document.getElementById('rewardsPoints').textContent = newPoints;
    updateRedeemButtons(newPoints);

    // Update sidebar display
    updateRewardsDisplay();

    // Animate the points change
    const pointsEl = document.getElementById('rewardsPoints');
    pointsEl.style.transform = 'scale(1.3)';
    pointsEl.style.color = amount > 0 ? '#4CAF50' : '#e74c3c';
    setTimeout(() => {
        pointsEl.style.transform = 'scale(1)';
        pointsEl.style.color = '#B8860B';
    }, 300);

    // Save to server
    saveRewards();

    // Show celebration for adding points
    if (amount > 0) {
        showStarBurst();
    }
}

// ==============================================
// Redeem Prize
// ==============================================
async function redeemPrize(cost, prizeName) {
    if (!selectedKid) return;

    const currentPoints = data.rewards?.[selectedKid] || 0;
    if (currentPoints < cost) {
        alert(`Not enough stars! Need ${cost - currentPoints} more.`);
        return;
    }

    // Confirm redemption
    const name = selectedKid === 'kid1' ? 'Liv' : 'Jane';
    if (!confirm(`${name} wants to redeem "${prizeName}" for ${cost} stars?`)) {
        return;
    }

    // Deduct points
    data.rewards[selectedKid] -= cost;

    // Update displays
    const newPoints = data.rewards[selectedKid];
    document.getElementById('rewardsPoints').textContent = newPoints;
    updateRedeemButtons(newPoints);
    updateRewardsDisplay();

    // Save to server
    saveRewards();

    // Celebrate!
    showPrizeRedeemed(prizeName);
}

// ==============================================
// Save Rewards to Server
// ==============================================
async function saveRewards() {
    try {
        await fetch('/api/rewards/save', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data.rewards)
        });
    } catch (e) {
        console.error('Failed to save rewards:', e);
    }
}

// ==============================================
// Star Burst Animation
// ==============================================
function showStarBurst() {
    const stars = ['⭐', '🌟', '✨', '💫'];
    for (let i = 0; i < 8; i++) {
        const star = document.createElement('div');
        star.className = 'star-burst';
        star.textContent = stars[Math.floor(Math.random() * stars.length)];
        star.style.left = `${40 + Math.random() * 20}%`;
        star.style.top = `${30 + Math.random() * 20}%`;
        star.style.animationDelay = `${i * 0.05}s`;
        document.body.appendChild(star);
        setTimeout(() => star.remove(), 1000);
    }
}

// ==============================================
// Prize Redeemed Celebration
// ==============================================
function showPrizeRedeemed(prizeName) {
    const celebration = document.createElement('div');
    celebration.className = 'prize-celebration';
    celebration.innerHTML = `
        <div class="prize-text">🎉 Prize Redeemed! 🎉</div>
        <div class="prize-name">${prizeName}</div>
    `;
    document.body.appendChild(celebration);
    setTimeout(() => celebration.remove(), 2500);
}

// Add CSS for animations
const rewardsStyle = document.createElement('style');
rewardsStyle.textContent = `
    .star-burst {
        position: fixed;
        font-size: 30px;
        z-index: 9999;
        pointer-events: none;
        animation: burstOut 0.8s ease-out forwards;
    }

    @keyframes burstOut {
        0% {
            transform: scale(0) rotate(0deg);
            opacity: 1;
        }
        100% {
            transform: scale(2) rotate(360deg) translateY(-100px);
            opacity: 0;
        }
    }

    .prize-celebration {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(135deg, #9B59B6, #8E44AD);
        color: white;
        padding: 30px 50px;
        border-radius: 20px;
        text-align: center;
        z-index: 9999;
        box-shadow: 0 10px 40px rgba(155, 89, 182, 0.5);
        animation: celebratePop 2.5s ease-out forwards;
    }

    .prize-text {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .prize-name {
        font-size: 28px;
        font-weight: 800;
    }

    @keyframes celebratePop {
        0% {
            transform: translate(-50%, -50%) scale(0);
            opacity: 0;
        }
        15% {
            transform: translate(-50%, -50%) scale(1.2);
            opacity: 1;
        }
        25% {
            transform: translate(-50%, -50%) scale(1);
        }
        80% {
            transform: translate(-50%, -50%) scale(1);
            opacity: 1;
        }
        100% {
            transform: translate(-50%, -50%) scale(0.8);
            opacity: 0;
        }
    }
`;
document.head.appendChild(rewardsStyle);
