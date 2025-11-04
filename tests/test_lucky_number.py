import pytest
import math
from src.fortuneluckpredictor import luckyNumber

@pytest.fixture
def sample_ranges():
    return [
        (1, 100),
        (50, 60),
        (100, 1),  # reversed range
        (7, 7),    # single-number range
    ]

def test_sanity_check():
    assert True

# Range check
def test_output_type_and_bounds(sample_ranges):
    """Check that output is an integer within the expected bounds."""
    for r in sample_ranges:
        result = luckyNumber.get_lucky_number(r)
        assert isinstance(result, int)
        a, b = r
        lo, hi = (a, b) if a <= b else (b, a)
        assert lo <= result <= hi, f"{result} not in {lo}-{hi}"

# Returns same number when given same time
def test_consistent_same_seed(monkeypatch):
    """When called within the same minute, output should be stable."""
    from datetime import datetime
    class FixedTime(datetime):
        @classmethod
        def now(cls, tz=None):
            return datetime(2025, 11, 3, 14, 45)
    monkeypatch.setattr(luckyNumber, "datetime", FixedTime)
    first = luckyNumber.get_lucky_number((1, 100))
    second = luckyNumber.get_lucky_number((1, 100))
    assert first == second

# Returns different numbers at different times
def test_distribution_varies_over_time(monkeypatch):
    """Different times should usually yield different lucky numbers."""
    from datetime import datetime
    class TimeVariant(datetime):
        @classmethod
        def now(cls, tz=None):
            # alternate between two moments
            if hasattr(cls, "_toggle"):
                del cls._toggle
                return datetime(2025, 11, 3, 14, 46)
            else:
                cls._toggle = True
                return datetime(2025, 11, 2, 14, 45)
    monkeypatch.setattr(luckyNumber, "datetime", TimeVariant)
    n1 = luckyNumber.get_lucky_number((1, 100))
    n2 = luckyNumber.get_lucky_number((1, 100))
    assert n1 != n2, f"Expected different results across distinct datetimes ({n1} == {n2})"

def test_single_value_range():
    """If range has only one number, that number must be returned."""
    assert luckyNumber.get_lucky_number((42, 42)) == 42

def test_reversed_range_handled():
    """Swapped a,b should still produce valid result."""
    val = luckyNumber.get_lucky_number((100, 1))
    assert 1 <= val <= 100