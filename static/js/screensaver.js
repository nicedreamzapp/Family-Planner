/* ==============================================
   Screensaver.js - Video Screensaver
   Family Planner Application
   ============================================== */

// ==============================================
// Screensaver State
// ==============================================
let idleTime = 0;
const screensaverTime = 3; // Minutes
let videoList = [];
let currentVideoIndex = 0;
let screensaverStarting = false;
let playPromise = null;
let isTransitioning = false;
const SLOW_MO_RATE = 0.5;

// ==============================================
// DOM Elements
// ==============================================
const screensaver = document.getElementById('screensaver');
const video = document.getElementById('screensaverVideo');
const pixelOverlay = document.getElementById('pixelOverlay');

// ==============================================
// Logging Helper
// ==============================================
function log(msg) {
    console.log("[Screensaver] " + msg);
}

// ==============================================
// Video List Initialization
// ==============================================
fetch('/api/videos')
    .then(r => r.json())
    .then(data => {
        log("Video API response: " + JSON.stringify(data));
        if (data.videos && data.videos.length > 0) {
            videoList = data.videos;
            log("Loaded " + videoList.length + " videos: " + videoList.join(", "));
            // Preload first video
            video.src = "/videos/" + videoList[0];
            video.playbackRate = SLOW_MO_RATE;
            video.load();
            log("Preloaded first video at " + SLOW_MO_RATE + "x speed");
        } else {
            log("No videos found in API response.");
        }
    })
    .catch(e => log("Video fetch error: " + e));

// ==============================================
// Idle Timer
// ==============================================
setInterval(() => {
    idleTime++;
    if (idleTime >= screensaverTime) startScreensaver();
}, 60000);

// ==============================================
// Video Transitions
// ==============================================
function transitionToNextVideo() {
    if (videoList.length === 0 || isTransitioning) {
        log("Cannot transition: No videos or already transitioning.");
        return;
    }

    isTransitioning = true;
    log("Starting smooth transition...");

    // Step 1: Add pixelation and fade out
    video.classList.add('pixelate');
    pixelOverlay.classList.add('active');

    setTimeout(() => {
        video.classList.add('fade-out');
    }, 300);

    // Step 2: Change video source while faded
    setTimeout(() => {
        currentVideoIndex = (currentVideoIndex + 1) % videoList.length;
        const src = "/videos/" + videoList[currentVideoIndex];
        log("Switching to: " + src);
        video.src = src;
        video.playbackRate = SLOW_MO_RATE;
        video.load();
    }, 1500);

    // Step 3: Wait for new video ready, then fade in
    setTimeout(() => {
        video.oncanplaythrough = function() {
            video.classList.remove('fade-out');

            setTimeout(() => {
                video.classList.remove('pixelate');
                pixelOverlay.classList.remove('active');
            }, 500);

            playPromise = video.play();
            if (playPromise) {
                playPromise.then(() => {
                    log("Next video playing at " + SLOW_MO_RATE + "x");
                    isTransitioning = false;
                }).catch(e => {
                    log("Play error: " + e);
                    isTransitioning = false;
                });
            }
            video.oncanplaythrough = null;
        };

        if (video.readyState >= 3) {
            video.oncanplaythrough();
        }
    }, 1800);
}

// ==============================================
// Video Event Handlers
// ==============================================
video.onended = transitionToNextVideo;
video.onerror = (e) => log("Video Error: " + (video.error ? video.error.message : "unknown"));
video.oncanplay = () => { video.playbackRate = SLOW_MO_RATE; };
video.onloadeddata = () => {
    log("Video data loaded, setting playback rate to " + SLOW_MO_RATE);
    video.playbackRate = SLOW_MO_RATE;
};

// ==============================================
// Start Screensaver
// ==============================================
function startScreensaver() {
    if (screensaver.classList.contains('active') || screensaverStarting) return;

    screensaverStarting = true;
    screensaver.classList.add('active');
    log("Starting screensaver...");

    // Reset any transition state
    video.classList.remove('fade-out', 'pixelate');
    pixelOverlay.classList.remove('active');
    isTransitioning = false;

    if (videoList.length === 0) {
        log("No videos available!");
        screensaverStarting = false;
        return;
    }

    if (currentVideoIndex >= videoList.length) currentVideoIndex = 0;

    const src = "/videos/" + videoList[currentVideoIndex];
    log("Video source: " + src);

    video.src = src;
    video.playbackRate = SLOW_MO_RATE;

    video.oncanplaythrough = function() {
        log("Video ready, playing at " + SLOW_MO_RATE + "x slow motion...");
        video.playbackRate = SLOW_MO_RATE;
        playPromise = video.play();
        if (playPromise !== undefined) {
            playPromise.then(() => {
                log("Playback started at " + SLOW_MO_RATE + "x!");
                video.playbackRate = SLOW_MO_RATE;
                setTimeout(() => { screensaverStarting = false; }, 500);
            }).catch(e => {
                log("Autoplay failed: " + e.name + " - " + e.message);
                screensaverStarting = false;
                if (e.name === 'NotAllowedError') {
                    log("Click/tap screen to start playback");
                }
            });
        }
        video.oncanplaythrough = null;
    };

    if (video.readyState >= 3) {
        video.oncanplaythrough();
    } else {
        video.load();
    }

    idleTime = 0;
}

// ==============================================
// User Interaction Handlers
// ==============================================
// Handle click on screensaver to start video (for autoplay policy)
screensaver.addEventListener('click', function(e) {
    if (screensaver.classList.contains('active') && video.paused) {
        log("User clicked - attempting play");
        video.playbackRate = SLOW_MO_RATE;
        playPromise = video.play();
        if (playPromise) {
            playPromise.then(() => {
                video.playbackRate = SLOW_MO_RATE;
                log("Playing after click at " + SLOW_MO_RATE + "x");
            }).catch(err => log("Still failed: " + err));
        }
        e.stopPropagation();
    }
});

// ==============================================
// Reset Timer (Exit Screensaver)
// ==============================================
function resetTimer() {
    if (screensaverStarting || isTransitioning) return;

    if (screensaver.classList.contains('active')) {
        screensaver.classList.remove('active');
        video.classList.remove('fade-out', 'pixelate');
        pixelOverlay.classList.remove('active');

        if (playPromise !== null) {
            playPromise.then(() => {
                video.pause();
            }).catch(() => {
                video.pause();
            });
        } else {
            video.pause();
        }
        playPromise = null;
    }
    idleTime = 0;
}

// Listen for user activity
['mousemove', 'mousedown', 'keypress', 'touchstart', 'scroll'].forEach(evt =>
    document.addEventListener(evt, resetTimer, false)
);
