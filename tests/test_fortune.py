import pytest
from src.fortuneluckpredictor import fortune

def test_sanity_check():
    assert True

def test_output_type():
    """Check that get_fortune returns a string."""
    result = fortune.get_fortune()
    assert isinstance(result, str), f"Expected string, got {type(result)}"
    
    result_no_cookie = fortune.get_fortune(cookie=False)
    assert isinstance(result_no_cookie, str), f"Expected string, got {type(result_no_cookie)}"

def test_cookie_emoji():
    """Check that get_fortune(cookie=True) includes the cookie emoji."""
    result = fortune.get_fortune(cookie=True)
    assert result.startswith("🍪"), f"Expected cookie emoji at start, got: {result}"
    assert "🍪" in result, f"Cookie emoji not found in: {result}"

def test_no_cookie_emoji():
    """Check that get_fortune(cookie=False) does not include the cookie emoji."""
    result = fortune.get_fortune(cookie=False)
    assert not result.startswith("🍪"), f"Should not start with cookie emoji, got: {result}"
    assert "🍪" not in result, f"Cookie emoji should not be in output: {result}"

def test_valid_fortune():
    """Check that the fortune text (without emoji) is from the valid list."""
    valid_fortunes = [
        "Your resume will land on the perfect Meta recruiter's desk this week.",
        "A Meta engineer will soon endorse your skills and open a new door.",
        "The next coding interview you take will feel like designing the future of social connections.",
        "Your grind on system design is about to pay off with a Reality Labs breakthrough.",
        "A friendly referral will unlock the Meta pipeline you've been eyeing.",
        "An unexpected DM from a Meta recruiter will kickstart your big tech journey.",
        "Your portfolio will impress a Meta hiring manager far more than you expect.",
        "A well-timed leetcode streak will boost your confidence for the Meta onsite.",
        "Soon you'll celebrate a Meta offer with your closest supporters.",
        "The next recruiter call you accept will change the trajectory of your career in the metaverse.",
        "A spontaneous trip will lead to a story you retell for years.",
        "Your curiosity will uncover a hobby that becomes a passion.",
        "A long-standing question will be answered in the most unexpected way.",
        "You will reconnect with someone who inspires you to dream bigger.",
        "Small daily habits will compound into a breakthrough moment.",
        "A random compliment will brighten your day and boost your confidence.",
        "Your next challenge will reveal strength you didn't know you had.",
        "A creative idea will blossom into a project that excites others.",
        "Soon you will realize you are exactly where you need to be.",
        "An opportunity to help someone will come, and your kindness will be remembered.",
    ]
    
    result_with_cookie = fortune.get_fortune(cookie=True)
    fortune_text = result_with_cookie.replace("🍪 ", "").strip()
    assert fortune_text in valid_fortunes, f"Fortune '{fortune_text}' not in valid list"
    
    result_no_cookie = fortune.get_fortune(cookie=False)
    assert result_no_cookie in valid_fortunes, f"Fortune '{result_no_cookie}' not in valid list"

