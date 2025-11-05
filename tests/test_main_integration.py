import importlib
from unittest.mock import patch

def _load_main_module():
    """Import the main entrypoint module."""
    return importlib.import_module("fortuneluckpredictor.__main__")

# Helper to run main() with mocked inputs
def run_main_with_inputs(capsys, inputs):
    module = _load_main_module()
    with patch("builtins.input", side_effect=inputs):
        module.main()
    # Capture everything printed during this call to main()
    return capsys.readouterr().out

# Option 1: Get Fortune
def test_main_get_fortune_then_quit(capsys):
    out = run_main_with_inputs(capsys, ["1", "no"])
    assert "Your fortune" in out
    assert "Goodbye" in out

# Option 2: Future Prediction
def test_main_future_prediction(capsys):
    out = run_main_with_inputs(capsys, ["2", "TestUser", "n"])
    assert "will be a" in out
    assert "Goodbye" in out

# Option 3: Predict Day
def test_main_predict_day(capsys):
    out = run_main_with_inputs(capsys, ["3", "monday", "n"])
    assert "Fortune:" in out
    assert "Goodbye" in out

# Option 4: Compatibility Score
def test_main_compatibility_flow(capsys):
    out = run_main_with_inputs(capsys, ["4", "Alice", "Bob", "n"])
    assert "Compatibility score:" in out
    assert "Goodbye" in out

# Option 5: Lucky Number
def test_main_lucky_number(capsys):
    out = run_main_with_inputs(capsys, ["5", "n"])
    assert "Your lucky number" in out
    assert any(ch.isdigit() for ch in out)
    assert "Goodbye" in out

# Option 6: Exit
def test_main_exit_immediately(capsys):
    out = run_main_with_inputs(capsys, ["6"])
    assert "Goodbye" in out

# Invalid Option Test
def test_main_invalid_choice_then_exit(capsys):
    out = run_main_with_inputs(capsys, ["9", "6"])
    assert "Invalid choice" in out
    assert "Goodbye" in out

# Non-integer Input Test
def test_main_non_integer_choice_then_exit(capsys):
    out = run_main_with_inputs(capsys, ["abc", "6"])
    assert "Invalid choice" in out
    assert "Goodbye" in out

# Empty Input Test
def test_main_empty_choice_then_exit(capsys):
    out = run_main_with_inputs(capsys, ["", "6"])
    assert "Invalid choice" in out
    assert "Goodbye" in out

# Multiple Interactions Test
def test_main_multiple_interactions(capsys):
    out = run_main_with_inputs(capsys, [
        "1",  # Get fortune
        "yes",
        "5",  # Get lucky number
        "yes",
        "6"   # Exit
    ])
    assert out.count("Your fortune") == 1
    assert out.count("Your lucky number") == 1
    assert "Goodbye" in out

# Case Insensitive Test for Quit
def test_main_case_insensitive_options(capsys):
    out = run_main_with_inputs(capsys, ["  1  ", "Y", "2", "TestUser", "YES", "5", "NO"])
    assert "Your fortune" in out
    assert "will be a" in out
    assert "Your lucky number" in out
    assert "Goodbye" in out

# Error Handling in Predict Day
def test_main_handle_predict_day_error(capsys):
    out = run_main_with_inputs(capsys, ["3", "Funday", "6"])
    assert "Error:" in out
    assert "Goodbye" in out