/* ==============================================
   Shopping.js - Shopping List Management
   Family Planner Application
   ============================================== */

// ==============================================
// Render Shopping List
// ==============================================
function renderShopping() {
    const items = data.shopping.items;
    const checkedCount = items.filter(i => i.checked).length;

    let html = '';

    // Show action buttons if there are items
    if (items.length > 0) {
        html += `<div class="shopping-actions">
            ${checkedCount > 0 ? `<button class="clear-checked-btn" onclick="clearChecked()">Clear Checked (${checkedCount})</button>` : ''}
            <button class="clear-all-btn" onclick="clearAllItems()">Clear All</button>
        </div>`;
    }

    html += items.length ?
        items.map(i => `
            <div class="shopping-item ${i.checked ? 'checked' : ''}">
                <div class="checkbox" onclick="toggleItem(${i.id})">${i.checked ? '\u2713' : ''}</div>
                <span onclick="toggleItem(${i.id})">${i.name}</span>
                <button class="delete-item-btn" onclick="deleteItem(${i.id})">\u2715</button>
            </div>
        `).join('') :
        '<div class="empty-state"><div class="icon">\uD83D\uDED2</div>Shopping list is empty</div>';

    document.getElementById('shoppingList').innerHTML = html;
}

// ==============================================
// Add Shopping Item
// ==============================================
async function addShoppingItem() {
    const input = document.getElementById('newItem');
    const name = input.value.trim();
    if (!name) return;

    const tempId = Date.now();
    const newItem = { id: tempId, name, checked: false };

    data.shopping.items.push(newItem);
    input.value = '';
    renderShopping();

    fetch('/api/shopping/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name })
    }).then(res => res.json()).then(result => {
        if (result.success) {
            const idx = data.shopping.items.findIndex(i => i.id === tempId);
            if (idx !== -1) data.shopping.items[idx].id = result.item.id;
        }
    });
}

// ==============================================
// Toggle Shopping Item
// ==============================================
function toggleItem(id) {
    const item = data.shopping.items.find(i => i.id === id);
    if (item) item.checked = !item.checked;
    renderShopping();

    fetch('/api/shopping/toggle', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id })
    });
}

// ==============================================
// Delete Single Item
// ==============================================
function deleteItem(id) {
    data.shopping.items = data.shopping.items.filter(i => i.id !== id);
    renderShopping();

    fetch('/api/shopping/delete', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id })
    });
}

// ==============================================
// Clear Checked Items
// ==============================================
function clearChecked() {
    data.shopping.items = data.shopping.items.filter(i => !i.checked);
    renderShopping();

    fetch('/api/shopping/clear', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: '{}'
    });
}

// ==============================================
// Clear All Items
// ==============================================
function clearAllItems() {
    if (confirm('Clear all shopping items?')) {
        data.shopping.items = [];
        renderShopping();

        fetch('/api/shopping/clearall', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: '{}'
        });
    }
}
