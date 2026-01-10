/* ==============================================
   Themes.js - Earthy Seasonal Themes
   Family Planner - Humboldt Redwood Coast Edition
   ============================================== */

// ==============================================
// Monthly Theme Configuration - Earthy & Womanly
// Inspired by Humboldt County, Redwood Coast, Pacific NW
// ==============================================
const MONTH_THEMES = {
    0: { // January - Wolf Moon, New Beginnings
        name: 'january',
        emoji: ['🐺', '🌕', '✨'],
        cornerEmojis: ['🎇', '🥂', '🎊'],
        colors: { primary: '#5C6BC0', accent: '#7E57C2', bg: '#E8EAF6' },
        particles: ['✨', '⭐', '🌟', '💫'],
        description: 'Wolf Moon & New Beginnings'
    },
    1: { // February - Imbolc, Snow Moon, Brigid
        name: 'february',
        emoji: ['🕯️', '🌸', '💜'],
        cornerEmojis: ['🕯️', '💕', '🌷'],
        colors: { primary: '#E91E63', accent: '#9C27B0', bg: '#FCE4EC' },
        particles: ['💗', '🌸', '✨', '💜'],
        description: 'Imbolc & Goddess Brigid'
    },
    2: { // March - Spring Equinox, Ostara, Rebirth
        name: 'march',
        emoji: ['🌸', '🐣', '🦋'],
        cornerEmojis: ['🌸', '🐰', '🦋'],
        colors: { primary: '#4CAF50', accent: '#8BC34A', bg: '#E8F5E9' },
        particles: ['🌸', '🌿', '🌱', '🦋'],
        description: 'Spring Equinox & Ostara'
    },
    3: { // April - Earth Day, Pink Moon, Growth
        name: 'april',
        emoji: ['🌍', '🌷', '🌧️'],
        cornerEmojis: ['🌍', '🌧️', '🌈'],
        colors: { primary: '#43A047', accent: '#66BB6A', bg: '#E8F5E9' },
        particles: ['🌧️', '🌿', '🌱', '💧'],
        description: 'Earth Day & Spring Showers'
    },
    4: { // May - Beltane, Flower Moon, Fertility
        name: 'may',
        emoji: ['🔥', '🌺', '🧚'],
        cornerEmojis: ['🌺', '🔥', '🧚'],
        colors: { primary: '#E91E63', accent: '#FF5722', bg: '#FFF3E0' },
        particles: ['🌺', '🌸', '🌷', '🌻'],
        description: 'Beltane & Flower Moon'
    },
    5: { // June - Summer Solstice, Litha, Ocean
        name: 'june',
        emoji: ['☀️', '🌊', '🐚'],
        cornerEmojis: ['☀️', '🌊', '🐚'],
        colors: { primary: '#00BCD4', accent: '#FFB300', bg: '#E0F7FA' },
        particles: ['☀️', '🌊', '✨', '🐚'],
        description: 'Summer Solstice & Litha'
    },
    6: { // July - Self-Care, Buck Moon, Warmth
        name: 'july',
        emoji: ['💆', '🌻', '🦌'],
        cornerEmojis: ['🦌', '🌻', '💆'],
        colors: { primary: '#FF9800', accent: '#F57C00', bg: '#FFF8E1' },
        particles: ['🌻', '☀️', '✨', '🦋'],
        description: 'Self-Care & Buck Moon'
    },
    7: { // August - Lughnasadh, First Harvest, Lions Gate
        name: 'august',
        emoji: ['🌾', '🦁', '🌕'],
        cornerEmojis: ['🌾', '🦁', '🍞'],
        colors: { primary: '#FF6F00', accent: '#E65100', bg: '#FFF3E0' },
        particles: ['🌾', '✨', '⭐', '🍂'],
        description: 'Lughnasadh & First Harvest'
    },
    8: { // September - Mabon, Harvest Moon, Abundance
        name: 'september',
        emoji: ['🍂', '🎃', '🍁'],
        cornerEmojis: ['🍂', '🌕', '🍎'],
        colors: { primary: '#FF5722', accent: '#BF360C', bg: '#FBE9E7' },
        particles: ['🍂', '🍁', '🌾', '🍎'],
        description: 'Mabon & Autumn Equinox'
    },
    9: { // October - Samhain, Halloween, Ancestors
        name: 'october',
        emoji: ['🎃', '🌙', '🦇'],
        cornerEmojis: ['🎃', '👻', '🦇'],
        colors: { primary: '#FF6F00', accent: '#6A1B9A', bg: '#FFF3E0' },
        particles: ['🍂', '🎃', '🦇', '🕷️'],
        description: 'Samhain & Veil Thinning'
    },
    10: { // November - Ancestors, Cailleach, Gratitude
        name: 'november',
        emoji: ['👑', '🍂', '🦃'],
        cornerEmojis: ['👑', '🦃', '🍁'],
        colors: { primary: '#795548', accent: '#5D4037', bg: '#EFEBE9' },
        particles: ['🍂', '🍁', '✨', '🦉'],
        description: 'Cailleach & Gratitude'
    },
    11: { // December - Yule, Winter Solstice, Return of Light
        name: 'december',
        emoji: ['❄️', '🎄', '🕯️'],
        cornerEmojis: ['🎄', '🎅', '❄️'],
        colors: { primary: '#C62828', accent: '#2E7D32', bg: '#FFEBEE' },
        particles: ['❄️', '✨', '⭐', '🌟'],
        description: 'Yule & Winter Solstice'
    }
};

// ==============================================
// Seasonal Theme Application
// ==============================================
function applySeasonalTheme(viewingMonth) {
    // Use the month being viewed, or default to current month
    const month = (viewingMonth !== undefined) ? viewingMonth : new Date().getMonth();
    const body = document.body;
    const theme = MONTH_THEMES[month];

    // Remove all existing theme classes
    Object.values(MONTH_THEMES).forEach(t => {
        body.classList.remove(t.name + '-theme');
    });

    // Remove any existing decorations and video
    document.querySelectorAll('.december-decorations, .new-year-sparkles, .seasonal-particles').forEach(el => el.remove());
    const existingDecemberVideo = document.querySelector('.december-bg-video');
    if (existingDecemberVideo) existingDecemberVideo.remove();
    const existingJanuaryVideo = document.querySelector('.january-bg-video');
    if (existingJanuaryVideo) existingJanuaryVideo.remove();

    // Apply theme class
    body.classList.add(theme.name + '-theme');

    // Add decorations based on month
    addMonthDecorations(theme);

    // Add particles for all months
    if (theme.particles) {
        createSeasonalParticles(theme.particles);
    }

    // Special handling for months with background videos
    if (month === 11) {
        createDecemberBackgroundVideo();
    } else if (month === 0) {
        createJanuaryBackgroundVideo();
    }

    console.log(`[Theme] Applied ${theme.name} theme: ${theme.description}`);
}

// ==============================================
// Monthly Decorations (corner emojis)
// ==============================================
function addMonthDecorations(theme) {
    // Bottom right
    if (!document.querySelector('.decoration-tree')) {
        const bottomRight = document.createElement('div');
        bottomRight.className = 'december-decorations decoration-tree';
        bottomRight.textContent = theme.cornerEmojis[0];
        document.body.appendChild(bottomRight);
    }

    // Top left
    if (!document.querySelector('.decoration-top-left')) {
        const topLeft = document.createElement('div');
        topLeft.className = 'december-decorations decoration-top-left';
        topLeft.innerHTML = theme.cornerEmojis[1];
        document.body.appendChild(topLeft);
    }

    // Top right
    if (!document.querySelector('.decoration-top-right')) {
        const topRight = document.createElement('div');
        topRight.className = 'december-decorations decoration-top-right';
        topRight.textContent = theme.cornerEmojis[2];
        document.body.appendChild(topRight);
    }
}

// ==============================================
// Seasonal Particles Animation
// ==============================================
function createSeasonalParticles(particleEmojis) {
    let container = document.querySelector('.seasonal-particles');
    if (!container) {
        container = document.createElement('div');
        container.className = 'seasonal-particles new-year-sparkles';
        document.body.appendChild(container);
    }

    for (let i = 0; i < 20; i++) {
        const particle = document.createElement('div');
        particle.className = 'sparkle';
        particle.textContent = particleEmojis[Math.floor(Math.random() * particleEmojis.length)];
        particle.style.left = Math.random() * 100 + '%';
        particle.style.fontSize = (Math.random() * 12 + 10) + 'px';
        particle.style.opacity = Math.random() * 0.5 + 0.2;
        particle.style.animationDuration = (Math.random() * 10 + 8) + 's';
        particle.style.animationDelay = (Math.random() * 10) + 's';
        container.appendChild(particle);
    }
}

// ==============================================
// December Background Video
// ==============================================
function createDecemberBackgroundVideo() {
    console.log('[Theme] Creating December background video...');

    // Remove any existing snow
    const existingSnow = document.querySelector('.snowfall');
    if (existingSnow) {
        existingSnow.remove();
        console.log('[Theme] Removed existing snowfall');
    }

    // Check if video already exists
    if (document.querySelector('.december-bg-video')) {
        console.log('[Theme] Video already exists');
        return;
    }

    const video = document.createElement('video');
    video.className = 'december-bg-video';
    video.autoplay = true;
    video.loop = true;
    video.muted = true;
    video.playsInline = true;
    video.setAttribute('playsinline', ''); // iOS compatibility
    video.setAttribute('webkit-playsinline', ''); // Older iOS

    video.src = '/static/december-bg.mp4';
    console.log('[Theme] Video source set to /static/december-bg.mp4');

    // Ensure slow motion is applied after video loads
    video.addEventListener('loadeddata', () => {
        video.playbackRate = 0.3;
        console.log('[Theme] Video loaded, playback rate set to 0.3');
    });

    video.addEventListener('play', () => {
        video.playbackRate = 0.3;
    });

    video.addEventListener('error', (e) => {
        console.error('[Theme] Video error:', video.error);
    });

    // Insert as first child of body so it's behind everything
    document.body.insertBefore(video, document.body.firstChild);
    console.log('[Theme] Video element inserted into DOM');

    // Start playing
    video.play().then(() => {
        video.playbackRate = 0.3;
        console.log('[Theme] Video playing at 0.3x speed');
    }).catch(e => {
        console.log('[Theme] Background video autoplay blocked:', e);
        // Try playing on first user interaction
        document.addEventListener('click', () => {
            video.play();
            video.playbackRate = 0.3;
        }, { once: true });
    });
}

// ==============================================
// Monthly Video Preview (ScrSvr button)
// ==============================================
const MONTHLY_VIDEOS = {
    0: '/static/january-bg.mp4',   // January
    11: '/static/december-bg.mp4'  // December
};

function showMonthlyPreview() {
    const preview = document.getElementById('monthlyPreview');
    const video = document.getElementById('monthlyPreviewVideo');

    // Get the currently viewed month from the calendar
    const month = (typeof expandedMonth !== 'undefined') ? expandedMonth : new Date().getMonth();

    // Check if this month has a video
    const videoSrc = MONTHLY_VIDEOS[month];

    if (!videoSrc) {
        console.log('[Theme] No preview video for month:', month);
        // Fall back to ocean screensaver if no monthly video
        if (typeof startScreensaver === 'function') {
            startScreensaver();
        }
        return;
    }

    console.log('[Theme] Showing monthly preview for month:', month, 'video:', videoSrc);

    video.src = videoSrc;
    video.playbackRate = 0.25; // Slow to 25% speed
    preview.classList.add('active');

    video.addEventListener('loadeddata', () => {
        video.playbackRate = 0.25;
    }, { once: true });

    video.play().then(() => {
        video.playbackRate = 0.25;
        console.log('[Theme] Monthly preview playing at 0.25x speed');
    }).catch(e => {
        console.log('[Theme] Monthly preview autoplay blocked:', e);
    });
}

function closeMonthlyPreview() {
    const preview = document.getElementById('monthlyPreview');
    const video = document.getElementById('monthlyPreviewVideo');

    preview.classList.remove('active');
    video.pause();
    video.src = '';

    console.log('[Theme] Monthly preview closed');
}

// Close preview on click anywhere (except close button)
document.addEventListener('DOMContentLoaded', function() {
    const preview = document.getElementById('monthlyPreview');
    if (preview) {
        preview.addEventListener('click', function(e) {
            if (e.target === preview || e.target.tagName === 'VIDEO') {
                closeMonthlyPreview();
            }
        });
    }
});

// ==============================================
// January Background Video
// ==============================================
function createJanuaryBackgroundVideo() {
    console.log('[Theme] Creating January background video...');

    // Check if video already exists
    if (document.querySelector('.january-bg-video')) {
        console.log('[Theme] January video already exists');
        return;
    }

    const video = document.createElement('video');
    video.className = 'january-bg-video';
    video.autoplay = true;
    video.loop = true;
    video.muted = true;
    video.playsInline = true;
    video.setAttribute('playsinline', '');
    video.setAttribute('webkit-playsinline', '');

    video.src = '/static/january-bg.mp4';
    console.log('[Theme] Video source set to /static/january-bg.mp4');

    // Slow down to 1/3 speed (0.33x)
    video.addEventListener('loadeddata', () => {
        video.playbackRate = 0.33;
        console.log('[Theme] January video loaded, playback rate set to 0.33');
    });

    video.addEventListener('play', () => {
        video.playbackRate = 0.33;
    });

    video.addEventListener('error', (e) => {
        console.error('[Theme] January video error:', video.error);
    });

    // Insert as first child of body so it's behind everything
    document.body.insertBefore(video, document.body.firstChild);
    console.log('[Theme] January video element inserted into DOM');

    // Start playing at 1/3 speed
    video.play().then(() => {
        video.playbackRate = 0.33;
        console.log('[Theme] January video playing at 0.33x speed');
    }).catch(e => {
        console.log('[Theme] January background video autoplay blocked:', e);
        document.addEventListener('click', () => {
            video.play();
            video.playbackRate = 0.33;
        }, { once: true });
    });
}

// ==============================================
// December Theme - Snowfall
// ==============================================
function createSnowfall() {
    let snowfall = document.querySelector('.snowfall');
    if (!snowfall) {
        snowfall = document.createElement('div');
        snowfall.className = 'snowfall';
        document.body.appendChild(snowfall);
    }

    const snowflakes = ['\u2744', '\u2745', '\u2746', '\u273B', '\u273C', '\u274B'];
    for (let i = 0; i < 50; i++) {
        const flake = document.createElement('div');
        flake.className = 'snowflake';
        flake.textContent = snowflakes[Math.floor(Math.random() * snowflakes.length)];
        flake.style.left = Math.random() * 100 + '%';
        flake.style.fontSize = (Math.random() * 10 + 8) + 'px';
        flake.style.opacity = Math.random() * 0.6 + 0.4;
        flake.style.animationDuration = (Math.random() * 10 + 10) + 's';
        flake.style.animationDelay = (Math.random() * 10) + 's';
        snowfall.appendChild(flake);
    }
}

// ==============================================
// December - Christmas Decorations
// ==============================================
function addChristmasDecorations() {
    // Add Christmas tree to bottom right
    if (!document.querySelector('.decoration-tree')) {
        const tree = document.createElement('div');
        tree.className = 'december-decorations decoration-tree';
        tree.textContent = '🎄';
        document.body.appendChild(tree);
    }

    // Add Santa to top left
    if (!document.querySelector('.decoration-top-left')) {
        const santa = document.createElement('div');
        santa.className = 'december-decorations decoration-top-left';
        santa.innerHTML = '🎅';
        document.body.appendChild(santa);
    }

    // Add snowflake to top right
    if (!document.querySelector('.decoration-top-right')) {
        const flake = document.createElement('div');
        flake.className = 'december-decorations decoration-top-right';
        flake.textContent = '❄️';
        document.body.appendChild(flake);
    }
}

// ==============================================
// January - New Year's Celebration Decorations
// ==============================================
function addNewYearDecorations() {
    // Add sparkler/fireworks to bottom right
    if (!document.querySelector('.decoration-tree')) {
        const sparkler = document.createElement('div');
        sparkler.className = 'december-decorations decoration-tree';
        sparkler.textContent = '🎇';
        document.body.appendChild(sparkler);
    }

    // Add champagne toast to top left - celebration!
    if (!document.querySelector('.decoration-top-left')) {
        const champagne = document.createElement('div');
        champagne.className = 'december-decorations decoration-top-left';
        champagne.innerHTML = '🥂';
        document.body.appendChild(champagne);
    }

    // Add confetti ball to top right - party time!
    if (!document.querySelector('.decoration-top-right')) {
        const confetti = document.createElement('div');
        confetti.className = 'december-decorations decoration-top-right';
        confetti.textContent = '🎊';
        document.body.appendChild(confetti);
    }

    // Add floating sparkles for that fresh new year feel
    createNewYearSparkles();
}

// ==============================================
// New Year Sparkles Animation
// ==============================================
function createNewYearSparkles() {
    let sparkleContainer = document.querySelector('.new-year-sparkles');
    if (!sparkleContainer) {
        sparkleContainer = document.createElement('div');
        sparkleContainer.className = 'new-year-sparkles';
        document.body.appendChild(sparkleContainer);
    }

    const sparkles = ['✨', '⭐', '🌟', '💫', '✦', '✧'];
    for (let i = 0; i < 25; i++) {
        const sparkle = document.createElement('div');
        sparkle.className = 'sparkle';
        sparkle.textContent = sparkles[Math.floor(Math.random() * sparkles.length)];
        sparkle.style.left = Math.random() * 100 + '%';
        sparkle.style.fontSize = (Math.random() * 14 + 10) + 'px';
        sparkle.style.opacity = Math.random() * 0.7 + 0.3;
        sparkle.style.animationDuration = (Math.random() * 8 + 6) + 's';
        sparkle.style.animationDelay = (Math.random() * 8) + 's';
        sparkleContainer.appendChild(sparkle);
    }
}
