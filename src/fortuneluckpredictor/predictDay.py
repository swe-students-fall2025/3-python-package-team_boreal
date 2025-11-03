from .fortune import fortune

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

def predict_day(day: str) -> str:
    """
    Predict your day's vibe and include a random fortune.

    Args:
        day (str): Name of the day, case-insensitive (e.g. "Monday", "mon")

    Returns:
        str: A string combining the day's message and a random fortune.

    Example:
        >>> predict_day("Monday")
        'Monday: Fresh energy fills your week — set your intentions high. Fortune: Your resume will land on the perfect Meta recruiter’s desk this week.'
    """
    if not day or not day.strip():
        raise ValueError("Day must be a non-empty string.")

    day_lower = day.strip().lower()

    # Resolve abbreviations
    if day_lower in DAY_MESSAGES:
        key = day_lower
    elif day_lower in DAY_ALIASES:
        key = DAY_ALIASES[day_lower]
    else:
        raise ValueError(f"Unrecognized day name: {day}")

    message = DAY_MESSAGES[key]
    fortune_text = fortune()

    return f"{day.capitalize()}: {message} Fortune: {fortune_text}"
