import pytest
from src.fortuneluckpredictor import predictDay


# --- Helpers ---

def freeze_day(monkeypatch, year=2025, month=11, day=4):
    #Freeze datetime.now() to a fixed date for deterministic tests.
    from datetime import datetime as _DT

    class FixedDate(_DT):
        @classmethod
        def now(cls):
            return cls(year, month, day)

    monkeypatch.setattr(predictDay,"datetime", FixedDate, raising=True)


def pin_fortunes(monkeypatch, items):
    #Replace fortunes list inside predictDay.
    monkeypatch.setattr(predictDay,"fortunes", items, raising=True)


# --- Tests ---

def test_alias_normalization_is_case_and_space_insensitive(monkeypatch):
    freeze_day(monkeypatch)
    pin_fortunes(monkeypatch, ["ONLY_ONE"])
    for inp in ["fri", "Fri", "  FRI  "]:
        out = predictDay.predict_day(inp)
        assert out.startswith("Friday:")
        assert "Fortune: ONLY_ONE" in out


def test_full_day_name(monkeypatch):
    freeze_day(monkeypatch)
    pin_fortunes(monkeypatch, ["X"])
    out = predictDay.predict_day("Monday")
    assert out.startswith("Monday:")
    assert "Fresh energy fills your week" in out
    assert out.endswith("Fortune: X")


def test_blank_input_means_today(monkeypatch):
    freeze_day(monkeypatch, 2025, 11, 5)  # Wednesday
    pin_fortunes(monkeypatch, ["ONLY_ONE"])
    out = predictDay.predict_day("")  # blank → today
    assert out.startswith("Wednesday:")
    assert "Fortune: ONLY_ONE" in out


def test_whitespace_input(monkeypatch):
    freeze_day(monkeypatch, 2025, 11, 6)  # Thursday
    pin_fortunes(monkeypatch, ["Y"])
    out = predictDay.predict_day("   ")
    assert out.startswith("Thursday:")
    assert out.endswith("Fortune: Y")


def test_invalid_day_raises(monkeypatch):
    freeze_day(monkeypatch)
    with pytest.raises(ValueError):
        predictDay.predict_day("Funday")


def test_same_input_same_output_within_run(monkeypatch):
    freeze_day(monkeypatch)
    pin_fortunes(monkeypatch, ["A", "B", "C", "D", "E", "F", "G", "H"])
    a = predictDay.predict_day("Tuesday")
    b = predictDay.predict_day("Tuesday")
    assert a == b, "Same (date, day) should yield same fortune"

def test_different_day_different_output(monkeypatch):
    freeze_day(monkeypatch)
    pin_fortunes(monkeypatch, ["A", "B", "C", "D", "E", "F", "G", "H"])

    monday_output = predictDay.predict_day("Monday")
    tuesday_output = predictDay.predict_day("Tuesday")

    # Since RNG seed depends on day name, outputs should differ
    assert monday_output != tuesday_output, "Different days should yield different fortunes"

@pytest.mark.parametrize("alias, full", [
    ("mon", "Monday"), ("tue", "Tuesday"), ("tues", "Tuesday"),
    ("wed", "Wednesday"), ("thu", "Thursday"), ("thur", "Thursday"),
    ("thurs", "Thursday"), ("fri", "Friday"), ("sat", "Saturday"),
    ("sun", "Sunday"),
])
def test_alias_table(alias, full, monkeypatch):
    freeze_day(monkeypatch)
    pin_fortunes(monkeypatch, ["ONLY_ONE"])
    out = predictDay.predict_day(alias)
    assert out.startswith(f"{full}:")
    assert "Fortune: ONLY_ONE" in out
