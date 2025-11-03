import re
import pytest
from fortuneluckpredictor import compatibility_score


@pytest.fixture
def sample_names():
    return [
        ("", ""),
        ("Alice", "Alicia"),
        ("Bob", "Bobby"),
        ("Eve", "Adam"),
        ("A", "E"),
        ("Zoë", "Zoe"),
    ]


def test_sanity_check():
    assert True


def test_compatibility_score_format_and_message(sample_names):
    prefix_re = re.compile(r"^Compatibility score: \d+\. ")
    messages = [
        "Perfect match — pure harmony! 💞",
        "You two vibe really well! ❤️",
        "There’s potential — stay open and see where it goes! 🌈",
        "You’ll meet someone wonderful who complements you perfectly! 💫",
    ]

    for n1, n2 in sample_names:
        output = compatibility_score.compatibility_score(n1, n2)
        assert isinstance(output, str)
        assert prefix_re.match(output), f"output did not match prefix: {output!r}"
        assert any(output.endswith(m) for m in messages), f"unexpected message in output: {output!r}"


def test_compatibility_score_is_deterministic(sample_names):
    for n1, n2 in sample_names:
        a = compatibility_score.compatibility_score(n1, n2)
        b = compatibility_score.compatibility_score(n1, n2)
        assert a == b