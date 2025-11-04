import pytest
from src.fortuneluckpredictor import compatibility_score

# Sample names for testing
@pytest.fixture
def sample_names():
    return [
        ("", "", "Compatibility score: 0. Perfect match — pure harmony! 💞"),
        ("hello", "hi", "Compatibility score: 4. You two vibe really well! ❤️"),
        ("moon", "train", "Compatibility score: 5. There's potential — stay open and see where it goes! 🌈"),
        ("bee", "pool", "Compatibility score: 6. There's potential — stay open and see where it goes! 🌈"),
        ("aaa", "eee", "Compatibility score: 5. There's potential — stay open and see where it goes! 🌈"),
        ("hello", "hello", "Compatibility score: 0. Perfect match — pure harmony! 💞"),
        ("Michael", "Michelle", "Compatibility score: 5. There's potential — stay open and see where it goes! 🌈"),
        ("James", "Emma", "Compatibility score: 0. Perfect match — pure harmony! 💞"),
        ("Isabella", "Alexander", "Compatibility score: 0. Perfect match — pure harmony! 💞"),
        ("William", "Olivia", "Compatibility score: 4. You two vibe really well! ❤️"),
        ("Sophia", "Daniel", "Compatibility score: 8. You'll meet someone wonderful who complements you perfectly! 💫"),
        ("Emily", "David", "Compatibility score: 5. There's potential — stay open and see where it goes! 🌈"),
        ("Ethan", "Ava", "Compatibility score: 5. There's potential — stay open and see where it goes! 🌈"),
        ("Benjamin", "Charlotte", "Compatibility score: 0. Perfect match — pure harmony! 💞"),
        ("Mia", "Lucas", "Compatibility score: 7. There's potential — stay open and see where it goes! 🌈")
    ]

# Test sanity check
def test_sanity_check():
    assert True

# Test that output is a string
def test_format(sample_names):
    for n1, n2, _ in sample_names:
        output = compatibility_score.compatibility_score(n1, n2)
        assert isinstance(output, str)

# Test exact outputs for sample names
def test_exact_match(sample_names):
    for n1, n2, expected in sample_names:
        actual = compatibility_score.compatibility_score(n1, n2)
        assert actual == expected, f"for ({n1},{n2}) expected {expected!r} but got {actual!r}"

# Test that the compatibility score is same for same inputs
def test_consistent_output(sample_names):
    for n1, n2, _ in sample_names:
        a = compatibility_score.compatibility_score(n1, n2)
        b = compatibility_score.compatibility_score(n1, n2)
        assert a == b