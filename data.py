"""
Data constants for Family Planner Hub.
"""

# Family members with Skylight-style colors
FAMILY = {
    "dad": {"name": "Dad", "color": "#5B9BD5", "emoji": "👨", "role": "dad"},
    "mom": {"name": "Mom", "color": "#E36B9A", "emoji": "👩", "role": "mom"},
    "kid1": {"name": "Kid 1", "color": "#9B59B6", "emoji": "👧", "role": "daughter"},
    "kid2": {"name": "Kid 2", "color": "#F39C12", "emoji": "👧", "role": "daughter"},
    "family": {"name": "Family", "color": "#2ECC71", "emoji": "👨‍👩‍👧‍👧", "role": "all"}
}

# Complete US Holidays for 2025 and 2026
HOLIDAYS = {
    # 2025 Holidays
    "2025-01-01": {"name": "New Year's Day", "emoji": "🎉", "color": "#f39c12"},
    "2025-01-20": {"name": "Martin Luther King Jr. Day", "emoji": "✊", "color": "#3498db"},
    "2025-02-02": {"name": "Groundhog Day", "emoji": "🦫", "color": "#8B4513"},
    "2025-02-14": {"name": "Valentine's Day", "emoji": "💕", "color": "#e74c3c"},
    "2025-02-17": {"name": "Presidents' Day", "emoji": "🇺🇸", "color": "#3498db"},
    "2025-03-17": {"name": "St. Patrick's Day", "emoji": "🍀", "color": "#27ae60"},
    "2025-04-01": {"name": "April Fools' Day", "emoji": "🤡", "color": "#f39c12"},
    "2025-04-20": {"name": "Easter Sunday", "emoji": "🐰", "color": "#9b59b6"},
    "2025-04-22": {"name": "Earth Day", "emoji": "🌍", "color": "#27ae60"},
    "2025-05-05": {"name": "Cinco de Mayo", "emoji": "🌮", "color": "#27ae60"},
    "2025-05-11": {"name": "Mother's Day", "emoji": "💐", "color": "#e91e63"},
    "2025-05-26": {"name": "Memorial Day", "emoji": "🇺🇸", "color": "#3498db"},
    "2025-06-14": {"name": "Flag Day", "emoji": "🇺🇸", "color": "#3498db"},
    "2025-06-15": {"name": "Father's Day", "emoji": "👔", "color": "#3498db"},
    "2025-06-19": {"name": "Juneteenth", "emoji": "✊", "color": "#27ae60"},
    "2025-07-04": {"name": "Independence Day", "emoji": "🎆", "color": "#e74c3c"},
    "2025-09-01": {"name": "Labor Day", "emoji": "⚒️", "color": "#3498db"},
    "2025-10-13": {"name": "Columbus Day", "emoji": "🚢", "color": "#3498db"},
    "2025-10-31": {"name": "Halloween", "emoji": "🎃", "color": "#f39c12"},
    "2025-11-11": {"name": "Veterans Day", "emoji": "🎖️", "color": "#3498db"},
    "2025-11-27": {"name": "Thanksgiving Day", "emoji": "🦃", "color": "#d35400"},
    "2025-11-28": {"name": "Black Friday", "emoji": "🛍️", "color": "#2c3e50"},
    # December 2025 - Lunar phases
    "2025-12-04": {"name": "New Moon", "emoji": "🌑", "color": "#2c3e50"},
    "2025-12-07": {"name": "Pearl Harbor Day", "emoji": "🇺🇸", "color": "#3498db"},
    "2025-12-14": {"name": "Hanukkah Begins", "emoji": "🕎", "color": "#3498db"},
    "2025-12-15": {"name": "Full Cold Moon", "emoji": "🌕", "color": "#f1c40f"},
    "2025-12-21": {"name": "Winter Solstice", "emoji": "❄️", "color": "#00bcd4"},
    "2025-12-24": {"name": "Christmas Eve", "emoji": "🎄", "color": "#27ae60"},
    "2025-12-25": {"name": "Christmas Day", "emoji": "🎁", "color": "#c0392b"},
    "2025-12-26": {"name": "Kwanzaa Begins", "emoji": "🎊", "color": "#8e44ad"},
    "2025-12-31": {"name": "New Year's Eve", "emoji": "🎆", "color": "#f39c12"},

    # ============================================
    # 2026 - EARTHY, WELLNESS & WOMEN'S CALENDAR
    # Moon cycles, seasonal changes, goddess days,
    # nature observances, and wellness awareness
    # ============================================

    # JANUARY 2026
    "2026-01-01": {"name": "New Year's Day 🌿 Renewal", "emoji": "🎉", "color": "#f39c12"},
    "2026-01-03": {"name": "Full Wolf Moon ♋ | Mind-Body Wellness Day", "emoji": "🌕", "color": "#f1c40f"},
    "2026-01-05": {"name": "National Bird Day", "emoji": "🐦", "color": "#00bcd4"},
    "2026-01-06": {"name": "Triple Goddess Day", "emoji": "🌙", "color": "#9b59b6"},
    "2026-01-10": {"name": "Last Quarter Moon", "emoji": "🌗", "color": "#7f8c8d"},
    "2026-01-14": {"name": "Thorrablot (Winter Endurance)", "emoji": "❄️", "color": "#5d6d7e"},
    "2026-01-18": {"name": "New Moon ♑ | Day of Danu", "emoji": "🌑", "color": "#9b59b6"},
    "2026-01-19": {"name": "Martin Luther King Jr. Day", "emoji": "✊", "color": "#3498db"},
    "2026-01-21": {"name": "🌳 Rowan Month Begins", "emoji": "🌿", "color": "#27ae60"},
    "2026-01-23": {"name": "Maternal Health Awareness Day", "emoji": "💗", "color": "#e91e63"},
    "2026-01-26": {"name": "First Quarter Moon", "emoji": "🌓", "color": "#7f8c8d"},
    "2026-01-31": {"name": "International Zebra Day", "emoji": "🦓", "color": "#2c3e50"},

    # FEBRUARY 2026
    "2026-02-01": {"name": "Full Snow Moon ♌ | Imbolc 🌸", "emoji": "🌕", "color": "#e91e63"},
    "2026-02-02": {"name": "Candlemas | World Wetlands Day", "emoji": "🕯️", "color": "#00bcd4"},
    "2026-02-04": {"name": "Dísablót (Honor Female Ancestors)", "emoji": "👑", "color": "#9b59b6"},
    "2026-02-06": {"name": "National Wear Red Day ❤️", "emoji": "❤️", "color": "#e74c3c"},
    "2026-02-09": {"name": "Last Quarter Moon", "emoji": "🌗", "color": "#7f8c8d"},
    "2026-02-14": {"name": "Valentine's Day | World Bonobo Day", "emoji": "💕", "color": "#e74c3c"},
    "2026-02-15": {"name": "Lupercalia | World Hippo Day", "emoji": "🦛", "color": "#9b59b6"},
    "2026-02-16": {"name": "Presidents' Day", "emoji": "🇺🇸", "color": "#3498db"},
    "2026-02-17": {"name": "New Moon ♒ | Solar Eclipse | Mardi Gras", "emoji": "🌑", "color": "#5d6d7e"},
    "2026-02-18": {"name": "🌳 Ash Month Begins", "emoji": "🌿", "color": "#27ae60"},
    "2026-02-19": {"name": "Chinese New Year 🐴", "emoji": "🐴", "color": "#e74c3c"},
    "2026-02-24": {"name": "First Quarter Moon", "emoji": "🌓", "color": "#7f8c8d"},
    "2026-02-27": {"name": "International Polar Bear Day", "emoji": "🐻‍❄️", "color": "#00bcd4"},
    "2026-02-28": {"name": "Cake Day (Deity Offerings)", "emoji": "🍰", "color": "#e91e63"},

    # MARCH 2026
    "2026-03-01": {"name": "Full Worm Moon ♍ | Matronalia 👑", "emoji": "🌕", "color": "#e91e63"},
    "2026-03-03": {"name": "Total Lunar Eclipse | World Wildlife Day", "emoji": "🐾", "color": "#27ae60"},
    "2026-03-08": {"name": "International Women's Day 👩", "emoji": "💜", "color": "#9b59b6"},
    "2026-03-10": {"name": "Women & Girls HIV/AIDS Day", "emoji": "🎗️", "color": "#e74c3c"},
    "2026-03-11": {"name": "Last Quarter Moon", "emoji": "🌗", "color": "#7f8c8d"},
    "2026-03-14": {"name": "Day of Action for Rivers", "emoji": "🌊", "color": "#00bcd4"},
    "2026-03-15": {"name": "Digital Cleanup Day", "emoji": "♻️", "color": "#27ae60"},
    "2026-03-16": {"name": "National Panda Day", "emoji": "🐼", "color": "#2c3e50"},
    "2026-03-17": {"name": "St. Patrick's Day", "emoji": "🍀", "color": "#27ae60"},
    "2026-03-18": {"name": "🌳 Alder Month | Global Recycling Day", "emoji": "♻️", "color": "#27ae60"},
    "2026-03-19": {"name": "New Moon ♈", "emoji": "🌑", "color": "#5d6d7e"},
    "2026-03-20": {"name": "Spring Equinox 🌸 Ostara | World Frog Day", "emoji": "🌸", "color": "#e91e63"},
    "2026-03-21": {"name": "Day of Forests | World Planting Day", "emoji": "🌲", "color": "#27ae60"},
    "2026-03-22": {"name": "World Water Day | International Seal Day", "emoji": "🦭", "color": "#00bcd4"},
    "2026-03-25": {"name": "First Quarter Moon | Lady Day", "emoji": "🌓", "color": "#9b59b6"},
    "2026-03-30": {"name": "International Zero Waste Day", "emoji": "♻️", "color": "#27ae60"},

    # APRIL 2026
    "2026-04-02": {"name": "Full Pink Moon ♎", "emoji": "🌕", "color": "#f1c40f"},
    "2026-04-03": {"name": "World Aquatic Animal Day", "emoji": "🐠", "color": "#00bcd4"},
    "2026-04-04": {"name": "World Rat Day", "emoji": "🐀", "color": "#7f8c8d"},
    "2026-04-05": {"name": "Easter Sunday", "emoji": "🐰", "color": "#9b59b6"},
    "2026-04-07": {"name": "World Health Day | Beaver Day", "emoji": "🦫", "color": "#27ae60"},
    "2026-04-10": {"name": "Last Quarter Moon", "emoji": "🌗", "color": "#7f8c8d"},
    "2026-04-11": {"name": "Black Maternal Health Week Begins", "emoji": "💗", "color": "#9b59b6"},
    "2026-04-15": {"name": "🌳 Willow Month | Tax Day", "emoji": "🌿", "color": "#27ae60"},
    "2026-04-17": {"name": "New Moon ♈ | Bat Appreciation Day", "emoji": "🦇", "color": "#5d6d7e"},
    "2026-04-19": {"name": "Infertility Awareness Week Begins", "emoji": "💜", "color": "#9b59b6"},
    "2026-04-22": {"name": "Earth Day 🌍", "emoji": "🌍", "color": "#27ae60"},
    "2026-04-24": {"name": "First Quarter Moon | Lab Animals Day", "emoji": "🐁", "color": "#7f8c8d"},
    "2026-04-26": {"name": "Arbor Day 🌳", "emoji": "🌳", "color": "#27ae60"},
    "2026-04-27": {"name": "World Tapir Day | Hyena Day", "emoji": "🐾", "color": "#d35400"},
    "2026-04-28": {"name": "Floralia Begins (Flowers & Fertility)", "emoji": "🌺", "color": "#e91e63"},
    "2026-04-30": {"name": "May Eve 🧚 Walpurgisnacht", "emoji": "🧚", "color": "#9b59b6"},

    # MAY 2026
    "2026-05-01": {"name": "Full Flower Moon ♏ | Beltane 🔥 | Bona Dea", "emoji": "🌕", "color": "#e91e63"},
    "2026-05-02": {"name": "Greenery Day", "emoji": "🌿", "color": "#27ae60"},
    "2026-05-03": {"name": "International Leopard Day", "emoji": "🐆", "color": "#f39c12"},
    "2026-05-05": {"name": "Cinco de Mayo", "emoji": "🌮", "color": "#27ae60"},
    "2026-05-06": {"name": "World Maternal Mental Health Day", "emoji": "💜", "color": "#9b59b6"},
    "2026-05-08": {"name": "World Donkey Day", "emoji": "🫏", "color": "#7f8c8d"},
    "2026-05-09": {"name": "Last Quarter Moon", "emoji": "🌗", "color": "#7f8c8d"},
    "2026-05-10": {"name": "National Women's Health Week | Mother's Day 💐", "emoji": "💐", "color": "#e91e63"},
    "2026-05-11": {"name": "National Women's Checkup Day", "emoji": "💗", "color": "#e91e63"},
    "2026-05-13": {"name": "🌳 Hawthorn Month Begins", "emoji": "🌿", "color": "#27ae60"},
    "2026-05-16": {"name": "New Moon ♉", "emoji": "🌑", "color": "#5d6d7e"},
    "2026-05-20": {"name": "World Bee Day 🐝", "emoji": "🐝", "color": "#f39c12"},
    "2026-05-22": {"name": "Biodiversity Day | Preeclampsia Day", "emoji": "🌿", "color": "#27ae60"},
    "2026-05-23": {"name": "First Quarter Moon | World Turtle Day", "emoji": "🐢", "color": "#27ae60"},
    "2026-05-25": {"name": "Memorial Day", "emoji": "🇺🇸", "color": "#3498db"},
    "2026-05-27": {"name": "World Otter Day", "emoji": "🦦", "color": "#00bcd4"},
    "2026-05-28": {"name": "World Dugong Day", "emoji": "🌊", "color": "#00bcd4"},
    "2026-05-31": {"name": "Full Blue Moon ♐ | World Parrot Day", "emoji": "🌕", "color": "#3498db"},

    # JUNE 2026
    "2026-06-01": {"name": "World Reef Day 🐠", "emoji": "🐠", "color": "#00bcd4"},
    "2026-06-02": {"name": "World Peatlands Day", "emoji": "🌿", "color": "#27ae60"},
    "2026-06-03": {"name": "World Bicycle Day", "emoji": "🚲", "color": "#27ae60"},
    "2026-06-05": {"name": "World Environment Day 🌍", "emoji": "🌍", "color": "#27ae60"},
    "2026-06-08": {"name": "Last Quarter Moon | World Oceans Day 🌊", "emoji": "🌊", "color": "#00bcd4"},
    "2026-06-09": {"name": "Coral Triangle Day", "emoji": "🪸", "color": "#00bcd4"},
    "2026-06-10": {"name": "🌳 Oak Month Begins", "emoji": "🌳", "color": "#27ae60"},
    "2026-06-11": {"name": "International Lynx Day", "emoji": "🐱", "color": "#d35400"},
    "2026-06-12": {"name": "National Cougar Day", "emoji": "🦁", "color": "#d35400"},
    "2026-06-15": {"name": "New Moon ♊ | Global Wind Day", "emoji": "🌑", "color": "#00bcd4"},
    "2026-06-16": {"name": "World Sea Turtle Day", "emoji": "🐢", "color": "#27ae60"},
    "2026-06-17": {"name": "Desertification Day | World Croc Day", "emoji": "🐊", "color": "#27ae60"},
    "2026-06-19": {"name": "Juneteenth", "emoji": "✊", "color": "#27ae60"},
    "2026-06-20": {"name": "World Horseshoe Crab Day", "emoji": "🦀", "color": "#00bcd4"},
    "2026-06-21": {"name": "Summer Solstice ☀️ Litha | Father's Day | Giraffe Day", "emoji": "☀️", "color": "#f39c12"},
    "2026-06-22": {"name": "World Rainforest Day 🌴", "emoji": "🌴", "color": "#27ae60"},
    "2026-06-23": {"name": "Day of Lady & Lord of Sidhe 🧚", "emoji": "🧚", "color": "#9b59b6"},
    "2026-06-24": {"name": "Day of Household Deities", "emoji": "🏠", "color": "#9b59b6"},
    "2026-06-25": {"name": "World Decarbonisation Day", "emoji": "♻️", "color": "#27ae60"},
    "2026-06-29": {"name": "Full Strawberry Moon ♑", "emoji": "🌕", "color": "#f1c40f"},

    # JULY 2026
    "2026-07-01": {"name": "Crone Day (Wisdom Cycles) 👑", "emoji": "👑", "color": "#9b59b6"},
    "2026-07-04": {"name": "Independence Day", "emoji": "🎆", "color": "#e74c3c"},
    "2026-07-07": {"name": "Last Quarter Moon", "emoji": "🌗", "color": "#7f8c8d"},
    "2026-07-08": {"name": "🌳 Holly Month Begins", "emoji": "🌿", "color": "#27ae60"},
    "2026-07-11": {"name": "World Population Day", "emoji": "🌍", "color": "#27ae60"},
    "2026-07-14": {"name": "New Moon ♋ | Shark Day 🦈 | Chimp Day | Orca Day", "emoji": "🦈", "color": "#00bcd4"},
    "2026-07-16": {"name": "World Snake Day", "emoji": "🐍", "color": "#27ae60"},
    "2026-07-21": {"name": "First Quarter Moon", "emoji": "🌓", "color": "#7f8c8d"},
    "2026-07-24": {"name": "International Self-Care Day 💆", "emoji": "💆", "color": "#e91e63"},
    "2026-07-26": {"name": "International Mangrove Day", "emoji": "🌳", "color": "#27ae60"},
    "2026-07-28": {"name": "World Nature Conservation Day", "emoji": "🌿", "color": "#27ae60"},
    "2026-07-29": {"name": "Full Buck Moon ♒ | Tiger Day 🐅", "emoji": "🐅", "color": "#f39c12"},
    "2026-07-31": {"name": "World Ranger Day", "emoji": "🌲", "color": "#27ae60"},

    # AUGUST 2026
    "2026-08-01": {"name": "Lughnasadh 🌾 Lammas (Harvest)", "emoji": "🌾", "color": "#d35400"},
    "2026-08-04": {"name": "International Clouded Leopard Day", "emoji": "🐆", "color": "#f39c12"},
    "2026-08-05": {"name": "🌳 Hazel Month Begins", "emoji": "🌿", "color": "#27ae60"},
    "2026-08-06": {"name": "Last Quarter Moon", "emoji": "🌗", "color": "#7f8c8d"},
    "2026-08-08": {"name": "International Moon Bear Day", "emoji": "🐻", "color": "#5d6d7e"},
    "2026-08-10": {"name": "World Lion Day 🦁", "emoji": "🦁", "color": "#f39c12"},
    "2026-08-12": {"name": "New Moon ♌ | Total Solar Eclipse | Elephant Day 🐘", "emoji": "🐘", "color": "#5d6d7e"},
    "2026-08-13": {"name": "International Wolf Day 🐺", "emoji": "🐺", "color": "#5d6d7e"},
    "2026-08-15": {"name": "National Honey Bee Day 🐝", "emoji": "🐝", "color": "#f39c12"},
    "2026-08-19": {"name": "World Orangutan Day 🦧", "emoji": "🦧", "color": "#d35400"},
    "2026-08-20": {"name": "First Quarter Moon", "emoji": "🌓", "color": "#7f8c8d"},
    "2026-08-26": {"name": "Women's Equality Day 👩 | African Wild Dog Day", "emoji": "💪", "color": "#9b59b6"},
    "2026-08-28": {"name": "Full Sturgeon Moon ♓ | Partial Lunar Eclipse", "emoji": "🌕", "color": "#f1c40f"},
    "2026-08-30": {"name": "International Whale Shark Day 🦈", "emoji": "🦈", "color": "#00bcd4"},

    # SEPTEMBER 2026
    "2026-09-01": {"name": "World Beach Day | Primate Day 🐒", "emoji": "🏖️", "color": "#00bcd4"},
    "2026-09-02": {"name": "🌳 Vine Month Begins", "emoji": "🍇", "color": "#9b59b6"},
    "2026-09-04": {"name": "Last Quarter Moon", "emoji": "🌗", "color": "#7f8c8d"},
    "2026-09-05": {"name": "Amazon Rainforest Day 🌴", "emoji": "🌴", "color": "#27ae60"},
    "2026-09-07": {"name": "Labor Day | Clean Air Day", "emoji": "🌬️", "color": "#00bcd4"},
    "2026-09-11": {"name": "New Moon ♍", "emoji": "🌑", "color": "#5d6d7e"},
    "2026-09-12": {"name": "World Dolphin Day 🐬", "emoji": "🐬", "color": "#00bcd4"},
    "2026-09-16": {"name": "Ozone Layer Day", "emoji": "🌍", "color": "#00bcd4"},
    "2026-09-18": {"name": "First Quarter Moon | Water Monitoring Day", "emoji": "💧", "color": "#00bcd4"},
    "2026-09-20": {"name": "World Cleanup Day 🧹", "emoji": "🧹", "color": "#27ae60"},
    "2026-09-21": {"name": "Zero Emissions Day | Day of Peace ☮️", "emoji": "☮️", "color": "#00bcd4"},
    "2026-09-22": {"name": "Car Free Day | World Rhino Day 🦏", "emoji": "🦏", "color": "#5d6d7e"},
    "2026-09-23": {"name": "Autumn Equinox 🍂 Mabon", "emoji": "🍂", "color": "#d35400"},
    "2026-09-24": {"name": "World Gorilla Day 🦍", "emoji": "🦍", "color": "#5d6d7e"},
    "2026-09-26": {"name": "Full Harvest Moon ♈ | Cassowary Day", "emoji": "🌕", "color": "#f1c40f"},
    "2026-09-29": {"name": "Food Loss & Waste Awareness Day", "emoji": "🍎", "color": "#27ae60"},
    "2026-09-30": {"name": "🌳 Ivy Month | Women's Health & Fitness Day 💪", "emoji": "💪", "color": "#e91e63"},

    # OCTOBER 2026
    "2026-10-01": {"name": "International Raccoon Day 🦝", "emoji": "🦝", "color": "#7f8c8d"},
    "2026-10-02": {"name": "World Farm Animals Day", "emoji": "🐄", "color": "#27ae60"},
    "2026-10-03": {"name": "Last Quarter Moon", "emoji": "🌗", "color": "#7f8c8d"},
    "2026-10-04": {"name": "World Animal Day 🐾", "emoji": "🐾", "color": "#27ae60"},
    "2026-10-06": {"name": "National Badger Day 🦡", "emoji": "🦡", "color": "#5d6d7e"},
    "2026-10-08": {"name": "World Octopus Day 🐙", "emoji": "🐙", "color": "#9b59b6"},
    "2026-10-10": {"name": "New Moon ♎ | World Mental Health Day 💚", "emoji": "💚", "color": "#27ae60"},
    "2026-10-12": {"name": "Columbus Day", "emoji": "🚢", "color": "#3498db"},
    "2026-10-13": {"name": "Natural Disaster Reduction Day", "emoji": "🌍", "color": "#27ae60"},
    "2026-10-14": {"name": "International E-Waste Day", "emoji": "♻️", "color": "#27ae60"},
    "2026-10-17": {"name": "Sawfish Day | Stepping Stone Day", "emoji": "🐟", "color": "#00bcd4"},
    "2026-10-18": {"name": "First Quarter Moon | The Horn Fair", "emoji": "🌓", "color": "#d35400"},
    "2026-10-20": {"name": "International Sloth Day 🦥", "emoji": "🦥", "color": "#27ae60"},
    "2026-10-21": {"name": "Reptile Day | Earthworm Day 🪱", "emoji": "🪱", "color": "#27ae60"},
    "2026-10-22": {"name": "International Wombat Day", "emoji": "🐨", "color": "#7f8c8d"},
    "2026-10-23": {"name": "International Snow Leopard Day 🐆", "emoji": "🐆", "color": "#00bcd4"},
    "2026-10-24": {"name": "Freshwater Dolphin Day | Climate Action Day 🌍", "emoji": "🌍", "color": "#27ae60"},
    "2026-10-26": {"name": "Full Hunter's Moon ♉ | World Okapi Day", "emoji": "🌕", "color": "#f1c40f"},
    "2026-10-28": {"name": "🌳 Reed Month | World Sustainability Day", "emoji": "🌿", "color": "#27ae60"},
    "2026-10-31": {"name": "Samhain 🎃 Veil Thinning | Halloween", "emoji": "🎃", "color": "#f39c12"},

    # NOVEMBER 2026
    "2026-11-01": {"name": "World Ecology Day | Ancestor Days | Cailleach's Reign 👑", "emoji": "👑", "color": "#9b59b6"},
    "2026-11-03": {"name": "Election Day | World Basking Shark Day", "emoji": "🗳️", "color": "#00bcd4"},
    "2026-11-06": {"name": "Prevent Environmental War Day", "emoji": "☮️", "color": "#27ae60"},
    "2026-11-09": {"name": "New Moon ♏", "emoji": "🌑", "color": "#5d6d7e"},
    "2026-11-11": {"name": "Veterans Day", "emoji": "🎖️", "color": "#3498db"},
    "2026-11-15": {"name": "America Recycles Day ♻️", "emoji": "♻️", "color": "#27ae60"},
    "2026-11-16": {"name": "Night of Hecate 🌙 (Wisdom & Transitions)", "emoji": "🌙", "color": "#9b59b6"},
    "2026-11-17": {"name": "First Quarter Moon", "emoji": "🌓", "color": "#7f8c8d"},
    "2026-11-21": {"name": "World Fisheries Day 🐟", "emoji": "🐟", "color": "#00bcd4"},
    "2026-11-24": {"name": "Full Beaver Moon ♊", "emoji": "🌕", "color": "#f1c40f"},
    "2026-11-25": {"name": "🌳 Elder Month Begins", "emoji": "🌿", "color": "#9b59b6"},
    "2026-11-26": {"name": "Thanksgiving Day", "emoji": "🦃", "color": "#d35400"},
    "2026-11-27": {"name": "Black Friday", "emoji": "🛍️", "color": "#2c3e50"},
    "2026-11-29": {"name": "International Jaguar Day 🐆", "emoji": "🐆", "color": "#f39c12"},

    # DECEMBER 2026
    "2026-12-01": {"name": "Last Quarter Moon", "emoji": "🌗", "color": "#7f8c8d"},
    "2026-12-04": {"name": "International Cheetah Day 🐆 | Wildlife Conservation", "emoji": "🐆", "color": "#f39c12"},
    "2026-12-05": {"name": "Hanukkah Begins | World Soil Day", "emoji": "🕎", "color": "#3498db"},
    "2026-12-09": {"name": "New Moon ♐", "emoji": "🌑", "color": "#5d6d7e"},
    "2026-12-11": {"name": "International Mountain Day ⛰️", "emoji": "⛰️", "color": "#5d6d7e"},
    "2026-12-13": {"name": "Festival of Fortuna 🍀 (Luck & Blessings)", "emoji": "🍀", "color": "#f39c12"},
    "2026-12-14": {"name": "Monkey Day 🐵", "emoji": "🐵", "color": "#d35400"},
    "2026-12-17": {"name": "First Quarter Moon | Saturnalia Begins 🎊", "emoji": "🎊", "color": "#9b59b6"},
    "2026-12-21": {"name": "Winter Solstice ❄️ Yule (Sun Rebirth)", "emoji": "❄️", "color": "#00bcd4"},
    "2026-12-24": {"name": "Full Cold Moon ♋ | Birch Month | Christmas Eve", "emoji": "🌕", "color": "#f1c40f"},
    "2026-12-25": {"name": "Christmas Day | Oak King Birth 🌳", "emoji": "🎁", "color": "#c0392b"},
    "2026-12-26": {"name": "Kwanzaa Begins", "emoji": "🎊", "color": "#8e44ad"},
    "2026-12-30": {"name": "Last Quarter Moon", "emoji": "🌗", "color": "#7f8c8d"},
    "2026-12-31": {"name": "New Year's Eve | Hogmanay (Cleansing)", "emoji": "🎆", "color": "#f39c12"},
    # January 2027 (for the calendar end date)
    "2027-01-01": {"name": "New Year's Day", "emoji": "🎉", "color": "#f39c12"},
}

# Example school menu. Replace with your own school's menu (date -> lunch).
# Breakfast/snack are keyed by weekday and only show on days that have a lunch.
SCHOOL_LUNCHES = {
    "2026-01-05": "Example Lunch: Pasta",
    "2026-01-06": "Example Lunch: Tacos",
    "2026-01-07": "Example Lunch: Soup",
}

SCHOOL_BREAKFAST = {
    "monday": "Example Breakfast",
    "wednesday": "Example Breakfast",
}

SCHOOL_SNACK = {
    "monday": "Example Snack",
}

# Event categories
EVENT_CATEGORIES = {
    "medical": {"name": "Medical", "emoji": "🏥", "color": "#e74c3c"},
    "birthday": {"name": "Birthday", "emoji": "🎂", "color": "#9b59b6"},
    "school": {"name": "School", "emoji": "📚", "color": "#3498db"},
    "sports": {"name": "Sports", "emoji": "⚽", "color": "#27ae60"},
    "work": {"name": "Work", "emoji": "💼", "color": "#34495e"},
    "party": {"name": "Party", "emoji": "🎉", "color": "#e91e63"},
    "travel": {"name": "Travel", "emoji": "✈️", "color": "#00bcd4"},
    "reminder": {"name": "Reminder", "emoji": "⏰", "color": "#ff9800"},
    "other": {"name": "Other", "emoji": "📌", "color": "#607d8b"},
}
