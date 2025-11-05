from .fortune import fortunes
import random
from datetime import datetime

# Each day has its own "theme" or message style
DAY_MESSAGES = {
    "monday": "Fresh energy fills your week — set your intentions high.",
    "tuesday": "Progress is building; stay focused and take bold steps.",
    "wednesday": "Midweek clarity brings productive breakthroughs.",
    "thursday": "You’re almost at the finish line — stay sharp and consistent.",
    "friday": "Celebrate your wins, no matter how small!",
    "saturday": "Recharge your creative battery — inspiration awaits.",
    "sunday": "Plan lightly and dream big for the week ahead.",
}

# Support abbreviations (Mon, Tue, etc.)
DAY_ALIASES = {
    "mon": "monday",
    "tue": "tuesday", "tues": "tuesday",
    "wed": "wednesday",
    "thu": "thursday", "thur": "thursday", "thurs": "thursday",
    "fri": "friday",
    "sat": "saturday",
    "sun": "sunday",
}

def predict_day(day: str | None = None) -> str:
    # If no day provided, use today's day name
    if not day or not day.strip():
        day = datetime.now().strftime("%A")
    d = day.strip().lower()

    # Normalize to full day name
    key = d if d in DAY_MESSAGES else DAY_ALIASES.get(d)
    if not key:
        raise ValueError(f"Unrecognized day name: '{day}'")

    message = DAY_MESSAGES[key]

    # Create a deterministic fortune based on today's date and day name
    today = datetime.now().strftime("%Y-%m-%d")
    seed_value = hash(today + key) % (2**32)
    rng = random.Random(seed_value)
    fortune_text = rng.choice(fortunes)

    # Format nicely
    return f"{key.capitalize()}: {message} Fortune: {fortune_text}"