/* ==============================================
   OCR.js - Camera Capture and Event Import
   Family Planner Application
   Scan invitations, meal calendars, etc.
   ============================================== */

// ==============================================
// Camera Modal State
// ==============================================
let cameraStream = null;
let capturedImageData = null;
let useFrontCamera = false; // false = rear (environment), true = front (user)

// ==============================================
// Open Camera Modal
// ==============================================
function openCameraModal() {
    const modal = document.getElementById('cameraModal');
    if (!modal) return;

    modal.classList.add('show');
    modal.style.display = 'flex';

    // Reset to capture mode
    showCameraView();
    startCamera();
}

// ==============================================
// Close Camera Modal
// ==============================================
function closeCameraModal() {
    const modal = document.getElementById('cameraModal');
    if (modal) {
        modal.classList.remove('show');
        modal.style.display = 'none';
    }
    stopCamera();
    capturedImageData = null;
}

// ==============================================
// Start Camera Stream
// ==============================================
async function startCamera() {
    const video = document.getElementById('cameraVideo');
    const status = document.getElementById('cameraStatus');

    if (!video) return;

    try {
        // Request camera based on toggle
        const facingMode = useFrontCamera ? 'user' : 'environment';
        const constraints = {
            video: {
                facingMode: { ideal: facingMode },
                width: { ideal: 1920 },
                height: { ideal: 1080 }
            }
        };

        cameraStream = await navigator.mediaDevices.getUserMedia(constraints);
        video.srcObject = cameraStream;
        video.play();

        if (status) status.textContent = 'Position document and tap capture';
        updateCameraToggleBtn();

    } catch (err) {
        console.error('Camera error:', err);
        if (status) status.textContent = 'Camera access denied. Please allow camera permission.';
    }
}

// ==============================================
// Toggle Camera (Front/Rear)
// ==============================================
function toggleCamera() {
    useFrontCamera = !useFrontCamera;
    stopCamera();
    startCamera();
}

function updateCameraToggleBtn() {
    const btn = document.getElementById('cameraToggleBtn');
    if (btn) {
        btn.textContent = useFrontCamera ? '📷 Front' : '📷 Rear';
    }
}

// ==============================================
// Stop Camera Stream
// ==============================================
function stopCamera() {
    if (cameraStream) {
        cameraStream.getTracks().forEach(track => track.stop());
        cameraStream = null;
    }
    const video = document.getElementById('cameraVideo');
    if (video) video.srcObject = null;
}

// ==============================================
// Capture Photo
// ==============================================
function capturePhoto() {
    const video = document.getElementById('cameraVideo');
    const canvas = document.getElementById('cameraCanvas');
    const preview = document.getElementById('capturePreview');

    if (!video || !canvas) return;

    // Set canvas size to video size
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    // Draw video frame to canvas
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0);

    // Convert to data URL
    capturedImageData = canvas.toDataURL('image/jpeg', 0.9);

    // Show preview
    if (preview) {
        preview.src = capturedImageData;
    }

    // Switch to preview mode
    showPreviewView();
    stopCamera();
}

// ==============================================
// Retake Photo
// ==============================================
function retakePhoto() {
    capturedImageData = null;
    showCameraView();
    startCamera();
}

// ==============================================
// Accept Photo and Process OCR
// ==============================================
async function acceptPhoto() {
    if (!capturedImageData) return;

    const status = document.getElementById('cameraStatus');
    const acceptBtn = document.getElementById('acceptPhotoBtn');
    const retakeBtn = document.getElementById('retakePhotoBtn');
    const previewView = document.getElementById('previewView');

    // Show big processing overlay
    if (previewView) {
        previewView.innerHTML = `
            <div class="ocr-processing">
                <div class="processing-spinner"></div>
                <div class="processing-text">Reading document...</div>
                <div class="processing-sub">This may take a moment</div>
            </div>
        `;
    }
    if (status) status.textContent = 'Processing with OCR...';

    try {
        // Convert data URL to blob
        const response = await fetch(capturedImageData);
        const blob = await response.blob();

        // Create form data
        const formData = new FormData();
        formData.append('image', blob, 'capture.jpg');

        // Send to OCR endpoint
        const result = await fetch('/api/ocr', {
            method: 'POST',
            body: formData
        });

        const data = await result.json();

        if (data.error) {
            if (status) status.textContent = 'Error: ' + data.error;
            if (previewView) {
                previewView.innerHTML = `
                    <div class="ocr-error">
                        <div class="error-icon">&#9888;</div>
                        <div class="error-text">${data.error}</div>
                        <button class="btn-primary" onclick="retakePhoto()">Try Again</button>
                    </div>
                `;
            }
            return;
        }

        // Show results
        showOcrResults(data);

    } catch (err) {
        console.error('OCR error:', err);
        if (status) status.textContent = 'Error processing image.';
        if (previewView) {
            previewView.innerHTML = `
                <div class="ocr-error">
                    <div class="error-icon">&#9888;</div>
                    <div class="error-text">Connection error. Is Fia running?</div>
                    <button class="btn-primary" onclick="retakePhoto()">Try Again</button>
                </div>
            `;
        }
    }
}

// ==============================================
// Show OCR Results
// ==============================================
function showOcrResults(data) {
    const cameraView = document.getElementById('cameraView');
    const previewView = document.getElementById('previewView');
    const resultsView = document.getElementById('resultsView');
    const eventsList = document.getElementById('ocrEventsList');
    const status = document.getElementById('cameraStatus');

    if (cameraView) cameraView.style.display = 'none';
    if (previewView) previewView.style.display = 'none';
    if (resultsView) resultsView.style.display = 'block';

    const events = data.events || [];

    if (events.length === 0) {
        if (status) status.textContent = 'No events found. Try a clearer image.';
        if (eventsList) {
            eventsList.innerHTML = `
                <div class="ocr-no-events">
                    <div class="no-events-icon">&#128269;</div>
                    <div>No dates or events detected</div>
                    <button class="btn-secondary" onclick="retakePhoto()">Try Again</button>
                </div>
            `;
        }
        return;
    }

    if (status) status.textContent = `Found ${events.length} event(s). Select which to add:`;

    // Render events list with checkboxes
    if (eventsList) {
        eventsList.innerHTML = events.map((event, index) => `
            <div class="ocr-event-item">
                <input type="checkbox" id="ocrEvent${index}" checked data-index="${index}">
                <label for="ocrEvent${index}">
                    <span class="event-title">${event.title}</span>
                    <span class="event-date">${formatDate(event.date)}</span>
                </label>
            </div>
        `).join('');

        // Store events for later
        eventsList.dataset.events = JSON.stringify(events);
    }
}

// ==============================================
// Add Selected Events to Calendar
// ==============================================
async function addSelectedEvents() {
    const eventsList = document.getElementById('ocrEventsList');
    const status = document.getElementById('cameraStatus');

    if (!eventsList) return;

    const events = JSON.parse(eventsList.dataset.events || '[]');
    const checkboxes = eventsList.querySelectorAll('input[type="checkbox"]:checked');

    if (checkboxes.length === 0) {
        if (status) status.textContent = 'Please select at least one event to add.';
        return;
    }

    if (status) status.textContent = 'Adding events...';

    let addedCount = 0;
    for (const checkbox of checkboxes) {
        const index = parseInt(checkbox.dataset.index);
        const event = events[index];

        try {
            const res = await fetch('/api/calendar/add', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(event)
            });

            const result = await res.json();
            if (result.success) {
                addedCount++;
                // Add to local data
                if (data && data.calendar && data.calendar.events) {
                    data.calendar.events.push(result.event);
                }
            }
        } catch (err) {
            console.error('Failed to add event:', err);
        }
    }

    // Show success and close
    if (status) status.textContent = `Added ${addedCount} event(s) to calendar!`;

    // Refresh calendar display
    if (typeof renderCalendar === 'function') {
        renderCalendar();
    }
    if (typeof renderTodayEvents === 'function') {
        renderTodayEvents();
    }

    // Close modal after a moment
    setTimeout(() => {
        closeCameraModal();
    }, 1500);
}

// ==============================================
// View Helpers
// ==============================================
function showCameraView() {
    const cameraView = document.getElementById('cameraView');
    const previewView = document.getElementById('previewView');
    const resultsView = document.getElementById('resultsView');
    const status = document.getElementById('cameraStatus');

    if (cameraView) cameraView.style.display = 'block';
    if (previewView) previewView.style.display = 'none';
    if (resultsView) resultsView.style.display = 'none';
    if (status) status.textContent = 'Position document and tap capture';
}

function showPreviewView() {
    const cameraView = document.getElementById('cameraView');
    const previewView = document.getElementById('previewView');
    const resultsView = document.getElementById('resultsView');
    const status = document.getElementById('cameraStatus');
    const acceptBtn = document.getElementById('acceptPhotoBtn');
    const retakeBtn = document.getElementById('retakePhotoBtn');

    if (cameraView) cameraView.style.display = 'none';
    if (previewView) previewView.style.display = 'block';
    if (resultsView) resultsView.style.display = 'none';
    if (status) status.textContent = 'Is the image clear? Accept or retake.';
    if (acceptBtn) acceptBtn.disabled = false;
    if (retakeBtn) retakeBtn.disabled = false;
}

// ==============================================
// Utility: Format Date
// ==============================================
function formatDate(dateStr) {
    try {
        const date = new Date(dateStr + 'T00:00:00');
        return date.toLocaleDateString('en-US', {
            weekday: 'short',
            month: 'short',
            day: 'numeric',
            year: 'numeric'
        });
    } catch {
        return dateStr;
    }
}
