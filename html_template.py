"""
HTML template for Family Family Hub dashboard.
"""


def get_dashboard_html():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="mobile-web-app-capable" content="yes">
    <title>Family Family Calendar 2025</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }

        :root {
            --bg-cream: #FFFFFF;
            --bg-warm: #F8F9FA;
            --text-dark: #1A1A1A;
            --text-muted: #4A4A4A;
            --border-gold: #C9A66B;
            --border-light: #D4D4D4;
            --accent-orange: #D84315;
            --accent-pink: #C2185B;
            --accent-teal: #00838F;
            --accent-purple: #7B1FA2;
            --accent-blue: #1565C0;
            --accent-green: #2E7D32;
            --accent-yellow: #F9A825;
            --shadow: rgba(0,0,0,0.12);

            --matt: #1565C0;
            --melanie: #C2185B;
            --liv: #7B1FA2;
            --jane: #E65100;
            --family: #2E7D32;

            /* Responsive Variables */
            --fs-xxs: 10px;
            --fs-xs: 11px;
            --fs-sm: 13px;
            --fs-base: 16px;
            --fs-md: 18px;
            --fs-lg: 20px;
            --fs-xl: 24px;
            --fs-xxl: 36px;
            --fs-huge: 48px;

            --sidebar-width: 240px;
            --spacing-base: 15px;
        }

        html, body {
            margin: 0;
            padding: 0;
            height: 100vh;
            height: 100dvh;
            height: var(--vh, 100vh);
            overflow: hidden;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
        }

        body {
            font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg-cream);
            color: var(--text-dark);
        }

        /* Main Layout */
        .app-container {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            height: 100vh;
            height: 100dvh;
            height: var(--vh, 100vh);
            display: flex;
            overflow: hidden;
        }

        /* Left Sidebar - Hidden */
        .sidebar {
            display: none;
        }

        .sidebar-header {
            text-align: center;
            margin-bottom: 10px;
        }

        .current-time {
            font-size: 36px;
            font-weight: 200;
            color: var(--text-dark);
            line-height: 1;
        }

        .current-date {
            font-size: var(--fs-base);
            color: var(--text-muted);
            margin-top: 6px;
        }

        .family-name {
            font-size: var(--fs-xs);
            text-transform: uppercase;
            letter-spacing: 3px;
            color: var(--border-gold);
            margin-top: 15px;
        }

        /* Jump to month - Quick Nav */
        .month-nav {
            margin-bottom: 15px;
        }

        .month-nav-title {
            font-size: var(--fs-xxs);
            text-transform: uppercase;
            letter-spacing: 2px;
            color: var(--text-muted);
            margin-bottom: 8px;
        }

        .month-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 4px;
        }

        .month-btn {
            padding: 8px 4px;
            border: 1px solid var(--border-light);
            border-radius: 8px;
            background: white;
            font-size: var(--fs-xs);
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }

        .month-btn:hover {
            border-color: var(--border-gold);
            background: var(--bg-warm);
        }

        .month-btn.current {
            background: var(--accent-orange);
            color: white;
            border-color: var(--accent-orange);
        }

        /* Today's Events Section */
        .today-section {
            margin-bottom: 15px;
        }

        .section-title {
            font-size: var(--fs-xxs);
            text-transform: uppercase;
            letter-spacing: 2px;
            color: var(--text-muted);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
            flex-shrink: 0;
        }

        .section-title::after {
            content: '';
            flex: 1;
            height: 1px;
            background: var(--border-light);
        }

        .today-event {
            display: flex;
            align-items: center;
            padding: 10px 12px;
            background: white;
            border-radius: 10px;
            margin-bottom: 6px;
            border-left: 3px solid var(--accent-orange);
            box-shadow: 0 2px 6px var(--shadow);
            font-size: var(--fs-sm);
        }

        .today-event .event-time {
            font-size: var(--fs-xs);
            color: var(--text-muted);
            width: 45px;
        }

        .today-event .event-title {
            flex: 1;
            font-weight: 500;
        }

        /* Weather */
        .weather-widget {
            background: white;
            border-radius: 10px;
            padding: 10px;
            text-align: center;
            box-shadow: 0 2px 8px var(--shadow);
            margin-bottom: 10px;
        }

        .weather-temp {
            font-size: 28px;
            font-weight: 200;
        }

        .weather-desc {
            font-size: 11px;
            color: var(--text-muted);
        }

        .weather-forecast {
            margin-top: 8px;
            border-top: 1px solid var(--border-light);
            padding-top: 8px;
        }

        .forecast-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 11px;
            margin-bottom: 4px;
        }

        .forecast-day {
            font-weight: 500;
            width: 50px;
        }

        .forecast-icon {
            font-size: 14px;
        }

        .forecast-temps {
            color: var(--text-muted);
            font-size: 11px;
        }

        .rain-alert {
            font-size: 9px;
            color: #1565C0;
            background: #E3F2FD;
            padding: 1px 4px;
            border-radius: 4px;
            margin-left: 2px;
            display: inline-block;
        }

        /* Quick Actions */
        .quick-actions {
            margin-top: auto;
        }

        .quick-btn {
            display: flex;
            align-items: center;
            gap: 8px;
            width: 100%;
            padding: 8px 12px;
            background: white;
            border: 1px solid var(--border-light);
            border-radius: 8px;
            color: var(--text-dark);
            font-size: 13px;
            cursor: pointer;
            margin-bottom: 6px;
            transition: all 0.2s;
        }

        .quick-btn:hover {
            border-color: var(--border-gold);
            box-shadow: 0 2px 8px var(--shadow);
        }

        .quick-btn .icon {
            font-size: 18px;
        }

        /* Main Calendar Area - Full Width */
        .main-content {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            padding: 10px 15px 10px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        /* Year Header */
        .year-header {
            background: var(--bg-cream);
            z-index: 50;
            padding: 8px 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid var(--border-gold);
            margin-bottom: 10px;
            flex-shrink: 0;
        }

        .year-nav {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .year-title {
            font-size: var(--fs-xxl);
            font-weight: 300;
            color: var(--text-dark);
            margin: 0;
        }

        .page-title {
            font-size: 28px;
            font-weight: 600;
            color: var(--text-dark);
            margin: 0;
        }

        .year-arrow {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            border: 2px solid var(--border-gold);
            background: white;
            color: var(--border-gold);
            font-size: var(--fs-base);
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .year-arrow:hover {
            background: var(--border-gold);
            color: white;
        }

        .header-actions {
            display: flex;
            gap: 12px;
            align-items: center;
            flex: 1;
            justify-content: center;
            margin: 0 30px;
        }

        .action-pill {
            padding: 14px 24px;
            border-radius: 25px;
            border: none;
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            color: #333;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 3px 8px rgba(0,0,0,0.1);
            white-space: nowrap;
        }

        .action-pill:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(0,0,0,0.15);
            background: linear-gradient(145deg, #fff, #f8f8f8);
        }

        .action-pill.ocean {
            background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
            color: #1565C0;
        }

        .action-pill.ocean:hover {
            background: linear-gradient(135deg, #BBDEFB, #90CAF9);
        }

        .today-btn {
            padding: 10px 20px;
            background: var(--accent-orange);
            border: none;
            border-radius: 25px;
            color: white;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s;
        }

        .today-btn:hover {
            background: #E55D3A;
            transform: scale(1.02);
        }

        /* Header Compact Info Section */
        .header-info {
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 0 10px;
        }

        .header-time-date {
            display: flex;
            flex-direction: column;
            align-items: center;
            line-height: 1.1;
        }

        .header-time {
            font-size: 20px;
            font-weight: 300;
            color: var(--text-dark);
        }

        .header-date {
            font-size: 11px;
            color: var(--text-muted);
        }

        .header-weather {
            display: flex;
            align-items: center;
            gap: 6px;
            background: white;
            padding: 6px 12px;
            border-radius: 20px;
            box-shadow: 0 2px 6px var(--shadow);
        }

        .header-weather-temp {
            font-size: 16px;
            font-weight: 500;
        }

        .header-weather-icon {
            font-size: 18px;
        }

        /* Month Select Dropdown in Header */
        .month-select-wrapper {
            position: relative;
        }

        .month-select {
            padding: 8px 30px 8px 12px;
            border: 1px solid var(--border-light);
            border-radius: 20px;
            background: white;
            font-size: 13px;
            font-weight: 500;
            cursor: pointer;
            appearance: none;
            -webkit-appearance: none;
        }

        .month-select-wrapper::after {
            content: '▼';
            position: absolute;
            right: 12px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 10px;
            pointer-events: none;
            color: var(--text-muted);
        }

        /* Kid Buttons - 30% Bigger than other pills */
        .action-pill.kid-btn {
            padding: 18px 32px;
            font-size: 21px;
            font-weight: 700;
        }

        .action-pill.kid-btn.liv {
            background: linear-gradient(135deg, #F3E5F5, #E1BEE7);
            color: var(--liv);
        }

        .action-pill.kid-btn.liv:hover {
            background: linear-gradient(135deg, #E1BEE7, #CE93D8);
            transform: translateY(-2px);
        }

        .action-pill.kid-btn.jane {
            background: linear-gradient(135deg, #FFF3E0, #FFE0B2);
            color: var(--jane);
        }

        .action-pill.kid-btn.jane:hover {
            background: linear-gradient(135deg, #FFE0B2, #FFCC80);
            transform: translateY(-2px);
        }

        /* Month Section */
        .month-section {
            margin-bottom: 40px;
            scroll-margin-top: 100px;
        }

        .month-header {
            font-size: var(--fs-xl);
            font-weight: 400;
            color: var(--text-dark);
            margin-bottom: 15px;
            padding: 10px 15px;
            background: linear-gradient(90deg, var(--bg-warm), transparent);
            border-left: 4px solid var(--accent-orange);
            border-radius: 0 10px 10px 0;
        }

        /* Calendar Grid */
        .calendar-grid {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            grid-template-rows: auto repeat(6, minmax(0, 1fr));
            border: 2px solid var(--border-gold);
            border-radius: 12px;
            overflow: hidden;
            background: white;
            box-shadow: 0 4px 15px var(--shadow);
            flex: 1 1 0;
            min-height: 0;
            max-height: 100%;
        }

        .day-header-row {
            display: contents;
        }

        .day-header-cell {
            padding: 8px 4px;
            text-align: center;
            background: var(--bg-warm);
            border-bottom: 1px solid var(--border-light);
            font-size: var(--fs-xs);
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-muted);
            font-weight: 600;
            min-width: 0;
            overflow: hidden;
        }

        .day-header-cell.weekend {
            background: #FFF5F2;
            color: var(--accent-orange);
        }

        .calendar-day {
            min-width: 0;
            min-height: 0;
            padding: 4px;
            border-right: 1px solid var(--border-light);
            border-bottom: 1px solid var(--border-light);
            cursor: pointer;
            transition: background 0.2s;
            position: relative;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        .calendar-day:nth-child(7n) {
            border-right: none;
        }

        .calendar-day:hover {
            background: var(--bg-warm);
        }

        .calendar-day.other-month {
            background: #FAFAFA;
            opacity: 0.5;
        }

        .calendar-day.today {
            background: #FFF5F2;
            box-shadow: inset 0 0 0 2px var(--accent-orange);
        }

        .calendar-day.weekend {
            background: #FFFBFA;
        }

        .day-num {
            font-size: var(--fs-lg);
            font-weight: 600;
            color: var(--text-dark);
            margin-bottom: 8px;
        }

        .calendar-day.today .day-num {
            background: var(--accent-orange);
            color: white;
            width: 32px;
            height: 32px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            font-size: var(--fs-md);
        }

        .calendar-day.other-month .day-num {
            color: var(--text-muted);
        }

        /* Events in calendar cells */
        .day-events {
            display: flex;
            flex-direction: column;
            gap: 4px;
            flex: 1;
            overflow-y: auto;
            min-width: 0;
        }

        .event-pill {
            padding: 6px 10px;
            border-radius: 6px;
            font-size: var(--fs-sm);
            position: relative;
            font-weight: 500;
            color: white;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            min-width: 0;
        }

        .event-pill.matt { background: var(--matt); }
        .event-pill.melanie { background: var(--melanie); }
        .event-pill.liv { background: var(--liv); }
        .event-pill.jane { background: var(--jane); }
        .event-pill.family { background: var(--family); }

        .event-pill .pill-delete {
            position: absolute;
            right: 2px;
            top: 50%;
            transform: translateY(-50%);
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: rgba(0,0,0,0.3);
            color: white;
            border: none;
            cursor: pointer;
            font-size: 12px;
            line-height: 18px;
            text-align: center;
            opacity: 0;
            transition: opacity 0.15s;
            padding: 0;
        }

        .event-pill:hover .pill-delete {
            opacity: 1;
        }

        .event-pill .pill-delete:hover {
            background: rgba(0,0,0,0.6);
        }

        /* Holiday in cell */
        .holiday-pill {
            padding: 6px 10px;
            background: linear-gradient(135deg, #FFF3E0, #FFE0B2);
            border-radius: 8px;
            font-size: var(--fs-sm);
            font-weight: 600;
            color: #D84315;
            display: flex;
            align-items: center;
            gap: 6px;
            margin-bottom: 4px;
            border: 1px solid #FFCC80;
        }

        .holiday-pill .emoji {
            font-size: 16px;
        }

        /* Add Event Button */
        .add-event-btn {
            position: fixed;
            bottom: 80px;
            right: 25px;
            width: 56px;
            height: 56px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--accent-orange), #E55D3A);
            border: none;
            color: white;
            font-size: 26px;
            cursor: pointer;
            box-shadow: 0 4px 20px rgba(246, 105, 81, 0.4);
            transition: all 0.2s;
            z-index: 100;
        }

        .add-event-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 25px rgba(246, 105, 81, 0.5);
        }


        /* Large Screen Responsiveness (> 9in tablet approx >1024px) */
        @media (min-width: 1024px) {
            :root {
                --fs-xxs: 14px;
                --fs-xs: 16px;
                --fs-sm: 18px;
                --fs-base: 22px;
                --fs-md: 24px;
                --fs-lg: 28px;
                --fs-xl: 32px;
                --fs-xxl: 48px;
                --fs-huge: 64px;

                --sidebar-width: 350px;
                --spacing-base: 30px;
            }

            .day-num {
                margin-bottom: 12px;
            }
            
            .event-pill {
                padding: 8px 14px;
            }
            
            .current-time {
                font-size: 80px;
            }

            /* Better grid gap on big screens */
            .month-grid {
                gap: 8px;
            }
            
            .month-btn {
                padding: 12px 0;
            }
            
            /* Responsive Weather */
            .forecast-item {
                font-size: var(--fs-sm);
                margin-bottom: 10px;
            }
            
            .rain-alert {
                font-size: var(--fs-xxs);
            }
        }

        .nav-item:hover {
            background: var(--bg-warm);
        }

        .nav-item.active {
            color: var(--accent-orange);
            background: #FFF5F2;
        }

        .nav-item .icon {
            font-size: 22px;
        }

        /* Modal */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            z-index: 1000;
            align-items: center;
            justify-content: center;
        }

        .modal.show {
            display: flex;
        }

        .modal-content {
            background: white;
            border-radius: 20px;
            padding: 25px;
            width: 90%;
            max-width: 420px;
            max-height: 90vh;
            overflow-y: auto;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }

        .modal h2 {
            font-size: 22px;
            font-weight: 400;
            margin-bottom: 20px;
            color: var(--text-dark);
        }

        .modal input, .modal select {
            width: 100%;
            padding: 12px 16px;
            margin-bottom: 12px;
            border-radius: 10px;
            border: 2px solid var(--border-light);
            font-size: 15px;
            color: var(--text-dark);
            background: white;
            transition: border-color 0.2s;
        }

        .modal input:focus, .modal select:focus {
            outline: none;
            border-color: var(--accent-orange);
        }

        .person-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            margin-bottom: 15px;
        }

        .person-opt {
            padding: 12px 8px;
            border-radius: 10px;
            border: 2px solid var(--border-light);
            background: white;
            cursor: pointer;
            text-align: center;
            transition: all 0.2s;
        }

        .person-opt:hover {
            border-color: var(--border-gold);
        }

        .person-opt.selected {
            border-color: currentColor;
            background: currentColor;
        }

        .person-opt.selected .name {
            color: white;
        }

        .person-opt .emoji {
            font-size: 24px;
            display: block;
            margin-bottom: 4px;
        }

        .person-opt .name {
            font-size: 11px;
            color: var(--text-dark);
        }

        .modal-btns {
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }

        .modal-btns button {
            flex: 1;
            padding: 12px;
            border-radius: 10px;
            font-size: 15px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s;
        }

        .btn-primary {
            background: var(--accent-orange);
            border: none;
            color: white;
        }

        .btn-primary:hover {
            background: #E55D3A;
        }

        .btn-secondary {
            background: white;
            border: 2px solid var(--border-light);
            color: var(--text-dark);
        }

        .btn-secondary:hover {
            border-color: var(--border-gold);
        }

        /* Panels */
        .panel {
            display: none;
        }

        .panel.active {
            display: flex;
            flex-direction: column;
            flex: 1 1 0;
            min-height: 0;
            max-height: 100%;
            overflow: hidden;
        }

        /* Panel content containers - fill remaining space */
        #yearCalendar {
            flex: 1 1 0;
            display: flex;
            flex-direction: column;
            min-height: 0;
            max-height: 100%;
            overflow: hidden;
        }

        #shoppingList {
            display: grid;
            gap: 10px;
            flex: 1;
            overflow-y: auto;
            min-height: 0;
            align-content: start;
        }

        #mealWeek {
            flex: 1;
            overflow-y: auto;
            min-height: 0;
        }

        /* Shopping List Panel */
        .shopping-list {
            background: white;
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 4px 20px var(--shadow);
        }

        .shopping-input {
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
        }

        .shopping-input input {
            flex: 1;
            padding: 12px 16px;
            border: 2px solid var(--border-light);
            border-radius: 10px;
            font-size: 15px;
        }

        .shopping-input input:focus {
            outline: none;
            border-color: var(--accent-orange);
        }

        .shopping-input button {
            padding: 12px 20px;
            background: var(--accent-orange);
            border: none;
            border-radius: 10px;
            color: white;
            font-size: 18px;
            cursor: pointer;
        }

        .shopping-item {
            display: flex;
            align-items: center;
            padding: 12px 15px;
            border-bottom: 1px solid var(--border-light);
            cursor: pointer;
            transition: background 0.2s;
        }

        .shopping-item:hover {
            background: var(--bg-warm);
        }

        .shopping-item.checked {
            opacity: 0.5;
            text-decoration: line-through;
        }

        .shopping-item .checkbox {
            width: 22px;
            height: 22px;
            border: 2px solid var(--border-gold);
            border-radius: 6px;
            margin-right: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--accent-orange);
            font-size: 12px;
        }

        .shopping-item.checked .checkbox {
            background: var(--accent-green);
            border-color: var(--accent-green);
            color: white;
        }

        /* Meals Panel */
        .meal-week {
            display: flex;
            flex-direction: column;
            gap: 8px;
            flex: 1;
            overflow-y: auto;
            min-height: 0;
        }

        .meal-day {
            display: flex;
            align-items: center;
            padding: 14px 18px;
            background: white;
            border-radius: 12px;
            border: 2px solid var(--border-light);
            cursor: pointer;
            transition: all 0.2s;
        }

        .meal-day:hover {
            border-color: var(--border-gold);
        }

        .meal-day.today {
            border-color: var(--accent-orange);
            background: #FFF5F2;
        }

        .meal-day .day-name {
            width: 90px;
            font-weight: 600;
            color: var(--text-dark);
        }

        .meal-day .meal-name {
            flex: 1;
            color: var(--text-muted);
        }

        .meal-day .meal-icon {
            font-size: 24px;
        }

        /* Kids/Chores Panel */
        .kids-header {
            display: flex;
            gap: 12px;
            margin-bottom: 20px;
            flex-shrink: 0;
        }

        .kid-card {
            flex: 1;
            padding: 20px 15px;
            border-radius: 14px;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s;
            border: 3px solid transparent;
        }

        .kid-card.liv {
            background: linear-gradient(135deg, #F3E5F5, #E1BEE7);
        }

        .kid-card.jane {
            background: linear-gradient(135deg, #FFF3E0, #FFE0B2);
        }

        .kid-card.selected {
            border-color: var(--accent-orange);
            transform: scale(1.02);
        }

        .kid-card .emoji {
            font-size: 40px;
        }

        .kid-card .name {
            font-size: 18px;
            font-weight: 600;
            margin: 8px 0 4px;
        }

        .kid-card .points {
            font-size: 20px;
            font-weight: 700;
            color: var(--accent-orange);
        }

        .chore-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
            flex: 1;
            overflow-y: auto;
            min-height: 0;
            align-content: start;
        }

        .chore-btn {
            padding: 18px 12px;
            background: white;
            border: 2px solid var(--border-light);
            border-radius: 14px;
            cursor: pointer;
            text-align: center;
            transition: all 0.2s;
        }

        .chore-btn:hover {
            border-color: var(--border-gold);
        }

        .chore-btn.done {
            background: #E8F5E9;
            border-color: var(--accent-green);
        }

        .chore-btn .icon {
            font-size: 28px;
            margin-bottom: 6px;
        }

        .chore-btn .name {
            font-size: 12px;
            color: var(--text-dark);
            margin-bottom: 4px;
        }

        .chore-btn .pts {
            font-size: 11px;
            color: var(--accent-orange);
            font-weight: 600;
        }

        /* Day detail modal - ENHANCED & INTERACTIVE */
        .day-events-modal {
            max-width: 600px !important;
            max-height: 85vh !important;
        }

        .day-events-modal .event-item {
            display: flex;
            align-items: center;
            padding: 12px;
            background: var(--bg-warm);
            border-radius: 10px;
            margin-bottom: 8px;
            border-left: 4px solid var(--accent-orange);
        }

        .day-events-modal .event-item .title {
            flex: 1;
            font-weight: 500;
        }

        .day-events-modal .event-item .time {
            font-size: 12px;
            color: var(--text-muted);
            margin-right: 10px;
        }

        .day-events-modal .event-item .delete-btn {
            width: 28px;
            height: 28px;
            border: none;
            background: #ffebee;
            color: #c62828;
            border-radius: 50%;
            cursor: pointer;
            font-size: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
            flex-shrink: 0;
        }

        .day-events-modal .event-item .delete-btn:hover {
            background: #c62828;
            color: white;
        }

        .holiday-banner {
            padding: 15px;
            background: linear-gradient(90deg, #E8F5E9, #FFF3E0);
            border-radius: 12px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 10px;
            border: 2px solid #FFE082;
        }

        .holiday-banner .emoji {
            font-size: 32px;
            animation: holidayBounce 1s ease-in-out infinite;
        }

        @keyframes holidayBounce {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }

        .holiday-banner .text {
            font-weight: 600;
            font-size: 16px;
            color: var(--text-dark);
        }

        /* Day Modal Tabs */
        .day-tabs {
            display: flex;
            gap: 8px;
            margin-bottom: 15px;
            border-bottom: 2px solid var(--border-light);
            padding-bottom: 10px;
        }

        .day-tab {
            padding: 10px 15px;
            border: none;
            background: var(--bg-warm);
            border-radius: 20px;
            cursor: pointer;
            font-size: 13px;
            font-weight: 600;
            color: var(--text-muted);
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .day-tab:hover {
            background: var(--accent-orange);
            color: white;
        }

        .day-tab.active {
            background: var(--accent-orange);
            color: white;
        }

        .day-tab .tab-emoji {
            font-size: 16px;
        }

        /* Day Modal Sections */
        .day-section {
            display: none;
            animation: fadeIn 0.3s ease;
        }

        .day-section.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Chore Achievement Section in Modal */
        .modal-chore-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 10px;
        }

        .modal-kid-column {
            background: white;
            border-radius: 12px;
            padding: 15px;
            border: 2px solid var(--border-light);
        }

        .modal-kid-column.liv {
            border-color: var(--liv);
            background: linear-gradient(135deg, #F3E5F5, white);
        }

        .modal-kid-column.jane {
            border-color: var(--jane);
            background: linear-gradient(135deg, #FFF3E0, white);
        }

        .modal-kid-header {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 12px;
            padding-bottom: 10px;
            border-bottom: 2px solid currentColor;
        }

        .modal-kid-header .avatar {
            font-size: 28px;
        }

        .modal-kid-header .name {
            font-size: 16px;
            font-weight: 700;
        }

        .modal-kid-header .points {
            margin-left: auto;
            background: var(--accent-orange);
            color: white;
            padding: 4px 10px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 700;
        }

        .modal-chore-item {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 10px;
            background: white;
            border-radius: 8px;
            margin-bottom: 6px;
            cursor: pointer;
            transition: all 0.2s;
            border: 1px solid #eee;
        }

        .modal-chore-item:hover {
            background: #E8F5E9;
            border-color: var(--accent-green);
        }

        .modal-chore-item.done {
            background: #C8E6C9;
            border-color: var(--accent-green);
        }

        .modal-chore-item .chore-icon {
            font-size: 20px;
        }

        .modal-chore-item .chore-name {
            flex: 1;
            font-size: 13px;
        }

        .modal-chore-item .chore-points {
            font-size: 11px;
            color: var(--accent-orange);
            font-weight: 600;
        }

        .modal-chore-check {
            width: 20px;
            height: 20px;
            border: 2px solid var(--accent-green);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }

        .modal-chore-item.done .modal-chore-check {
            background: var(--accent-green);
        }

        /* Achievement/Progress Bar */
        .achievement-bar {
            margin-top: 15px;
            padding: 12px;
            background: linear-gradient(135deg, #FFF8E1, #FFECB3);
            border-radius: 10px;
            text-align: center;
        }

        .achievement-bar .label {
            font-size: 12px;
            color: var(--text-muted);
            margin-bottom: 8px;
        }

        .progress-track {
            height: 12px;
            background: rgba(255,255,255,0.8);
            border-radius: 6px;
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #4CAF50, #8BC34A);
            border-radius: 6px;
            transition: width 0.5s ease;
        }

        .achievement-text {
            margin-top: 8px;
            font-size: 14px;
            font-weight: 600;
            color: var(--accent-orange);
        }

        /* Family Log / Journal Section */
        .family-log {
            margin-top: 10px;
        }

        .log-entry {
            padding: 15px;
            background: white;
            border-radius: 12px;
            margin-bottom: 10px;
            border-left: 4px solid var(--border-gold);
            box-shadow: 0 2px 8px var(--shadow);
        }

        .log-entry .entry-header {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 8px;
        }

        .log-entry .entry-person {
            font-weight: 600;
            color: var(--text-dark);
        }

        .log-entry .entry-time {
            font-size: 11px;
            color: var(--text-muted);
            margin-left: auto;
        }

        .log-entry .entry-text {
            font-size: 14px;
            color: var(--text-dark);
            line-height: 1.5;
        }

        .log-entry .entry-feeling {
            margin-top: 8px;
            padding: 8px 12px;
            background: var(--bg-warm);
            border-radius: 8px;
            font-size: 13px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* Add Note Form */
        .add-note-form {
            background: var(--bg-warm);
            padding: 15px;
            border-radius: 12px;
            margin-top: 10px;
        }

        .add-note-form textarea {
            width: 100%;
            min-height: 80px;
            padding: 12px;
            border: 2px solid var(--border-light);
            border-radius: 10px;
            font-size: 14px;
            resize: vertical;
            font-family: inherit;
        }

        .add-note-form textarea:focus {
            outline: none;
            border-color: var(--accent-orange);
        }

        .feeling-picker {
            display: flex;
            gap: 8px;
            margin: 12px 0;
            flex-wrap: wrap;
        }

        .feeling-btn {
            padding: 8px 12px;
            border: 2px solid var(--border-light);
            border-radius: 20px;
            background: white;
            cursor: pointer;
            font-size: 20px;
            transition: all 0.2s;
        }

        .feeling-btn:hover {
            border-color: var(--accent-orange);
            transform: scale(1.1);
        }

        .feeling-btn.selected {
            border-color: var(--accent-orange);
            background: #FFF5F2;
        }

        /* Voice Memory Button */
        .voice-memory-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
            border: 2px dashed #2196F3;
            border-radius: 12px;
            cursor: pointer;
            font-size: 15px;
            font-weight: 600;
            color: #1565C0;
            margin-top: 15px;
            transition: all 0.2s;
        }

        .voice-memory-btn:hover {
            background: linear-gradient(135deg, #BBDEFB, #90CAF9);
            transform: scale(1.02);
        }

        .voice-memory-btn.recording {
            background: linear-gradient(135deg, #FFCDD2, #EF9A9A);
            border-color: #E53935;
            color: #B71C1C;
            animation: pulse 1s ease-in-out infinite;
        }

        .empty-state {
            text-align: center;
            padding: 30px;
            color: var(--text-muted);
        }

        .empty-state .icon {
            font-size: 40px;
            margin-bottom: 12px;
            opacity: 0.5;
        }

        /* Collapsed Month Styles */
        .collapsed-month {
            background: white;
            border: 2px solid var(--border-light);
            border-radius: 12px;
            padding: 12px 15px;
            margin-bottom: 10px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .collapsed-month:hover {
            border-color: var(--border-gold);
            box-shadow: 0 2px 10px var(--shadow);
        }

        .collapsed-header {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .collapsed-name {
            font-size: 16px;
            font-weight: 600;
            color: var(--text-dark);
        }

        .collapsed-info {
            flex: 1;
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }

        .event-badge {
            font-size: 11px;
            background: var(--accent-orange);
            color: white;
            padding: 2px 8px;
            border-radius: 10px;
        }

        .holiday-badge {
            font-size: 14px;
        }

        .expand-arrow {
            color: var(--text-muted);
            font-size: 12px;
        }

        /* Mini Calendar for collapsed months */
        .mini-calendar {
            margin-top: 10px;
        }

        .mini-grid {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 2px;
        }

        .mini-header {
            font-size: 9px;
            text-align: center;
            color: var(--text-muted);
            padding: 2px;
        }

        .mini-day {
            font-size: 10px;
            text-align: center;
            padding: 3px 2px;
            border-radius: 3px;
            color: var(--text-dark);
        }

        .mini-day.empty {
            color: transparent;
        }

        .mini-day.today {
            background: var(--accent-orange);
            color: white;
            font-weight: 600;
        }

        .mini-day.has-event {
            background: #E3F2FD;
            font-weight: 500;
        }

        .mini-day.has-holiday {
            background: #FFF3E0;
            color: #E65100;
        }

        /* Expanded Month Styles */
        .expanded-month {
            background: white;
            border: 2px solid var(--border-gold);
            border-radius: 16px;
            padding: 10px;
            box-shadow: 0 4px 20px var(--shadow);
            overflow: hidden;
            flex: 1 1 0;
            display: flex;
            flex-direction: column;
            min-height: 0;
            max-height: 100%;
        }

        .expanded-header {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            margin-bottom: 8px;
            flex-shrink: 0;
        }

        .expanded-header .month-title {
            font-size: 28px;
            font-weight: 400;
            color: var(--text-dark);
            margin: 0;
        }

        .nav-arrow {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            border: 2px solid var(--border-gold);
            background: white;
            color: var(--border-gold);
            font-size: 14px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .nav-arrow:hover {
            background: var(--border-gold);
            color: white;
        }

        /* Voice mic button style */
        .mic-btn {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            border: 2px solid var(--accent-orange);
            background: linear-gradient(135deg, #FFF5F2, white);
            color: var(--accent-orange);
            font-size: 20px;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }

        .mic-btn:hover {
            background: var(--accent-orange);
            color: white;
            transform: scale(1.05);
        }

        .mic-btn.recording {
            background: #E53935;
            border-color: #E53935;
            color: white;
            animation: pulse 1s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }

        /* Help tooltip */
        .help-tip {
            position: relative;
            display: inline-block;
        }

        .help-tip::after {
            content: attr(data-tip);
            position: absolute;
            bottom: 100%;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0,0,0,0.85);
            color: white;
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 12px;
            white-space: nowrap;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.2s;
            z-index: 1000;
        }

        .help-tip:hover::after {
            opacity: 1;
        }

        /* School Lunch indicator - FUN and COLORFUL for kids! */
        .lunch-pill {
            padding: 8px 12px;
            background: linear-gradient(135deg, #FFE082, #FFCA28);
            border-radius: 20px;
            font-size: 13px;
            font-weight: 700;
            color: #E65100;
            display: flex;
            align-items: center;
            gap: 6px;
            margin-top: 6px;
            border: 2px dashed #FF9800;
            box-shadow: 0 2px 8px rgba(255, 152, 0, 0.3);
            animation: lunchBounce 2s ease-in-out infinite;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }

        @keyframes lunchBounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-2px); }
        }

        .lunch-pill:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 12px rgba(255, 152, 0, 0.5);
        }

        .lunch-pill .emoji {
            font-size: 16px;
            animation: foodWiggle 1.5s ease-in-out infinite;
        }

        @keyframes foodWiggle {
            0%, 100% { transform: rotate(0deg); }
            25% { transform: rotate(-5deg); }
            75% { transform: rotate(5deg); }
        }

        /* Different lunch colors based on food type */
        .lunch-pill.pizza { background: linear-gradient(135deg, #FFCDD2, #EF5350); color: #B71C1C; border-color: #E53935; }
        .lunch-pill.chicken { background: linear-gradient(135deg, #FFE0B2, #FFB74D); color: #E65100; border-color: #FF9800; }
        .lunch-pill.taco { background: linear-gradient(135deg, #C8E6C9, #81C784); color: #1B5E20; border-color: #4CAF50; }
        .lunch-pill.pasta { background: linear-gradient(135deg, #FFECB3, #FFD54F); color: #F57F17; border-color: #FFC107; }
        .lunch-pill.burger { background: linear-gradient(135deg, #D7CCC8, #A1887F); color: #3E2723; border-color: #795548; }

        /* School Meals Container - shows breakfast, lunch, snack together */
        .school-meals {
            display: flex;
            flex-direction: column;
            gap: 4px;
            margin-top: 6px;
        }

        /* Breakfast pill - morning sunshine colors */
        .breakfast-pill {
            padding: 4px 8px;
            background: linear-gradient(135deg, #E3F2FD, #90CAF9);
            border-radius: 12px;
            font-size: 10px;
            font-weight: 600;
            color: #1565C0;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            border: 1px solid #42A5F5;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }

        .breakfast-pill .emoji {
            font-size: 12px;
        }

        /* Snack pill - fun purple/pink colors */
        .snack-pill {
            padding: 4px 8px;
            background: linear-gradient(135deg, #F3E5F5, #CE93D8);
            border-radius: 12px;
            font-size: 10px;
            font-weight: 600;
            color: #7B1FA2;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            border: 1px solid #AB47BC;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }

        .snack-pill .emoji {
            font-size: 12px;
        }

        /* Make lunch pill smaller to fit with breakfast/snack */
        .school-meals .lunch-pill {
            padding: 4px 8px;
            font-size: 10px;
            margin-top: 0;
            border-radius: 12px;
            border-width: 1px;
            border-style: solid;
            animation: none;
        }

        .school-meals .lunch-pill .emoji {
            font-size: 12px;
            animation: none;
        }

        /* ========== SMART CALENDAR SIZING ========== */
        /* Past days small & grayscale, future days big & colorful, today biggest */

        /* ALL PAST DAYS - small, gray, faded */
        .calendar-day.distant-past,
        .calendar-day.past-week,
        .calendar-day.recent-past,
        .calendar-day.yesterday {
            min-height: 45px;
            padding: 3px;
            background: #F5F5F5;
        }
        .calendar-day.distant-past .day-events,
        .calendar-day.past-week .day-events,
        .calendar-day.recent-past .day-events,
        .calendar-day.yesterday .day-events {
            filter: grayscale(100%);
            opacity: 0.6;
        }
        .calendar-day.distant-past .day-events .event-pill,
        .calendar-day.distant-past .day-events .holiday-pill,
        .calendar-day.past-week .day-events .event-pill,
        .calendar-day.past-week .day-events .holiday-pill,
        .calendar-day.recent-past .day-events .event-pill,
        .calendar-day.recent-past .day-events .holiday-pill,
        .calendar-day.yesterday .day-events .event-pill,
        .calendar-day.yesterday .day-events .holiday-pill {
            font-size: 8px;
            padding: 2px 4px;
            background: #DDD !important;
            color: #666 !important;
        }
        .calendar-day.distant-past .day-num,
        .calendar-day.past-week .day-num,
        .calendar-day.recent-past .day-num,
        .calendar-day.yesterday .day-num {
            font-size: 11px;
            color: #999;
            width: 20px;
            height: 20px;
        }
        /* Hide school meals in past to keep rows short */
        .calendar-day.distant-past .school-meals,
        .calendar-day.past-week .school-meals,
        .calendar-day.recent-past .school-meals,
        .calendar-day.yesterday .school-meals {
            display: none;
        }

        /* TODAY - BIGGEST with highlight */
        .calendar-day.today {
            min-height: 160px;
            padding: 8px;
            background: linear-gradient(135deg, #FFF8E1, #FFECB3) !important;
            box-shadow: inset 0 0 0 4px var(--accent-orange), 0 6px 20px rgba(216, 67, 21, 0.25) !important;
        }
        .calendar-day.today .day-num {
            font-size: 22px;
            font-weight: 700;
            background: var(--accent-orange);
            color: white;
            width: 40px;
            height: 40px;
        }

        /* TOMORROW - second biggest */
        .calendar-day.tomorrow {
            min-height: 140px;
            padding: 7px;
            background: linear-gradient(135deg, #FFF3E0, #FFE0B2);
            box-shadow: inset 0 0 0 2px #FF9800;
        }
        .calendar-day.tomorrow .day-num { font-size: 18px; font-weight: 600; color: #E65100; width: 34px; height: 34px; }

        /* NEAR FUTURE CLOSE (2-3 days) */
        .calendar-day.near-future-close {
            min-height: 120px;
            padding: 6px;
            background: #FFFDE7;
        }
        .calendar-day.near-future-close .day-num { font-size: 16px; width: 30px; height: 30px; }

        /* NEAR FUTURE (4-7 days) */
        .calendar-day.near-future {
            min-height: 100px;
            padding: 6px;
        }
        .calendar-day.near-future .day-num { font-size: 15px; width: 28px; height: 28px; }

        /* FAR FUTURE (8-14 days) */
        .calendar-day.far-future {
            min-height: 85px;
            padding: 5px;
        }
        .calendar-day.far-future .day-num { font-size: 14px; width: 26px; height: 26px; }

        /* DISTANT FUTURE (more than 14 days) */
        .calendar-day.distant-future {
            min-height: 70px;
            padding: 5px;
        }
        .calendar-day.distant-future .day-num { font-size: 13px; width: 24px; height: 24px; }

        /* Today's chore columns */
        .today-chores-container {
            display: none;
        }

        .chore-column {
            flex: 1;
            background: rgba(255,255,255,0.8);
            border-radius: 8px;
            padding: 8px;
            border: 1px solid rgba(0,0,0,0.1);
        }

        .chore-column-header {
            font-size: 11px;
            font-weight: 700;
            text-align: center;
            padding: 4px;
            border-radius: 4px;
            margin-bottom: 6px;
        }

        .chore-column.liv .chore-column-header {
            background: var(--liv);
            color: white;
        }

        .chore-column.jane .chore-column-header {
            background: var(--jane);
            color: white;
        }

        .chore-item {
            display: flex;
            align-items: center;
            gap: 4px;
            font-size: 10px;
            padding: 4px;
            border-radius: 4px;
            margin-bottom: 3px;
            background: white;
            cursor: pointer;
            transition: all 0.2s;
        }

        .chore-item:hover {
            background: #E8F5E9;
        }

        .chore-item.done {
            background: #C8E6C9;
            text-decoration: line-through;
            opacity: 0.7;
        }

        .chore-checkbox {
            width: 14px;
            height: 14px;
            border: 2px solid #ccc;
            border-radius: 3px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
            flex-shrink: 0;
        }

        .chore-item.done .chore-checkbox {
            background: #4CAF50;
            border-color: #4CAF50;
            color: white;
        }

        /* Reward animation */
        @keyframes celebrateReward {
            0% { transform: scale(1); }
            25% { transform: scale(1.3) rotate(-5deg); }
            50% { transform: scale(1.5) rotate(5deg); }
            75% { transform: scale(1.3) rotate(-5deg); }
            100% { transform: scale(1); }
        }

        .reward-animation {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 80px;
            z-index: 9999;
            animation: celebrateReward 0.8s ease-out;
            pointer-events: none;
        }

        /* Near future (next 9 days) - large (second biggest) */
        .calendar-day.near-future {
            min-height: 100px;
        }

        /* Far future (after 9 days) - medium (bigger than past, smaller than near) */
        .calendar-day.far-future {
            min-height: 65px;
        }

        .calendar-day.far-future .day-events .event-pill,
        .calendar-day.far-future .day-events .holiday-pill {
            font-size: 11px;
            padding: 3px 6px;
        }

        /* 4-Day Preview Section */
        .preview-section {
            margin-bottom: 20px;
        }

        .preview-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
        }

        .preview-title {
            font-size: 18px;
            font-weight: 600;
            color: var(--text-primary);
        }

        .preview-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
        }

        .preview-day {
            background: linear-gradient(145deg, rgba(255,255,255,0.95), rgba(248,250,252,0.9));
            border-radius: 16px;
            padding: 12px;
            min-height: 100px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            border: 1px solid rgba(0,0,0,0.05);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .preview-day:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(0,0,0,0.12);
        }

        .preview-day.today {
            background: linear-gradient(145deg, #FFF3E0, #FFE0B2);
            border: 2px solid var(--accent-orange);
        }

        .preview-day.tomorrow {
            background: linear-gradient(145deg, #E8F5E9, #C8E6C9);
            border: 2px solid #81C784;
        }

        .preview-day-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }

        .preview-day-name {
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #666;
        }

        .preview-day-num {
            font-size: 22px;
            font-weight: 700;
            color: var(--text-primary);
        }

        .preview-day.today .preview-day-num {
            color: var(--accent-orange);
        }

        .preview-day.tomorrow .preview-day-num {
            color: #4CAF50;
        }

        .preview-events {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .preview-event {
            font-size: 11px;
            padding: 4px 8px;
            border-radius: 8px;
            background: rgba(99, 102, 241, 0.15);
            color: #4338CA;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .preview-event.holiday {
            background: linear-gradient(135deg, #FEE2E2, #FECACA);
            color: #DC2626;
        }

        .preview-event.birthday {
            background: linear-gradient(135deg, #FCE7F3, #FBCFE8);
            color: #BE185D;
        }

        @media (max-width: 768px) {
            .preview-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        /* Holiday-specific colors */
        .holiday-pill.christmas {
            background: linear-gradient(135deg, #C62828, #2E7D32) !important;
            color: white !important;
            border-color: #1B5E20 !important;
        }

        .holiday-pill.christmas-eve {
            background: linear-gradient(135deg, #2E7D32, #C62828) !important;
            color: white !important;
            border-color: #C62828 !important;
        }

        .holiday-pill.winter-solstice {
            background: linear-gradient(135deg, #E3F2FD, #B3E5FC) !important;
            color: #0277BD !important;
            border-color: #4FC3F7 !important;
        }

        .holiday-pill.new-years {
            background: linear-gradient(135deg, #FFD700, #FFA000) !important;
            color: #333 !important;
            border-color: #FFB300 !important;
        }

        .holiday-pill.valentines {
            background: linear-gradient(135deg, #F8BBD9, #F48FB1) !important;
            color: #880E4F !important;
            border-color: #EC407A !important;
        }

        .holiday-pill.halloween {
            background: linear-gradient(135deg, #FF9800, #E65100) !important;
            color: white !important;
            border-color: #BF360C !important;
        }

        .holiday-pill.thanksgiving {
            background: linear-gradient(135deg, #8D6E63, #D84315) !important;
            color: white !important;
            border-color: #BF360C !important;
        }

        .holiday-pill.easter {
            background: linear-gradient(135deg, #E1BEE7, #CE93D8) !important;
            color: #4A148C !important;
            border-color: #9C27B0 !important;
        }

        .holiday-pill.stpatricks {
            background: linear-gradient(135deg, #4CAF50, #2E7D32) !important;
            color: white !important;
            border-color: #1B5E20 !important;
        }

        .holiday-pill.july4th {
            background: linear-gradient(135deg, #1565C0, #C62828) !important;
            color: white !important;
            border-color: #0D47A1 !important;
        }

        .holiday-pill.hanukkah {
            background: linear-gradient(135deg, #1976D2, #64B5F6) !important;
            color: white !important;
            border-color: #1565C0 !important;
        }

        .holiday-pill.kwanzaa {
            background: linear-gradient(135deg, #D32F2F, #388E3C) !important;
            color: white !important;
            border-color: #1B5E20 !important;
        }

        .holiday-pill.mothers-day, .holiday-pill.fathers-day {
            background: linear-gradient(135deg, #F8BBD9, #E1BEE7) !important;
            color: #880E4F !important;
            border-color: #EC407A !important;
        }

        .holiday-pill.memorial-day, .holiday-pill.veterans-day, .holiday-pill.labor-day {
            background: linear-gradient(135deg, #1565C0, #C62828) !important;
            color: white !important;
            border-color: #0D47A1 !important;
        }

        /* Voice Command Bar - appears in each section */
        .voice-command-bar {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 6px 12px;
            background: linear-gradient(135deg, #FFFBF5, #FFF8E1);
            flex-shrink: 0;
            border: 2px solid var(--border-gold);
            border-radius: 50px;
            margin-bottom: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        }

        .voice-command-bar .mic-btn {
            width: 42px;
            height: 42px;
            border-radius: 50%;
            border: 2px solid var(--accent-orange);
            background: linear-gradient(135deg, var(--accent-orange), #E55D3A);
            color: white;
            font-size: 20px;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            box-shadow: 0 3px 10px rgba(216, 67, 21, 0.3);
        }

        .voice-command-bar .mic-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 4px 15px rgba(216, 67, 21, 0.4);
        }

        .voice-command-bar .mic-btn.recording {
            background: linear-gradient(135deg, #E53935, #C62828);
            animation: pulse 1s ease-in-out infinite;
        }

        .voice-command-bar .voice-input-area {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .voice-command-bar .voice-input {
            width: 100%;
            padding: 8px 12px;
            border: 1px solid var(--border-light);
            border-radius: 20px;
            font-size: 14px;
            background: white;
            outline: none;
            transition: border-color 0.2s;
        }

        .voice-command-bar .voice-input:focus {
            border-color: var(--accent-orange);
        }

        .voice-command-bar .voice-input::placeholder {
            color: #aaa;
            font-style: italic;
        }

        .voice-command-bar .voice-status-text {
            font-size: 11px;
            color: var(--text-muted);
            padding-left: 12px;
            min-height: 14px;
        }

        .voice-command-bar .voice-status-text.success {
            color: #2E7D32;
        }

        .voice-command-bar .voice-status-text.error {
            color: #C62828;
        }

        .voice-command-bar .voice-status-text.listening {
            color: var(--accent-orange);
            animation: pulse 1s ease-in-out infinite;
        }

        .voice-command-bar .voice-submit-btn {
            padding: 8px 16px;
            background: linear-gradient(135deg, #4CAF50, #388E3C);
            color: white;
            border: none;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3);
        }

        .voice-command-bar .voice-submit-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 12px rgba(76, 175, 80, 0.4);
        }

        .voice-status {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(0, 0, 0, 0.9);
            color: white;
            padding: 30px 50px;
            border-radius: 20px;
            font-size: 18px;
            z-index: 9999;
            text-align: center;
            display: none;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        }

        .voice-status.show {
            display: block;
        }

        .voice-status .listening-icon {
            font-size: 50px;
            margin-bottom: 15px;
            animation: pulse 1s ease-in-out infinite;
        }

        .voice-status .status-text {
            margin-bottom: 10px;
        }

        .voice-status .command-preview {
            font-size: 14px;
            color: #aaa;
            margin-top: 10px;
        }

        /* ========== RESPONSIVE SIZING ========== */

        /* Medium screens (1000-1199px) */
        @media (min-width: 1000px) and (max-width: 1199px) {
            :root { --sidebar-width: 200px; }
        }

        /* Tablet (768-999px) */
        @media (min-width: 768px) and (max-width: 999px) {
            :root { --sidebar-width: 180px; }
            .day-header-cell { font-size: 11px; padding: 8px 4px; }
        }

        /* Small tablet / Phone landscape (600-767px) */
        @media (min-width: 600px) and (max-width: 767px) {
            .sidebar { display: none; }
            .main-content { left: 0; padding: 10px; }
            .day-header-cell { font-size: 10px; padding: 6px 3px; letter-spacing: 0; }
        }

        /* Phone (under 600px) */
        @media (max-width: 599px) {
            .sidebar { display: none; }
            .main-content { left: 0; padding: 8px; }
            .day-header-cell { font-size: 9px; padding: 5px 2px; }
            .year-title { font-size: 20px; }
            .month-title { font-size: 16px; }
        }
        /* ========== DECEMBER WINTER THEME ========== */
        .december-theme {
            background: linear-gradient(180deg, #87CEEB 0%, #B0D4E8 30%, #D4E8F2 100%) !important;
        }

        .december-theme .sidebar {
            background: rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-right: 2px solid rgba(255, 255, 255, 0.3);
        }

        .december-theme .calendar-grid {
            background: rgba(255, 255, 255, 0.85);
            border-color: #C9A66B;
        }

        .december-theme .expanded-month {
            background: rgba(255, 255, 255, 0.9);
            border-color: #C9A66B;
        }

        .december-theme .year-header {
            background: transparent;
        }

        .december-theme .month-title {
            color: #1a4a6e;
        }

        /* Snowfall animation */
        .snowfall {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
            overflow: hidden;
        }

        .snowflake {
            position: absolute;
            top: -20px;
            color: white;
            font-size: 1em;
            text-shadow: 0 0 5px rgba(255,255,255,0.8);
            animation: snowfall linear infinite;
            opacity: 0.8;
        }

        @keyframes snowfall {
            0% {
                transform: translateY(-20px) rotate(0deg);
            }
            100% {
                transform: translateY(100vh) rotate(360deg);
            }
        }

        /* Christmas decorations */
        .december-decorations {
            position: fixed;
            pointer-events: none;
            z-index: 2;
        }

        .decoration-top-left {
            top: 10px;
            left: 10px;
            font-size: 40px;
            animation: gentle-bounce 3s ease-in-out infinite;
        }

        .decoration-top-right {
            top: 10px;
            right: 20px;
            font-size: 35px;
        }

        .decoration-tree {
            bottom: 20px;
            right: 20px;
            font-size: 80px;
            animation: gentle-sway 4s ease-in-out infinite;
        }

        @keyframes gentle-bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        @keyframes gentle-sway {
            0%, 100% { transform: rotate(-2deg); }
            50% { transform: rotate(2deg); }
        }

        /* Winter month header decoration */
        .december-theme .expanded-header::before {
            content: '🎅 ❄️ ';
        }

        .december-theme .expanded-header::after {
            content: ' ❄️ 🎄';
        }

        /* Frosted day cells for past in December */
        .december-theme .calendar-day.distant-past,
        .december-theme .calendar-day.past-week,
        .december-theme .calendar-day.recent-past,
        .december-theme .calendar-day.yesterday {
            background: rgba(200, 220, 240, 0.5);
        }

        /* Warm glow for future days in December */
        .december-theme .calendar-day.tomorrow,
        .december-theme .calendar-day.near-future-close {
            background: linear-gradient(135deg, #FFF8DC, #FFE4B5);
        }

        /* Screensaver */
        .screensaver {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background: black;
            z-index: 5000;
            opacity: 0;
            pointer-events: none;
            transition: opacity 1s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }
        .screensaver.active {
            opacity: 1;
            pointer-events: all;
        }
        .screensaver video {
            width: 100%; height: 100%;
            object-fit: cover;
            transition: opacity 1.5s ease-in-out, filter 1s ease;
        }
        .screensaver video.fade-out {
            opacity: 0;
        }
        .screensaver video.pixelate {
            filter: blur(8px) saturate(1.2);
        }
        /* Pixelation overlay for transitions */
        .screensaver .pixel-overlay {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: transparent;
            pointer-events: none;
            z-index: 5001;
            opacity: 0;
            transition: opacity 0.8s ease;
        }
        .screensaver .pixel-overlay.active {
            opacity: 1;
            background:
                repeating-linear-gradient(
                    0deg,
                    rgba(0,0,0,0.15) 0px,
                    rgba(0,0,0,0.15) 3px,
                    transparent 3px,
                    transparent 6px
                ),
                repeating-linear-gradient(
                    90deg,
                    rgba(0,0,0,0.15) 0px,
                    rgba(0,0,0,0.15) 3px,
                    transparent 3px,
                    transparent 6px
                );
        }
    </style>
</head>
<body>
    <!-- Screensaver -->
    <div class="screensaver" id="screensaver">
        <video id="screensaverVideo" muted playsinline>
            <source src="" type="video/mp4">
        </video>
        <div class="pixel-overlay" id="pixelOverlay"></div>
    </div>
    <div class="app-container">
        <!-- Left Sidebar -->
        <div class="sidebar">
            <div class="sidebar-header">
                <div class="current-time" id="currentTime">12:00</div>
                <div class="current-date" id="currentDate">Monday, Dec 9</div>
                <div class="family-name">Family Family</div>
            </div>

            <!-- Jump to Month -->
            <div class="month-nav">
                <div class="month-nav-title">Jump to Month</div>
                <div class="month-grid" id="monthNav"></div>
            </div>

            <div class="today-section">
                <div class="section-title">Today</div>
                <div id="todayEvents"></div>
            </div>

            <div class="weather-widget">
                <div class="weather-temp" id="weatherTemp">--°</div>
                <div class="weather-desc" id="weatherDesc">Loading...</div>
            </div>

            <!-- Kids Rewards Widget -->
            <div class="rewards-widget">
                <div class="rewards-title">⭐ Star Rewards ⭐</div>
                <div class="rewards-kids">
                    <div class="reward-kid liv" onclick="showRewardsModal('liv')">
                        <div class="kid-avatar">👧</div>
                        <div class="kid-name">Emma</div>
                        <div class="kid-points" id="livPoints">0</div>
                        <div class="kid-stars">⭐</div>
                    </div>
                    <div class="reward-kid jane" onclick="showRewardsModal('jane')">
                        <div class="kid-avatar">👧</div>
                        <div class="kid-name">Sophie</div>
                        <div class="kid-points" id="janePoints">0</div>
                        <div class="kid-stars">⭐</div>
                    </div>
                </div>
                <div class="prizes-preview">
                    <div class="prize-tier">🎁 10 pts: Treat</div>
                    <div class="prize-tier">🎮 25 pts: Game Time</div>
                    <div class="prize-tier">🎬 50 pts: Movie Night</div>
                    <div class="prize-tier">🎢 100 pts: Special Outing</div>
                </div>
            </div>

        </div>

        <!-- Main Content Area -->
        <div class="main-content">
            <!-- Global Header - Shows on all panels -->
            <div class="year-header">
                <!-- Left: Time, Date, Weather -->
                <div class="header-info">
                    <div class="header-time-date">
                        <div class="header-time" id="headerTime">12:00</div>
                        <div class="header-date" id="headerDate">Mon, Dec 9</div>
                    </div>
                    <div class="header-weather" id="headerWeather">
                        <span class="header-weather-icon" id="headerWeatherIcon">☀️</span>
                        <span class="header-weather-temp" id="headerWeatherTemp">--°</span>
                    </div>
                </div>

                <div class="year-nav" id="calendarNav">
                    <button class="year-arrow" onclick="changeYear(-1)">◀</button>
                    <h1 class="year-title" id="yearTitle">2025</h1>
                    <button class="year-arrow" onclick="changeYear(1)">▶</button>
                </div>
                <h1 class="page-title" id="pageTitle" style="display:none;"></h1>

                <!-- Month Skip Dropdown -->
                <div class="month-select-wrapper" id="monthSelectWrapper">
                    <select class="month-select" id="monthSelect" onchange="jumpToMonth(this.value)">
                        <option value="0">Jan</option>
                        <option value="1">Feb</option>
                        <option value="2">Mar</option>
                        <option value="3">Apr</option>
                        <option value="4">May</option>
                        <option value="5">Jun</option>
                        <option value="6">Jul</option>
                        <option value="7">Aug</option>
                        <option value="8">Sep</option>
                        <option value="9">Oct</option>
                        <option value="10">Nov</option>
                        <option value="11">Dec</option>
                    </select>
                </div>

                <div class="header-actions" id="headerActions">
                    <button class="action-pill" id="navCalendar" onclick="showPanel('calendar')" style="display:none;">📅 Calendar</button>
                    <button class="action-pill" id="navMeals" onclick="showPanel('meals')">🍽️ Meals</button>
                    <button class="action-pill" id="navEvent" onclick="showAddEvent()">➕ Event</button>
                    <button class="action-pill" id="navShopping" onclick="showPanel('shopping')">🛒 Shop</button>
                    <button class="action-pill kid-btn liv" id="navLiv" onclick="showKidPanel('liv')">Liv</button>
                    <button class="action-pill kid-btn jane" id="navJane" onclick="showKidPanel('jane')">Jane</button>
                    <button class="action-pill ocean" id="navOcean" onclick="startScreensaver()">🌊 Ocean</button>
                </div>
                <button class="today-btn" id="todayBtn" onclick="scrollToToday()">Today</button>
            </div>

            <!-- Calendar Panel (Default) -->
            <div id="calendarPanel" class="panel active">
                <!-- Smart Voice Command Bar -->
                <div class="voice-command-bar" id="calendarVoiceBar">
                    <button class="mic-btn" id="calendarMic" onclick="startSmartVoice(this)">🎤</button>
                    <div class="voice-input-area">
                        <input type="text" class="voice-input" id="calendarVoiceInput" placeholder='Say anything: events, chores, shopping, meals...' onkeypress="if(event.key==='Enter')processSmartTextCommand(this.value)">
                        <div class="voice-status-text" id="calendarVoiceStatus"></div>
                    </div>
                    <button class="voice-submit-btn" onclick="processSmartTextCommand(document.getElementById('calendarVoiceInput').value)">Go</button>
                </div>

                <div id="yearCalendar"></div>
            </div>

            <!-- Shopping Panel -->
            <div id="shoppingPanel" class="panel">
                <div style="display:flex; gap:10px; margin-bottom:20px; flex-shrink:0;">
                    <div style="position:relative; flex:1;">
                        <input type="text" id="newItem" placeholder="Add item..." onkeypress="if(event.key==='Enter')addShoppingItem()" style="padding-right: 50px; margin-bottom:0;">
                        <button onclick="startVoiceCommand('shopping', this)" style="position:absolute; right:5px; top:50%; transform:translateY(-50%); width:36px; height:36px; border-radius:50%; background:linear-gradient(135deg, var(--accent-orange), #E55D3A); border:2px solid var(--accent-orange); font-size:16px; cursor:pointer; color:white; display:flex; align-items:center; justify-content:center;">🎤</button>
                    </div>
                    <button class="btn-primary" style="width:auto; background:var(--neon-pink);" onclick="addShoppingItem()">+</button>
                </div>
                <div id="shoppingList"></div>
            </div>

            <!-- Meals Panel -->
            <div id="mealsPanel" class="panel">
                <div class="meal-week" id="mealWeek"></div>
            </div>

            <!-- Kids Panel -->
            <div id="kidsPanel" class="panel">

                <div class="kids-header">
                    <div class="kid-card liv selected" id="livCard" onclick="selectKid('liv')">
                        <span class="emoji">👧</span>
                        <div class="name">Emma</div>
                        <div class="points" id="livPoints">0 ⭐</div>
                    </div>
                    <div class="kid-card jane" id="janeCard" onclick="selectKid('jane')">
                        <span class="emoji">👧</span>
                        <div class="name">Sophie</div>
                        <div class="points" id="janePoints">0 ⭐</div>
                    </div>
                </div>

                <div class="section-title" style="margin-bottom:12px">Today's Chores</div>
                <div class="chore-grid" id="choreGrid"></div>
            </div>
        </div>
    </div>

    <!-- Event Modal -->
    <div class="modal" id="eventModal">
        <div class="modal-content">
            <h2>Add Event</h2>
            <div style="position:relative; margin-bottom:15px;">
                 <input type="text" id="eventTitle" placeholder="Event Name" style="margin-bottom:0; padding-right:50px;">
                 <button onclick="startVoiceCommand('calendar', this)" style="position:absolute; right:5px; top:50%; transform:translateY(-50%); width:40px; height:40px; border-radius:50%; background:linear-gradient(135deg, var(--accent-orange), #E55D3A); border:2px solid var(--accent-orange); font-size:18px; cursor:pointer; color:white; display:flex; align-items:center; justify-content:center;">🎤</button>
            </div>
            <input type="date" id="eventDate">
            <input type="time" id="eventTime">
            <div class="modal-btns">
                <button class="btn-secondary" onclick="closeModal('eventModal')">Cancel</button>
                <button class="btn-primary" onclick="saveEvent()">Save</button>
            </div>
        </div>
    </div>

    <!-- Day Detail Modal -->
    <div class="modal" id="dayModal">
        <div class="modal-content day-events-modal">
            <h2 id="dayModalTitle">December 9</h2>
            <div id="dayModalContent"></div>
            <div class="modal-btns">
                <button class="btn-secondary" onclick="closeModal('dayModal')">Close</button>
                <button class="btn-primary" onclick="closeModal('dayModal');showAddEvent()">Add Event</button>
            </div>
        </div>
    </div>

    <!-- Rewards Modal -->
    <div class="modal" id="rewardsModal">
        <div class="modal-content rewards-modal">
            <h2 id="rewardsModalTitle">⭐ Emma's Stars ⭐</h2>
            <div class="rewards-modal-content">
                <div class="points-display">
                    <div class="big-avatar" id="rewardsAvatar">👧</div>
                    <div class="points-value" id="rewardsPoints">0</div>
                    <div class="points-label">Stars</div>
                </div>
                <div class="points-controls">
                    <button class="points-btn add" onclick="addPoints(1)">+1 ⭐</button>
                    <button class="points-btn add" onclick="addPoints(5)">+5 ⭐</button>
                    <button class="points-btn remove" onclick="addPoints(-1)">-1</button>
                </div>
                <div class="prizes-list">
                    <h3>🎁 Prizes Available</h3>
                    <div class="prize-item" data-cost="10">
                        <span class="prize-emoji">🍬</span>
                        <span class="prize-name">Special Treat</span>
                        <span class="prize-cost">10 ⭐</span>
                        <button class="redeem-btn" onclick="redeemPrize(10, 'Special Treat')">Redeem</button>
                    </div>
                    <div class="prize-item" data-cost="25">
                        <span class="prize-emoji">🎮</span>
                        <span class="prize-name">30 Min Game Time</span>
                        <span class="prize-cost">25 ⭐</span>
                        <button class="redeem-btn" onclick="redeemPrize(25, 'Game Time')">Redeem</button>
                    </div>
                    <div class="prize-item" data-cost="50">
                        <span class="prize-emoji">🎬</span>
                        <span class="prize-name">Movie Night Pick</span>
                        <span class="prize-cost">50 ⭐</span>
                        <button class="redeem-btn" onclick="redeemPrize(50, 'Movie Night')">Redeem</button>
                    </div>
                    <div class="prize-item" data-cost="100">
                        <span class="prize-emoji">🎢</span>
                        <span class="prize-name">Special Outing</span>
                        <span class="prize-cost">100 ⭐</span>
                        <button class="redeem-btn" onclick="redeemPrize(100, 'Special Outing')">Redeem</button>
                    </div>
                </div>
            </div>
            <div class="modal-btns">
                <button class="btn-secondary" onclick="closeModal('rewardsModal')">Close</button>
            </div>
        </div>
    </div>

    <!-- Meal Modal -->
    <div class="modal" id="mealModal">
        <div class="modal-content">
            <h2 id="mealDayTitle">Pick Meal</h2>
            <div id="mealPicker" style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:15px;"></div>
            <div style="position:relative; margin-bottom:15px;">
                <input type="text" id="customMeal" placeholder="Custom meal..." style="margin-bottom:0; padding-right:50px;">
                <button onclick="startVoiceCommand('meals', this)" style="position:absolute; right:5px; top:50%; transform:translateY(-50%); width:40px; height:40px; border-radius:50%; background:linear-gradient(135deg, var(--accent-orange), #E55D3A); border:2px solid var(--accent-orange); font-size:18px; cursor:pointer; color:white; display:flex; align-items:center; justify-content:center;">🎤</button>
            </div>
            <div class="modal-btns">
                <button class="btn-secondary" onclick="closeModal('mealModal')">Cancel</button>
                <button class="btn-primary" onclick="saveCustomMeal()">Save</button>
            </div>
        </div>
    </div>

    <!-- Voice Status Modal -->
    <div class="voice-status" id="voiceStatus">
        <div class="listening-icon">🎤</div>
        <div class="status-text">Listening...</div>
        <div class="command-preview" id="voicePreview">Speak now</div>
    </div>

    <!-- Fia Chat Modal - Premium Glassmorphic Design -->
    <div class="modal" id="fiaModal">
        <div class="modal-content fia-chat-modal">
            <div class="fia-header">
                <div class="fia-avatar">
                    <span class="fia-icon">🤖</span>
                    <span class="fia-pulse"></span>
                </div>
                <div class="fia-title">
                    <h2>Fia</h2>
                    <span class="fia-status">Family Assistant</span>
                </div>
                <button class="fia-close" onclick="closeModal('fiaModal')">✕</button>
            </div>

            <div class="fia-messages" id="fiaMessages">
                <div class="fia-message fia-response">
                    <div class="message-avatar">🤖</div>
                    <div class="message-bubble">
                        Hi! I'm Fia, your family assistant. I can help with the calendar, shopping list, meal planning, and kids' chores. What can I help you with?
                    </div>
                </div>
            </div>

            <div class="fia-input-container">
                <button class="fia-mic-btn" id="fiaChatMic" onclick="toggleFiaMic()">
                    <span class="mic-icon">🎤</span>
                </button>
                <input type="text" id="fiaInput" placeholder="Type or tap mic to speak..." onkeypress="if(event.key==='Enter')sendFiaMessage()">
                <button class="fia-send-btn" onclick="sendFiaMessage()">
                    <span>➤</span>
                </button>
            </div>

            <div class="fia-quick-actions">
                <button onclick="sendQuickFia('What\\'s on the calendar today?')">📅 Today</button>
                <button onclick="sendQuickFia('What\\'s for dinner?')">🍽️ Dinner</button>
                <button onclick="sendQuickFia('What\\'s on the shopping list?')">🛒 Shopping</button>
                <button onclick="sendQuickFia('How are the kids doing with chores?')">⭐ Chores</button>
            </div>
        </div>
    </div>

    <style>
        /* Fia Chat Modal - Premium Design */
        .fia-chat-modal {
            max-width: 500px !important;
            height: 600px !important;
            padding: 0 !important;
            border-radius: 24px !important;
            overflow: hidden;
            display: flex !important;
            flex-direction: column !important;
            background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%) !important;
        }

        .fia-header {
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 20px;
            background: linear-gradient(90deg, rgba(99, 102, 241, 0.3), rgba(168, 85, 247, 0.3));
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }

        .fia-avatar {
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #6366F1, #A855F7);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
        }

        .fia-icon {
            font-size: 26px;
        }

        .fia-pulse {
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            border: 2px solid #6366F1;
            animation: fiaPulse 2s ease-in-out infinite;
        }

        @keyframes fiaPulse {
            0%, 100% { transform: scale(1); opacity: 0.5; }
            50% { transform: scale(1.2); opacity: 0; }
        }

        .fia-title h2 {
            color: white;
            font-size: 20px;
            font-weight: 600;
            margin: 0;
        }

        .fia-status {
            color: rgba(255,255,255,0.6);
            font-size: 12px;
        }

        .fia-close {
            margin-left: auto;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            border: none;
            background: rgba(255,255,255,0.1);
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .fia-close:hover {
            background: rgba(255,255,255,0.2);
        }

        .fia-messages {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .fia-message {
            display: flex;
            gap: 10px;
            max-width: 85%;
        }

        .fia-message.fia-response {
            align-self: flex-start;
        }

        .fia-message.user-message {
            align-self: flex-end;
            flex-direction: row-reverse;
        }

        .message-avatar {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: linear-gradient(135deg, #6366F1, #A855F7);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            flex-shrink: 0;
        }

        .user-message .message-avatar {
            background: linear-gradient(135deg, #F97316, #EA580C);
        }

        .message-bubble {
            padding: 12px 16px;
            border-radius: 18px;
            font-size: 14px;
            line-height: 1.5;
        }

        .fia-response .message-bubble {
            background: rgba(255,255,255,0.1);
            color: white;
            border-bottom-left-radius: 4px;
        }

        .user-message .message-bubble {
            background: linear-gradient(135deg, #F97316, #EA580C);
            color: white;
            border-bottom-right-radius: 4px;
        }

        .fia-input-container {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 15px 20px;
            background: rgba(0,0,0,0.3);
            border-top: 1px solid rgba(255,255,255,0.1);
        }

        .fia-mic-btn {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            border: none;
            background: linear-gradient(135deg, #6366F1, #A855F7);
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
        }

        .fia-mic-btn:hover {
            transform: scale(1.1);
        }

        .fia-mic-btn.recording {
            background: linear-gradient(135deg, #EF4444, #DC2626);
            animation: pulse 1s ease-in-out infinite;
        }

        .fia-mic-btn .mic-icon {
            font-size: 22px;
        }

        .fia-input-container input {
            flex: 1;
            padding: 14px 18px;
            border-radius: 25px;
            border: 2px solid rgba(255,255,255,0.1);
            background: rgba(255,255,255,0.05);
            color: white;
            font-size: 14px;
        }

        .fia-input-container input::placeholder {
            color: rgba(255,255,255,0.4);
        }

        .fia-input-container input:focus {
            outline: none;
            border-color: #6366F1;
            background: rgba(255,255,255,0.1);
        }

        .fia-send-btn {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            border: none;
            background: linear-gradient(135deg, #F97316, #EA580C);
            color: white;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            box-shadow: 0 4px 15px rgba(249, 115, 22, 0.4);
        }

        .fia-send-btn:hover {
            transform: scale(1.1);
        }

        .fia-quick-actions {
            display: flex;
            gap: 8px;
            padding: 12px 20px 20px;
            background: rgba(0,0,0,0.3);
            overflow-x: auto;
        }

        .fia-quick-actions button {
            padding: 8px 14px;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.2);
            background: rgba(255,255,255,0.05);
            color: white;
            font-size: 12px;
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.2s;
        }

        .fia-quick-actions button:hover {
            background: rgba(255,255,255,0.15);
            border-color: rgba(255,255,255,0.4);
        }
    </style>

    <script>
        // State
        let selectedKid = 'liv';
        let selectedPerson = 'family';
        let selectedMealDay = null;
        let clickedDate = null;
        let currentYear = new Date().getFullYear(); // Current viewing year (2025, 2026, etc.)
        let expandedMonth = 11; // December (0-indexed) - currently expanded month
        let data = {
            calendar: { events: [] },
            chores: { chores: [], completed: [] },
            rewards: { points: {}, rewards: [] },
            meals: { thisWeek: {}, favorites: [] },
            shopping: { items: [] },
            family: {},
            holidays: {},
            lunches: {}
        };

        const monthNames = ['January', 'February', 'March', 'April', 'May', 'June',
                           'July', 'August', 'September', 'October', 'November', 'December'];
        const monthAbbrev = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        const dayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

        // Get holiday CSS class for colorful styling
        function getHolidayClass(holidayName) {
            const name = holidayName.toLowerCase();
            if (name.includes('christmas day') || name.includes('christmas')) return 'christmas';
            if (name.includes('christmas eve')) return 'christmas-eve';
            if (name.includes('winter solstice')) return 'winter-solstice';
            if (name.includes('new year')) return 'new-years';
            if (name.includes('valentine')) return 'valentines';
            if (name.includes('halloween')) return 'halloween';
            if (name.includes('thanksgiving')) return 'thanksgiving';
            if (name.includes('easter')) return 'easter';
            if (name.includes('patrick')) return 'stpatricks';
            if (name.includes('independence') || name.includes('july 4') || name.includes('4th')) return 'july4th';
            if (name.includes('hanukkah')) return 'hanukkah';
            if (name.includes('kwanzaa')) return 'kwanzaa';
            if (name.includes('mother')) return 'mothers-day';
            if (name.includes('father')) return 'fathers-day';
            if (name.includes('memorial')) return 'memorial-day';
            if (name.includes('veteran')) return 'veterans-day';
            if (name.includes('labor')) return 'labor-day';
            return '';
        }

        // Show reward animation when chore is completed
        function showRewardAnimation() {
            const emojis = ['⭐', '🎉', '🌟', '✨', '🎊', '👏', '💪', '🏆'];
            const emoji = emojis[Math.floor(Math.random() * emojis.length)];
            const el = document.createElement('div');
            el.className = 'reward-animation';
            el.textContent = emoji;
            document.body.appendChild(el);
            setTimeout(() => el.remove(), 800);
        }

        // Render chores in today's calendar cell
        function renderTodayChores() {
            const today = new Date().toISOString().split('T')[0];
            const livContainer = document.getElementById('livChores');
            const janeContainer = document.getElementById('janeChores');
            if (!livContainer || !janeContainer) return;

            // Get completed chores for today
            const completedToday = data.chores.completed.filter(c => c.date === today);

            // Render Emma's chores
            const livChores = data.chores.chores.filter(c => c.assignedTo.includes('liv'));
            const livCompletedIds = completedToday.filter(c => c.person === 'liv').map(c => c.choreId);
            livContainer.innerHTML = livChores.slice(0, 5).map(c => `
                <div class="chore-item ${livCompletedIds.includes(c.id) ? 'done' : ''}"
                     onclick="event.stopPropagation(); toggleCalendarChore(${c.id}, 'liv')">
                    <div class="chore-checkbox">${livCompletedIds.includes(c.id) ? '✓' : ''}</div>
                    <span>${c.icon} ${c.name.split(' ')[0]}</span>
                </div>
            `).join('');

            // Render Sophie's chores
            const janeChores = data.chores.chores.filter(c => c.assignedTo.includes('jane'));
            const janeCompletedIds = completedToday.filter(c => c.person === 'jane').map(c => c.choreId);
            janeContainer.innerHTML = janeChores.slice(0, 5).map(c => `
                <div class="chore-item ${janeCompletedIds.includes(c.id) ? 'done' : ''}"
                     onclick="event.stopPropagation(); toggleCalendarChore(${c.id}, 'jane')">
                    <div class="chore-checkbox">${janeCompletedIds.includes(c.id) ? '✓' : ''}</div>
                    <span>${c.icon} ${c.name.split(' ')[0]}</span>
                </div>
            `).join('');
        }

        // Toggle chore from calendar view
        async function toggleCalendarChore(choreId, person) {
            const today = new Date().toISOString().split('T')[0];
            const isCompleted = data.chores.completed.some(c =>
                c.choreId === choreId && c.person === person && c.date === today
            );

            const endpoint = isCompleted ? '/api/chores/uncomplete' : '/api/chores/complete';
            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ choreId, person })
            });

            const result = await res.json();
            if (result.success) {
                if (!isCompleted) {
                    const chore = data.chores.chores.find(c => c.id === choreId);
                    data.rewards.points[person] = (data.rewards.points[person] || 0) + (chore?.points || 0);
                    data.chores.completed.push({ choreId, person, date: today, points: chore?.points || 0 });
                    showRewardAnimation();
                } else {
                    const chore = data.chores.chores.find(c => c.id === choreId);
                    data.rewards.points[person] -= chore?.points || 0;
                    data.chores.completed = data.chores.completed.filter(c =>
                        !(c.choreId === choreId && c.person === person && c.date === today)
                    );
                }
                renderTodayChores();
                renderKids();
            }
        }

        // Initialize
        // Force layout to fit viewport
        function fitToScreen() {
            const vh = window.innerHeight;
            document.documentElement.style.setProperty('--vh', vh + 'px');
            document.body.style.height = vh + 'px';

            const appContainer = document.querySelector('.app-container');
            if (appContainer) appContainer.style.height = vh + 'px';

            const mainContent = document.querySelector('.main-content');
            if (mainContent) mainContent.style.height = vh + 'px';

            // Calculate exact calendar height
            const yearHeader = document.querySelector('.year-header');
            const voiceBar = document.querySelector('.voice-command-bar');
            const expandedHeader = document.querySelector('.expanded-header');
            const calendarGrid = document.querySelector('.calendar-grid');

            if (calendarGrid && mainContent) {
                const headerH = yearHeader ? yearHeader.offsetHeight : 0;
                const voiceH = voiceBar ? voiceBar.offsetHeight : 0;
                const expHeaderH = expandedHeader ? expandedHeader.offsetHeight : 0;
                const padding = 40; // padding/margins
                const monthBorder = 24; // expanded-month padding + border

                const availableHeight = vh - headerH - voiceH - expHeaderH - padding - monthBorder;
                const dayHeaderH = 35; // approximate day header row height
                const rowHeight = Math.floor((availableHeight - dayHeaderH) / 6);

                calendarGrid.style.height = availableHeight + 'px';
                calendarGrid.style.maxHeight = availableHeight + 'px';

                // Set each calendar row to exact height
                const days = calendarGrid.querySelectorAll('.calendar-day');
                days.forEach(day => {
                    day.style.height = rowHeight + 'px';
                    day.style.maxHeight = rowHeight + 'px';
                });
            }
        }

        window.addEventListener('resize', fitToScreen);
        window.addEventListener('orientationchange', () => setTimeout(fitToScreen, 100));
        window.addEventListener('load', () => setTimeout(fitToScreen, 200));

        async function init() {
            fitToScreen();
            updateClock();
            setInterval(updateClock, 1000);

            const endpoints = ['calendar', 'chores', 'rewards', 'meals', 'shopping', 'family', 'holidays', 'lunches', 'breakfast', 'snacks'];
            const results = await Promise.all(endpoints.map(e => fetch(`/api/${e}`).then(r => r.json())));
            endpoints.forEach((e, i) => data[e] = results[i]);

            // Set expanded month to current month
            expandedMonth = new Date().getMonth();

            // Apply seasonal theme
            applySeasonalTheme();

            renderMonthNav();
            renderCalendar();
            fitToScreen();
            renderTodayChores(); // Render chores in today's card
            renderTodayEvents();
            renderShopping();
            renderMeals();
            renderKids();
            fetchWeather();
        }

        // Seasonal themes based on month
        function applySeasonalTheme() {
            const month = new Date().getMonth();
            const body = document.body;

            // Remove any existing theme classes
            body.classList.remove('december-theme', 'october-theme', 'february-theme');

            // December - Winter/Christmas theme
            if (month === 11) {
                body.classList.add('december-theme');
                createSnowfall();
                addDecemberDecorations();
            }
        }

        function createSnowfall() {
            // Create snowfall container
            let snowfall = document.querySelector('.snowfall');
            if (!snowfall) {
                snowfall = document.createElement('div');
                snowfall.className = 'snowfall';
                document.body.appendChild(snowfall);
            }

            // Create snowflakes
            const snowflakes = ['❄', '❅', '❆', '✻', '✼', '❋'];
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

        function addDecemberDecorations() {
            // Add Christmas tree to bottom right
            if (!document.querySelector('.decoration-tree')) {
                const tree = document.createElement('div');
                tree.className = 'december-decorations decoration-tree';
                tree.textContent = '🎄';
                document.body.appendChild(tree);
            }

            // Add Santa to calendar area
            if (!document.querySelector('.decoration-top-left')) {
                const santa = document.createElement('div');
                santa.className = 'december-decorations decoration-top-left';
                santa.innerHTML = '🎅';
                document.body.appendChild(santa);
            }

            // Add snowflake decoration
            if (!document.querySelector('.decoration-top-right')) {
                const flake = document.createElement('div');
                flake.className = 'december-decorations decoration-top-right';
                flake.textContent = '❄️';
                document.body.appendChild(flake);
            }
        }

        function updateClock() {
            const now = new Date();
            const timeStr = now.toLocaleTimeString('en-US', {
                hour: 'numeric', minute: '2-digit', hour12: true
            });
            const dateStr = now.toLocaleDateString('en-US', {
                weekday: 'short', month: 'short', day: 'numeric'
            });
            // Update sidebar (if visible)
            const sidebarTime = document.getElementById('currentTime');
            const sidebarDate = document.getElementById('currentDate');
            if (sidebarTime) sidebarTime.textContent = timeStr;
            if (sidebarDate) sidebarDate.textContent = dateStr;
            // Update header
            const headerTime = document.getElementById('headerTime');
            const headerDate = document.getElementById('headerDate');
            if (headerTime) headerTime.textContent = timeStr;
            if (headerDate) headerDate.textContent = dateStr;
        }

        async function fetchWeather() {
            try {
                const res = await fetch('/api/weather');
                const weather = await res.json();

                if (weather.current) {
                    document.getElementById('weatherTemp').textContent = weather.current.temp + '°F';
                    document.getElementById('weatherDesc').textContent = weather.current.emoji;
                    // Update header weather
                    const headerTemp = document.getElementById('headerWeatherTemp');
                    const headerIcon = document.getElementById('headerWeatherIcon');
                    if (headerTemp) headerTemp.textContent = weather.current.temp + '°';
                    if (headerIcon) headerIcon.textContent = weather.current.emoji;
                    
                    // Render forecast
                    const forecastHtml = weather.forecast.map(day => `
                        <div class="forecast-item">
                            <span class="forecast-day">${day.day.substring(0, 3)}</span>
                            <span class="forecast-icon">${day.emoji}</span>
                            <span class="forecast-temps">${day.high}° / ${day.low}°</span>
                            ${day.rain > 30 ? `<span class="rain-alert">☔ ${day.rain}%</span>` : ''}
                        </div>
                    `).join('');
                    
                    // Add forecast container if not exists, else update
                    let container = document.getElementById('weatherForecast');
                    if (!container) {
                        const widget = document.querySelector('.weather-widget');
                        container = document.createElement('div');
                        container.id = 'weatherForecast';
                        container.className = 'weather-forecast';
                        widget.appendChild(container);
                    }
                    container.innerHTML = forecastHtml;
                }
            } catch (e) {
                console.error("Weather load failed", e);
            }
        }

        // Month Navigation
        function renderMonthNav() {
            const currentMonth = new Date().getMonth();
            document.getElementById('monthNav').innerHTML = monthAbbrev.map((m, i) => `
                <button class="month-btn ${i === expandedMonth ? 'current' : ''}" onclick="openMonth(${i})">${m}</button>
            `).join('');
            // Also update header dropdown
            const monthSelect = document.getElementById('monthSelect');
            if (monthSelect) monthSelect.value = expandedMonth;
        }

        function openMonth(month) {
            // Handle year change when navigating past December or before January
            if (month > 11) {
                month = 0;
                currentYear++;
                if (currentYear > 2030) currentYear = 2030;
            } else if (month < 0) {
                month = 11;
                currentYear--;
                if (currentYear < 2024) currentYear = 2024;
            }
            expandedMonth = month;
            renderMonthNav();
            renderCalendar();
            // Scroll to the expanded month
            setTimeout(() => {
                const el = document.getElementById('month-' + month);
                if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 100);
        }

        function showPanel(panel) {
            document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));

            const panelId = panel + 'Panel';
            const panelEl = document.getElementById(panelId);
            if (panelEl) panelEl.classList.add('active');

            // Update header - show year nav for calendar, page title for others
            const calendarNav = document.getElementById('calendarNav');
            const pageTitle = document.getElementById('pageTitle');
            const todayBtn = document.getElementById('todayBtn');
            const monthSelectWrapper = document.getElementById('monthSelectWrapper');

            const titles = {
                'calendar': '',
                'meals': '🍽️ Meal Planner',
                'shopping': '🛒 Shopping List',
                'kids': '⭐ Kids Corner'
            };

            if (panel === 'calendar') {
                if (calendarNav) calendarNav.style.display = 'flex';
                if (pageTitle) pageTitle.style.display = 'none';
                if (todayBtn) todayBtn.style.display = '';
                if (monthSelectWrapper) monthSelectWrapper.style.display = '';
            } else {
                if (calendarNav) calendarNav.style.display = 'none';
                if (pageTitle) {
                    pageTitle.style.display = '';
                    pageTitle.textContent = titles[panel] || panel;
                }
                if (todayBtn) todayBtn.style.display = 'none';
                if (monthSelectWrapper) monthSelectWrapper.style.display = 'none';
            }

            // Update header nav buttons - show all except current screen
            const navCalendar = document.getElementById('navCalendar');
            const navMeals = document.getElementById('navMeals');
            const navShopping = document.getElementById('navShopping');
            const navLiv = document.getElementById('navLiv');
            const navJane = document.getElementById('navJane');
            const navEvent = document.getElementById('navEvent');

            // Show Calendar button only when NOT on calendar
            if (navCalendar) navCalendar.style.display = (panel === 'calendar') ? 'none' : '';
            // Hide the button for current panel
            if (navMeals) navMeals.style.display = (panel === 'meals') ? 'none' : '';
            if (navShopping) navShopping.style.display = (panel === 'shopping') ? 'none' : '';
            // Hide both kid buttons when on kids panel
            if (navLiv) navLiv.style.display = (panel === 'kids') ? 'none' : '';
            if (navJane) navJane.style.display = (panel === 'kids') ? 'none' : '';
            // Event button only shows on calendar
            if (navEvent) navEvent.style.display = (panel === 'calendar') ? '' : 'none';
        }

        // Show kids panel with specific kid selected
        function showKidPanel(kid) {
            selectedKid = kid;
            showPanel('kids');
            // Update kid card selection
            document.getElementById('livCard').classList.toggle('selected', kid === 'liv');
            document.getElementById('janeCard').classList.toggle('selected', kid === 'jane');
            renderKids();
        }

        // Jump to month from dropdown
        function jumpToMonth(month) {
            expandedMonth = parseInt(month);
            renderMonthNav();
            renderCalendar();
            // Update dropdown to match
            const monthSelect = document.getElementById('monthSelect');
            if (monthSelect) monthSelect.value = month;
        }

        // Calendar - ONLY show the expanded month (no collapsed months)
        function renderCalendar() {
            const today = new Date();
            // Update the year title
            document.getElementById('yearTitle').textContent = currentYear;
            // Render 4-day preview
            renderPreview(today);
            // Only render the expanded month - no other months visible
            document.getElementById('yearCalendar').innerHTML = renderExpandedMonth(currentYear, expandedMonth, today);
        }

        // Render 4-day preview section
        function renderPreview(today) {
            const previewGrid = document.getElementById('previewGrid');
            if (!previewGrid) return;

            const dayNamesShort = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
            let html = '';

            for (let i = 0; i < 4; i++) {
                const date = new Date(today);
                date.setDate(today.getDate() + i);
                const dateStr = date.toISOString().split('T')[0];
                const dayName = dayNamesShort[date.getDay()];
                const dayNum = date.getDate();

                let dayClass = 'preview-day';
                if (i === 0) dayClass += ' today';
                else if (i === 1) dayClass += ' tomorrow';

                // Get events for this day from global data
                const dayEvents = data.calendar.events.filter(e => e.date === dateStr);

                // Check for holidays from global data
                const holidayKey = (date.getMonth() + 1) + '-' + date.getDate();
                const holiday = data.holidays[holidayKey];

                html += `<div class="${dayClass}">`;
                html += `<div class="preview-day-header">`;
                html += `<span class="preview-day-name">${i === 0 ? 'Today' : i === 1 ? 'Tomorrow' : dayName}</span>`;
                html += `<span class="preview-day-num">${dayNum}</span>`;
                html += `</div>`;
                html += `<div class="preview-events">`;

                // Show holiday first
                if (holiday) {
                    html += `<div class="preview-event holiday">${holiday}</div>`;
                }

                // Show events with emojis
                dayEvents.forEach(event => {
                    let emoji = '';
                    const titleLower = event.title.toLowerCase();
                    if (titleLower.includes('birthday')) emoji = '🎂 ';
                    else if (titleLower.includes('grammy') || titleLower.includes('grandma') || titleLower.includes('grandmother')) emoji = '👵 ';
                    else if (titleLower.includes('grandpa') || titleLower.includes('grandfather')) emoji = '👴 ';
                    else if (titleLower.includes('dentist')) emoji = '🦷 ';
                    else if (titleLower.includes('doctor') || titleLower.includes('appointment')) emoji = '🏥 ';
                    else if (titleLower.includes('school')) emoji = '🏫 ';
                    else if (titleLower.includes('party')) emoji = '🎉 ';
                    else if (titleLower.includes('visit') || titleLower.includes('coming')) emoji = '🏠 ';

                    const eventClass = titleLower.includes('birthday') ? 'preview-event birthday' : 'preview-event';
                    html += `<div class="${eventClass}">${emoji}${event.title}</div>`;
                });

                if (!holiday && dayEvents.length === 0) {
                    html += `<div style="color:#999; font-size:11px; font-style:italic;">No events</div>`;
                }

                html += `</div></div>`;
            }

            previewGrid.innerHTML = html;
        }

        // Change the calendar year (forward or backward)
        function changeYear(delta) {
            currentYear += delta;
            // Limit to reasonable range (2024-2030)
            if (currentYear < 2024) currentYear = 2024;
            if (currentYear > 2030) currentYear = 2030;
            renderCalendar();
        }

        // Jump to today (reset year and month to current)
        function scrollToToday() {
            const today = new Date();
            currentYear = today.getFullYear();
            expandedMonth = today.getMonth();
            renderMonthNav();
            renderCalendar();
        }

        // Helper for scrolling (not used now but keeping for compatibility)
        function scrollToMonth(month) {
            // Since we only show one month, just change the expanded month
            openMonth(month);
        }

        // Expanded full month view - main calendar display
        function renderExpandedMonth(year, month, today) {
            const firstDay = new Date(year, month, 1);
            const lastDay = new Date(year, month + 1, 0);
            const startDay = firstDay.getDay();
            const daysInMonth = lastDay.getDate();
            const todayDate = today.getDate();
            const todayMonth = today.getMonth();

            let html = `
                <div class="expanded-month" id="month-${month}">
                    <div class="expanded-header">
                        <button class="nav-arrow" onclick="event.stopPropagation(); openMonth(${month - 1})">◀</button>
                        <h2 class="month-title">${monthNames[month]} ${year}</h2>
                        <button class="nav-arrow" onclick="event.stopPropagation(); openMonth(${month + 1})">▶</button>
                    </div>
                    <div class="calendar-grid">
                        <div class="day-header-row">
                            ${dayNames.map((d, i) => `<div class="day-header-cell ${i === 0 || i === 6 ? 'weekend' : ''}">${d}</div>`).join('')}
                        </div>
            `;

            // Previous month padding
            const prevMonth = new Date(year, month, 0);
            const prevDays = prevMonth.getDate();
            for (let i = startDay - 1; i >= 0; i--) {
                const d = prevDays - i;
                html += `<div class="calendar-day other-month"><div class="day-num">${d}</div></div>`;
            }

            // Current month days with different sizes based on proximity to today
            for (let day = 1; day <= daysInMonth; day++) {
                const dateStr = `${year}-${String(month + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
                const date = new Date(year, month, day);
                const isToday = date.toDateString() === today.toDateString();
                const isWeekend = date.getDay() === 0 || date.getDay() === 6;
                const events = data.calendar.events.filter(e => e.date === dateStr);
                const holiday = data.holidays[dateStr];
                const lunch = data.lunches[dateStr]; // School lunch for this day
                const breakfast = data.breakfast[dateStr]; // School breakfast
                const snack = data.snacks[dateStr]; // School snack
                const hasSchoolMeals = (lunch || breakfast || snack) && !isWeekend;

                // Determine day's class based on proximity to today
                const daysFromToday = Math.floor((date - today) / (1000 * 60 * 60 * 24));

                // Get holiday class for colorful styling
                const holidayClass = holiday ? getHolidayClass(holiday.name) : '';

                // Build day classes - SMART sizing based on distance from today
                let dayClasses = 'calendar-day';
                if (isToday) {
                    dayClasses += ' today';
                } else if (daysFromToday === 1) {
                    dayClasses += ' tomorrow';
                } else if (daysFromToday === -1) {
                    dayClasses += ' yesterday';
                } else if (daysFromToday >= 2 && daysFromToday <= 3) {
                    dayClasses += ' near-future-close';
                } else if (daysFromToday >= 4 && daysFromToday <= 7) {
                    dayClasses += ' near-future';
                } else if (daysFromToday >= 8 && daysFromToday <= 14) {
                    dayClasses += ' far-future';
                } else if (daysFromToday > 14) {
                    dayClasses += ' distant-future';
                } else if (daysFromToday >= -3 && daysFromToday <= -2) {
                    dayClasses += ' recent-past';
                } else if (daysFromToday >= -7 && daysFromToday <= -4) {
                    dayClasses += ' past-week';
                } else if (daysFromToday < -7) {
                    dayClasses += ' distant-past';
                }
                if (isWeekend) dayClasses += ' weekend';

                // For TODAY, render with chore columns
                if (isToday) {
                    html += `
                        <div class="${dayClasses}" onclick="openAddEventForDate('${dateStr}')">
                            <div class="day-num">${day}</div>
                            ${holiday ? `<div class="holiday-pill ${holidayClass}"><span class="emoji">${holiday.emoji}</span>${holiday.name}</div>` : ''}
                            ${hasSchoolMeals ? `
                                <div class="school-meals">
                                    ${breakfast ? `<div class="breakfast-pill"><span class="emoji">🥣</span>${breakfast}</div>` : ''}
                                    ${lunch ? `<div class="lunch-pill"><span class="emoji">🍽️</span>${lunch}</div>` : ''}
                                    ${snack ? `<div class="snack-pill"><span class="emoji">🍎</span>${snack}</div>` : ''}
                                </div>
                            ` : ''}
                            <div class="day-events">
                                ${events.slice(0, 3).map(e => `<div class="event-pill ${e.person}">${e.title}<button class="pill-delete" onclick="event.stopPropagation(); deleteEventFromCalendar(${e.id})">✕</button></div>`).join('')}
                            </div>
                            <div class="today-chores-container">
                                <div class="chore-column liv">
                                    <div class="chore-column-header">Emma</div>
                                    <div id="livChores"></div>
                                </div>
                                <div class="chore-column jane">
                                    <div class="chore-column-header">Sophie</div>
                                    <div id="janeChores"></div>
                                </div>
                            </div>
                        </div>
                    `;
                } else {
                    html += `
                        <div class="${dayClasses}" onclick="openAddEventForDate('${dateStr}')">
                            <div class="day-num">${day}</div>
                            <div class="day-events">
                                ${holiday ? `<div class="holiday-pill ${holidayClass}"><span class="emoji">${holiday.emoji}</span>${holiday.name}</div>` : ''}
                                ${hasSchoolMeals ? `
                                    <div class="school-meals">
                                        ${breakfast ? `<div class="breakfast-pill"><span class="emoji">🥣</span>${breakfast}</div>` : ''}
                                        ${lunch ? `<div class="lunch-pill"><span class="emoji">🍽️</span>${lunch}</div>` : ''}
                                        ${snack ? `<div class="snack-pill"><span class="emoji">🍎</span>${snack}</div>` : ''}
                                    </div>
                                ` : ''}
                                ${events.slice(0, 4).map(e => `<div class="event-pill ${e.person}">${e.title}${daysFromToday >= 0 ? `<button class="pill-delete" onclick="event.stopPropagation(); deleteEventFromCalendar(${e.id})">✕</button>` : ''}</div>`).join('')}
                                ${events.length > 4 ? `<div class="event-pill family">+${events.length - 4} more</div>` : ''}
                            </div>
                        </div>
                    `;
                }
            }

            // Next month padding
            const totalCells = startDay + daysInMonth;
            const remaining = totalCells % 7 === 0 ? 0 : 7 - (totalCells % 7);
            for (let i = 1; i <= remaining; i++) {
                html += `<div class="calendar-day other-month"><div class="day-num">${i}</div></div>`;
            }

            html += '</div></div>';
            return html;
        }

        function renderTodayEvents() {
            const today = new Date().toISOString().split('T')[0];
            const events = data.calendar.events.filter(e => e.date === today);
            const holiday = data.holidays[today];

            let html = '';

            if (holiday) {
                html += `
                    <div class="today-event" style="border-color: ${holiday.color}">
                        <span style="font-size:18px;margin-right:8px">${holiday.emoji}</span>
                        <span class="event-title">${holiday.name}</span>
                    </div>
                `;
            }

            if (events.length) {
                html += events.map(e => `
                    <div class="today-event" style="border-color: ${data.family[e.person]?.color || '#666'}">
                        <span class="event-time">${e.time || ''}</span>
                        <span class="event-title">${e.title}</span>
                    </div>
                `).join('');
            }

            if (!html) {
                html = '<div style="color:var(--text-muted);font-size:13px;padding:8px">No events today</div>';
            }

            document.getElementById('todayEvents').innerHTML = html;
        }

        // Day Detail Modal
        function showDayDetail(dateStr) {
            clickedDate = dateStr;
            const date = new Date(dateStr + 'T12:00:00');
            const events = data.calendar.events.filter(e => e.date === dateStr);
            const holiday = data.holidays[dateStr];

            document.getElementById('dayModalTitle').textContent = date.toLocaleDateString('en-US', {
                weekday: 'long', month: 'long', day: 'numeric', year: 'numeric'
            });

            let html = '';

            if (holiday) {
                html += `
                    <div class="holiday-banner">
                        <span class="emoji">${holiday.emoji}</span>
                        <span class="text">${holiday.name}</span>
                    </div>
                `;
            }

            if (events.length) {
                html += events.map(e => `
                    <div class="event-item" style="border-color: ${data.family[e.person]?.color || 'var(--accent-orange)'}">
                        <span class="title">${e.title}</span>
                        <span class="time">${e.time || 'All day'}</span>
                        <button class="delete-btn" onclick="event.stopPropagation(); deleteEvent(${e.id}, '${dateStr}', this)" title="Delete event">✕</button>
                    </div>
                `).join('');
            } else if (!holiday) {
                html = '<div class="empty-state"><div class="icon">📅</div>No events this day</div>';
            }

            document.getElementById('dayModalContent').innerHTML = html;
            document.getElementById('dayModal').classList.add('show');
        }

        // Add Event
        function openAddEventForDate(dateStr) {
            clickedDate = dateStr;
            showAddEvent();
        }

        function showAddEvent() {
            document.getElementById('eventDate').value = clickedDate || new Date().toISOString().split('T')[0];
            document.getElementById('eventTitle').value = '';
            document.getElementById('eventTime').value = '';
            selectedPerson = 'family';

            document.getElementById('personGrid').innerHTML = Object.entries(data.family).map(([key, p]) => `
                <div class="person-opt ${key === 'family' ? 'selected' : ''}"
                     style="color: ${p.color}"
                     onclick="selectPerson('${key}', this)">
                    <span class="emoji">${p.emoji}</span>
                    <span class="name">${p.name}</span>
                </div>
            `).join('');

            document.getElementById('eventModal').classList.add('show');
        }

        function selectPerson(person, el) {
            selectedPerson = person;
            document.querySelectorAll('.person-opt').forEach(p => p.classList.remove('selected'));
            el.classList.add('selected');
        }

        async function saveEvent() {
            const title = document.getElementById('eventTitle').value;
            const date = document.getElementById('eventDate').value;
            const time = document.getElementById('eventTime').value;
            if (!title || !date) return;

            // Create temporary event with temp ID for instant display
            const tempId = Date.now();
            const newEvent = { id: tempId, title, date, time, person: selectedPerson };

            // Immediately add to local data and update UI
            data.calendar.events.push(newEvent);
            closeModal('eventModal');
            renderCalendar();
            renderTodayEvents();

            // Send to server in background and update with real ID
            fetch('/api/calendar/add', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ title, date, time, person: selectedPerson })
            }).then(res => res.json()).then(result => {
                if (result.success) {
                    // Replace temp ID with real ID from server
                    const idx = data.calendar.events.findIndex(e => e.id === tempId);
                    if (idx !== -1) data.calendar.events[idx].id = result.event.id;
                }
            });
        }

        async function deleteEvent(eventId, dateStr, btn) {
            // Immediately hide the event item for instant feedback
            const eventItem = btn.closest('.event-item');
            eventItem.style.transition = 'opacity 0.2s, transform 0.2s';
            eventItem.style.opacity = '0';
            eventItem.style.transform = 'translateX(20px)';

            // Remove from local data immediately
            data.calendar.events = data.calendar.events.filter(e => e.id !== eventId);

            // Update the calendar view immediately
            renderCalendar();
            renderTodayEvents();

            // Remove the element after animation
            setTimeout(() => eventItem.remove(), 200);

            // Send delete to server in background
            fetch('/api/calendar/delete', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id: eventId })
            });
        }

        function deleteEventFromCalendar(eventId) {
            // Remove from local data immediately
            data.calendar.events = data.calendar.events.filter(e => e.id !== eventId);

            // Update the calendar view immediately
            renderCalendar();
            renderTodayEvents();

            // Send delete to server in background
            fetch('/api/calendar/delete', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id: eventId })
            });
        }

        // Shopping
        function renderShopping() {
            const items = data.shopping.items;
            document.getElementById('shoppingList').innerHTML = items.length ?
                items.map(i => `
                    <div class="shopping-item ${i.checked ? 'checked' : ''}" onclick="toggleItem(${i.id})">
                        <div class="checkbox">${i.checked ? '✓' : ''}</div>
                        <span>${i.name}</span>
                    </div>
                `).join('') :
                '<div class="empty-state"><div class="icon">🛒</div>Shopping list is empty</div>';
        }

        async function addShoppingItem() {
            const input = document.getElementById('newItem');
            const name = input.value.trim();
            if (!name) return;

            // Create temporary item with temp ID for instant display
            const tempId = Date.now();
            const newItem = { id: tempId, name, checked: false };

            // Immediately add to local data and update UI
            data.shopping.items.push(newItem);
            input.value = '';
            renderShopping();

            // Send to server in background and update with real ID
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

        function toggleItem(id) {
            // Immediately update local data and UI
            const item = data.shopping.items.find(i => i.id === id);
            if (item) item.checked = !item.checked;
            renderShopping();

            // Send to server in background
            fetch('/api/shopping/toggle', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id })
            });
        }

        function clearChecked() {
            // Immediately update local data and UI
            data.shopping.items = data.shopping.items.filter(i => !i.checked);
            renderShopping();

            // Send to server in background
            fetch('/api/shopping/clear', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: '{}' });
        }

        // Meals
        function renderMeals() {
            const days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
            const today = new Date().toLocaleDateString('en-US', { weekday: 'long' }).toLowerCase();

            document.getElementById('mealWeek').innerHTML = days.map(day => {
                const meal = data.meals.thisWeek[day];
                return `
                    <div class="meal-day ${day === today ? 'today' : ''}" onclick="showMealPicker('${day}')">
                        <span class="day-name">${day.charAt(0).toUpperCase() + day.slice(1)}</span>
                        <span class="meal-name">${meal?.name || 'Tap to plan'}</span>
                        <span class="meal-icon">${meal?.icon || '➕'}</span>
                    </div>
                `;
            }).join('');
        }

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

        function setMeal(name, icon) {
            // Immediately update local data and UI
            data.meals.thisWeek[selectedMealDay] = { name, icon };
            closeModal('mealModal');
            renderMeals();

            // Send to server in background
            fetch('/api/meals/set', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ day: selectedMealDay, meal: { name, icon } })
            });
        }

        function saveCustomMeal() {
            const name = document.getElementById('customMeal').value;
            if (name) setMeal(name, '🍽️');
        }

        // Kids/Chores
        function selectKid(kid) {
            selectedKid = kid;
            document.getElementById('livCard').classList.toggle('selected', kid === 'liv');
            document.getElementById('janeCard').classList.toggle('selected', kid === 'jane');
            renderKids();
        }

        function renderKids() {
            document.getElementById('livPoints').textContent = (data.rewards.points.liv || 0) + ' ⭐';
            document.getElementById('janePoints').textContent = (data.rewards.points.jane || 0) + ' ⭐';

            const today = new Date().toISOString().split('T')[0];
            const completedToday = data.chores.completed.filter(c => c.person === selectedKid && c.date === today);
            const completedIds = completedToday.map(c => c.choreId);

            const chores = data.chores.chores.filter(c => c.assignedTo.includes(selectedKid));
            document.getElementById('choreGrid').innerHTML = chores.map(c => `
                <button class="chore-btn ${completedIds.includes(c.id) ? 'done' : ''}" onclick="toggleChore(${c.id})">
                    <div class="icon">${c.icon}</div>
                    <div class="name">${c.name}</div>
                    <div class="pts">+${c.points} ⭐</div>
                </button>
            `).join('');
        }

        async function toggleChore(choreId) {
            const today = new Date().toISOString().split('T')[0];
            const isCompleted = data.chores.completed.some(c =>
                c.choreId === choreId && c.person === selectedKid && c.date === today
            );

            const endpoint = isCompleted ? '/api/chores/uncomplete' : '/api/chores/complete';
            const res = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ choreId, person: selectedKid })
            });

            const result = await res.json();
            if (result.success) {
                if (!isCompleted) {
                    const chore = data.chores.chores.find(c => c.id === choreId);
                    data.rewards.points[selectedKid] = (data.rewards.points[selectedKid] || 0) + (chore?.points || 0);
                    data.chores.completed.push({ choreId, person: selectedKid, date: today });
                } else {
                    const chore = data.chores.chores.find(c => c.id === choreId);
                    data.rewards.points[selectedKid] -= chore?.points || 0;
                    data.chores.completed = data.chores.completed.filter(c =>
                        !(c.choreId === choreId && c.person === selectedKid && c.date === today)
                    );
                }
                renderKids();
            }
        }

        // Fia Chat
        function toggleFiaChat() {
            document.getElementById('fiaModal').classList.toggle('show');
        }

        // Voice command functions - Web Speech API for real speech recognition
        let recognition = null;
        let currentVoiceContext = null;
        let currentMicBtn = null;

        // Initialize Web Speech API
        if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            recognition = new SpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = true;
            recognition.lang = 'en-US';
        }

        // Get the input and status elements for each context
        function getVoiceElements(context) {
            const map = {
                'calendar': { input: 'calendarVoiceInput', status: 'calendarVoiceStatus' },
                'meals': { input: 'mealsVoiceInput', status: 'mealsVoiceStatus' },
                'chores': { input: 'kidsVoiceInput', status: 'kidsVoiceStatus' },
                'shopping': { input: 'newItem', status: null }
            };
            return map[context] || { input: null, status: null };
        }

        function setVoiceStatus(context, message, type = '') {
            const els = getVoiceElements(context);
            if (els.status) {
                const statusEl = document.getElementById(els.status);
                if (statusEl) {
                    statusEl.textContent = message;
                    statusEl.className = 'voice-status-text ' + type;
                }
            }
        }

        async function startVoiceCommand(context, btn) {
            currentVoiceContext = context;
            currentMicBtn = btn;

            // Toggle off if already recording
            if (btn.classList.contains('recording')) {
                stopVoiceCommand();
                return;
            }

            // Check if speech recognition is available
            if (!recognition) {
                setVoiceStatus(context, 'Speech recognition not supported in this browser', 'error');
                return;
            }

            const els = getVoiceElements(context);
            const inputEl = document.getElementById(els.input);

            btn.classList.add('recording');
            btn.textContent = '⏹️';
            setVoiceStatus(context, '🎤 Listening...', 'listening');

            recognition.onresult = (event) => {
                let interimTranscript = '';
                let finalTranscript = '';

                for (let i = event.resultIndex; i < event.results.length; i++) {
                    const transcript = event.results[i][0].transcript;
                    if (event.results[i].isFinal) {
                        finalTranscript += transcript;
                    } else {
                        interimTranscript += transcript;
                    }
                }

                // Show interim results in input
                if (inputEl) {
                    inputEl.value = finalTranscript || interimTranscript;
                }

                // If we have final result, process it
                if (finalTranscript) {
                    setVoiceStatus(context, 'Processing...', '');
                }
            };

            recognition.onerror = (event) => {
                console.error('Speech recognition error:', event.error);
                let errorMsg = 'Error: ' + event.error;
                if (event.error === 'network') {
                    errorMsg = 'No internet - use the text box instead';
                } else if (event.error === 'not-allowed') {
                    errorMsg = 'Microphone blocked - check browser settings';
                } else if (event.error === 'no-speech') {
                    errorMsg = 'No speech heard - try again';
                } else if (event.error === 'aborted') {
                    errorMsg = '';
                }
                if (errorMsg) setVoiceStatus(context, errorMsg, 'error');
                stopVoiceCommand();
                // Clear error after 3 seconds
                if (errorMsg) setTimeout(() => setVoiceStatus(context, '', ''), 3000);
            };

            recognition.onend = () => {
                stopVoiceCommand();
                // Auto-submit if we got text
                if (inputEl && inputEl.value.trim()) {
                    processTextCommand(context, inputEl.value);
                }
            };

            try {
                recognition.start();
            } catch (err) {
                console.error('Recognition start error:', err);
                setVoiceStatus(context, 'Could not start listening', 'error');
                stopVoiceCommand();
            }
        }

        function stopVoiceCommand() {
            if (recognition) {
                try { recognition.stop(); } catch(e) {}
            }
            if (currentMicBtn) {
                currentMicBtn.classList.remove('recording');
                currentMicBtn.textContent = '🎤';
            }
        }

        // Process text command directly without chatbot
        async function processTextCommand(context, text) {
            if (!text || !text.trim()) return;

            const els = getVoiceElements(context);
            setVoiceStatus(context, 'Adding...', '');

            try {
                if (context === 'calendar') {
                    // Parse the text for event details
                    const eventData = parseEventText(text);
                    const response = await fetch('/api/calendar/add', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(eventData)
                    });
                    if (response.ok) {
                        setVoiceStatus(context, '✓ Added: ' + eventData.title, 'success');
                        document.getElementById(els.input).value = '';
                        renderCalendar();
                        setTimeout(() => setVoiceStatus(context, '', ''), 3000);
                    }
                } else if (context === 'shopping') {
                    // Add shopping items
                    const items = text.split(/,|and/).map(s => s.trim()).filter(s => s);
                    for (const item of items) {
                        await fetch('/api/shopping/add', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ name: item })
                        });
                    }
                    document.getElementById('newItem').value = '';
                    renderShopping();
                } else if (context === 'meals') {
                    // Parse meal planning
                    const mealData = parseMealText(text);
                    await fetch('/api/meals/set', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(mealData)
                    });
                    setVoiceStatus(context, '✓ Meal planned!', 'success');
                    document.getElementById(els.input).value = '';
                    renderMeals();
                    setTimeout(() => setVoiceStatus(context, '', ''), 3000);
                } else if (context === 'chores') {
                    // Parse chore completion
                    const choreData = parseChoreText(text);
                    if (choreData.person && choreData.chore) {
                        await fetch('/api/chores/complete', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify(choreData)
                        });
                        setVoiceStatus(context, '✓ ' + choreData.person + ' completed: ' + choreData.chore, 'success');
                        document.getElementById(els.input).value = '';
                        renderKids();
                        setTimeout(() => setVoiceStatus(context, '', ''), 3000);
                    } else {
                        setVoiceStatus(context, 'Could not understand. Try: "Emma made her bed"', 'error');
                    }
                }
            } catch (err) {
                console.error('Command processing error:', err);
                setVoiceStatus(context, 'Error processing command', 'error');
            }
        }

        // Parse natural language event text
        function parseEventText(text) {
            const now = new Date();
            let title = text;
            let date = now.toISOString().split('T')[0];
            let time = '';

            // Try to extract date patterns
            const datePatterns = [
                // "on the 15th" or "on dec 15" or "december 15th"
                /(?:on\s+)?(?:the\s+)?(\d{1,2})(?:st|nd|rd|th)?(?:\s+of)?(?:\s+(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*)?/i,
                // "dec 10" or "december 10th"
                /(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+(\d{1,2})(?:st|nd|rd|th)?/i,
                // "tomorrow"
                /tomorrow/i,
                // "next week"
                /next\s+week/i
            ];

            const monthMap = { jan:0, feb:1, mar:2, apr:3, may:4, jun:5, jul:6, aug:7, sep:8, oct:9, nov:10, dec:11 };

            // Check for month + day pattern first (e.g., "dec 10th")
            const monthDayMatch = text.match(/(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+(\d{1,2})(?:st|nd|rd|th)?/i);
            if (monthDayMatch) {
                const month = monthMap[monthDayMatch[1].toLowerCase().substring(0,3)];
                const day = parseInt(monthDayMatch[2]);
                const eventDate = new Date(now.getFullYear(), month, day);
                if (eventDate < now) eventDate.setFullYear(now.getFullYear() + 1);
                date = eventDate.toISOString().split('T')[0];
                title = text.replace(monthDayMatch[0], '').trim();
            }
            // Check for "on the 15th" pattern
            else {
                const dayMatch = text.match(/(?:on\s+)?(?:the\s+)?(\d{1,2})(?:st|nd|rd|th)/i);
                if (dayMatch) {
                    const day = parseInt(dayMatch[1]);
                    const eventDate = new Date(now.getFullYear(), now.getMonth(), day);
                    if (eventDate < now) eventDate.setMonth(eventDate.getMonth() + 1);
                    date = eventDate.toISOString().split('T')[0];
                    title = text.replace(dayMatch[0], '').trim();
                }
            }

            // Check for tomorrow
            if (/tomorrow/i.test(text)) {
                const tomorrow = new Date(now);
                tomorrow.setDate(tomorrow.getDate() + 1);
                date = tomorrow.toISOString().split('T')[0];
                title = text.replace(/tomorrow/i, '').trim();
            }

            // Extract time patterns - require "at" or am/pm to avoid matching dates
            const timeMatch = text.match(/at\s+(\d{1,2})(?::(\d{2}))?\s*(am|pm)?/i) ||
                              text.match(/(\d{1,2})(?::(\d{2}))?\s*(am|pm)/i);
            if (timeMatch) {
                let hours = parseInt(timeMatch[1]);
                const minutes = timeMatch[2] || '00';
                const ampm = timeMatch[3]?.toLowerCase();
                if (ampm === 'pm' && hours < 12) hours += 12;
                if (ampm === 'am' && hours === 12) hours = 0;
                time = hours.toString().padStart(2, '0') + ':' + minutes;
                title = title.replace(timeMatch[0], '').trim();
            }

            // Clean up title
            title = title.replace(/^(add|create|schedule|set|put)\s+/i, '').trim();
            title = title.replace(/\s+/g, ' ').trim();
            if (!title) title = 'Event';

            return { title, date, time, person: 'family' };
        }

        // Parse meal planning text
        function parseMealText(text) {
            const days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
            let day = null;
            let meal = text;

            for (const d of days) {
                if (text.toLowerCase().includes(d)) {
                    day = d;
                    meal = text.replace(new RegExp(d, 'i'), '').trim();
                    break;
                }
            }

            // Check for "tonight" or "today"
            if (/tonight|today/i.test(text)) {
                day = days[new Date().getDay()];
                meal = text.replace(/tonight|today/i, '').trim();
            }

            // Clean up meal
            meal = meal.replace(/^(plan|set|make|have|cook)\s+/i, '').trim();
            meal = meal.replace(/\s+for\s+(dinner|lunch|breakfast)\s*/i, '').trim();
            if (!meal) meal = 'Dinner';
            if (!day) day = days[new Date().getDay()];

            return { day, meal };
        }

        // Parse chore completion text
        function parseChoreText(text) {
            let person = null;
            let chore = text;

            // Check for person names
            if (/liv/i.test(text)) {
                person = 'liv';
                chore = text.replace(/liv('s)?\s*/i, '').trim();
            } else if (/jane/i.test(text)) {
                person = 'jane';
                chore = text.replace(/jane('s)?\s*/i, '').trim();
            }

            // Clean up chore text - extract the actual chore
            chore = chore.replace(/^(completed|did|finished|made|brushed|cleaned)\s+/i, '').trim();
            chore = chore.replace(/^(her|his|the)\s+/i, '').trim();

            return { person, chore };
        }

        async function sendFiaMessage() {
            const input = document.getElementById('fiaInput');
            const msg = input.value.trim();
            if (!msg) return;

            const messages = document.getElementById('fiaMessages');
            // Add user message with new styling
            messages.innerHTML += `
                <div class="fia-message user-message">
                    <div class="message-avatar">👤</div>
                    <div class="message-bubble">${msg}</div>
                </div>
            `;
            input.value = '';
            messages.scrollTop = messages.scrollHeight;

            try {
                const res = await fetch('http://localhost:8765/api/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: msg })
                });
                const result = await res.json();
                messages.innerHTML += `
                    <div class="fia-message fia-response">
                        <div class="message-avatar">🤖</div>
                        <div class="message-bubble">${result.response || 'No response'}</div>
                    </div>
                `;
            } catch (e) {
                messages.innerHTML += `
                    <div class="fia-message fia-response">
                        <div class="message-avatar">🤖</div>
                        <div class="message-bubble">I'm having trouble connecting. Make sure Fia is running at localhost:8765!</div>
                    </div>
                `;
            }
            messages.scrollTop = messages.scrollHeight;
        }

        // Quick Fia message from buttons
        function sendQuickFia(msg) {
            document.getElementById('fiaInput').value = msg;
            sendFiaMessage();
        }

        // Toggle Fia microphone for voice input
        let fiaMicRecorder = null;
        let fiaMicChunks = [];

        async function toggleFiaMic() {
            const btn = document.getElementById('fiaChatMic');

            if (btn.classList.contains('recording')) {
                // Stop recording
                if (fiaMicRecorder && fiaMicRecorder.state === 'recording') {
                    fiaMicRecorder.stop();
                }
                btn.classList.remove('recording');
                btn.querySelector('.mic-icon').textContent = '🎤';
                return;
            }

            // Start recording
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                fiaMicRecorder = new MediaRecorder(stream);
                fiaMicChunks = [];

                fiaMicRecorder.ondataavailable = e => fiaMicChunks.push(e.data);

                fiaMicRecorder.onstop = async () => {
                    stream.getTracks().forEach(track => track.stop());
                    // In production, send audio to Whisper for transcription
                    // For now, prompt user to type
                    document.getElementById('fiaInput').placeholder = 'Voice recorded! Type your message for now...';
                };

                fiaMicRecorder.start();
                btn.classList.add('recording');
                btn.querySelector('.mic-icon').textContent = '⏹️';

                // Auto-stop after 10 seconds
                setTimeout(() => {
                    if (fiaMicRecorder && fiaMicRecorder.state === 'recording') {
                        toggleFiaMic();
                    }
                }, 10000);

            } catch (err) {
                console.error('Mic error:', err);
                alert('Could not access microphone. Please allow microphone access.');
            }
        }

        // Modal helpers
        function closeModal(id) {
            document.getElementById(id).classList.remove('show');
        }

        document.querySelectorAll('.modal').forEach(modal => {
            modal.addEventListener('click', (e) => {
                if (e.target === modal) modal.classList.remove('show');
            });
        });

        // Screensaver Logic
        let idleTime = 0;
        const screensaverTime = 3; // Minutes
        const screensaver = document.getElementById('screensaver');
        const video = document.getElementById('screensaverVideo');
        const pixelOverlay = document.getElementById('pixelOverlay');
        let videoList = [];
        let currentVideoIndex = 0;
        let screensaverStarting = false;
        let playPromise = null;
        let isTransitioning = false;
        const SLOW_MO_RATE = 0.5; // 0.5x speed for slow motion

        function log(msg) {
            console.log("[Screensaver] " + msg);
        }

        // Fetch video list
        fetch('/api/videos')
            .then(r => r.json())
            .then(data => {
                log("Video API response: " + JSON.stringify(data));
                if (data.videos && data.videos.length > 0) {
                    videoList = data.videos;
                    log("Loaded " + videoList.length + " videos: " + videoList.join(", "));
                    // Preload first video
                    video.src = "/static/" + videoList[0];
                    video.playbackRate = SLOW_MO_RATE;
                    video.load();
                    log("Preloaded first video at " + SLOW_MO_RATE + "x speed");
                } else {
                    log("No videos found in API response.");
                }
            })
            .catch(e => log("Video fetch error: " + e));

        setInterval(() => {
            idleTime++;
            if (idleTime >= screensaverTime) startScreensaver();
        }, 60000);

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
                const src = "/static/" + videoList[currentVideoIndex];
                log("Switching to: " + src);
                video.src = src;
                video.playbackRate = SLOW_MO_RATE;
                video.load();
            }, 1500);

            // Step 3: Wait for new video ready, then fade in
            setTimeout(() => {
                video.oncanplaythrough = function() {
                    // Remove fade and pixelation
                    video.classList.remove('fade-out');

                    setTimeout(() => {
                        video.classList.remove('pixelate');
                        pixelOverlay.classList.remove('active');
                    }, 500);

                    // Start playing
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

                // Trigger if already ready
                if (video.readyState >= 3) {
                    video.oncanplaythrough();
                }
            }, 1800);
        }

        // Use transition instead of immediate switch
        video.onended = transitionToNextVideo;
        video.onerror = (e) => log("Video Error: " + (video.error ? video.error.message : "unknown"));
        video.oncanplay = () => { video.playbackRate = SLOW_MO_RATE; };
        video.onloadeddata = () => {
            log("Video data loaded, setting playback rate to " + SLOW_MO_RATE);
            video.playbackRate = SLOW_MO_RATE;
        };

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

            const src = "/static/" + videoList[currentVideoIndex];
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

        ['mousemove', 'mousedown', 'keypress', 'touchstart', 'scroll'].forEach(evt =>
            document.addEventListener(evt, resetTimer, false)
        );

        // Initial Load
        init();
    </script>
</body>
</html>
'''


