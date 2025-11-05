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

# Test that names with same letters but different cases produce the same score
def test_case_insensitive():
    pairs = [
        ("JOHN", "mary"),
        ("John", "MARY"),
        ("jOhN", "MaRy"),
    ]
    first = compatibility_score.compatibility_score(pairs[0][0], pairs[0][1])
    for n1, n2 in pairs[1:]:
        result = compatibility_score.compatibility_score(n1, n2)
        assert result == first, f"Case sensitivity affected score: {pairs[0]} vs ({n1},{n2})"

# Test that names with spaces produce same score as trimmed names
def test_whitespace_handling():
    pairs = [
        (" Alice ", " Bob "),
        ("Alice", "Bob"),
        ("  Alice", "Bob  "),
        ("\tAlice\t", "\nBob\n"),
    ]
    first = compatibility_score.compatibility_score(pairs[0][0], pairs[0][1])
    for n1, n2 in pairs[1:]:
        result = compatibility_score.compatibility_score(n1, n2)
        assert result == first, f"Whitespace affected score: {pairs[0]} vs ({n1},{n2})"

# Test that order of names does not affect the score
def test_order():
    name_pairs = [
        ("Alice", "Bob"),
        ("Emma", "Oliver"),
        ("Luna", "Sol"),
    ]
    for n1, n2 in name_pairs:
        forward = compatibility_score.compatibility_score(n1, n2)
        reverse = compatibility_score.compatibility_score(n2, n1)
        assert forward == reverse, f"Score differs when names swapped: {n1},{n2}"

# Test that names with special characters are handled correctly
def test_special_characters():
    special_names = [
        ("John123", "Mary456"),
        ("Anna-Maria", "Jean-Paul"),
        ("O'Connor", "McDonald"),
        ("  Space  ", "  Tab\t"),
    ]
    for n1, n2 in special_names:
        result = compatibility_score.compatibility_score(n1, n2)
        assert isinstance(result, str), f"Failed to handle special characters in {n1},{n2}"
        assert "Compatibility score:" in result

# Test that compatibility score is always between 0 and 9
def test_score_bounds():
    test_pairs = [
        ("aaaaaa", "eeeeee"),
        ("xyz123", "wvt456"),
        ("aeiou", "uoiea"),
        ("A"*100, "E"*100),
    ]
    for n1, n2 in test_pairs:
        result = compatibility_score.compatibility_score(n1, n2)
        score = int(result.split(".")[0].split(": ")[1])
        assert 0 <= score <= 9, f"Score {score} out of bounds for {n1},{n2}"