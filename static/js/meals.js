/* ==============================================
   Meals.js - Meal Planning
   Family Planner Application
   ============================================== */

// ==============================================
// Meal Week Rendering
// ==============================================
function renderMeals() {
    const days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
    const today = new Date().toLocaleDateString('en-US', { weekday: 'long' }).toLowerCase();

    document.getElementById('mealWeek').innerHTML = days.map(day => {
        const meal = data.meals.thisWeek[day];
        const isEmpty = !meal?.name;
        return `
            <div class="meal-day ${day === today ? 'today' : ''} ${isEmpty ? 'empty' : ''}" onclick="showMealPicker('${day}')">
                <span class="meal-icon">${meal?.icon || '➕'}</span>
                <span class="day-name">${day.charAt(0).toUpperCase() + day.slice(1)}</span>
                <span class="meal-name">${meal?.name || 'Tap to plan'}</span>
            </div>
        `;
    }).join('');
}

// ==============================================
// Meal Picker Modal
// ==============================================
function showMealPicker(day) {
    selectedMealDay = day;
    document.getElementById('mealDayTitle').textContent = day.charAt(0).toUpperCase() + day.slice(1) + "'s Dinner";

    document.getElementById('mealPicker').innerHTML = data.meals.favorites.map(m => `
        <div class="person-opt" onclick="setMeal('${m.name}', '${m.icon}')" style="cursor:pointer">
            <span class="emoji">${m.icon}</span>
            <span class="name">${m.name}</span>
        </div>
    `).join('');

    document.getElementById('customMeal').value = '';
    document.getElementById('mealModal').classList.add('show');
}

// ==============================================
// Set Meal
// ==============================================
function setMeal(name, icon) {
    data.meals.thisWeek[selectedMealDay] = { name, icon };
    closeModal('mealModal');
    renderMeals();

    fetch('/api/meals/set', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ day: selectedMealDay, meal: { name, icon } })
    });
}

function saveCustomMeal() {
    const name = document.getElementById('customMeal').value;
    if (name) setMeal(name, '\uD83C\uDF7D\uFE0F');
}
