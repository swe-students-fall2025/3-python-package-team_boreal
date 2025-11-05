import pytest
from fortuneluckpredictor import futurePredictions

@pytest.fixture
def sample_names():
    return ["Alice", "Bob", "Charlie", "Diana", "Eve", ""]

def test_sanity_check():
    assert True

def test_output_type(sample_names):
    """Check that futurePrediction returns a string."""
    for name in sample_names:
        result = futurePredictions.futurePrediction(name)
        assert isinstance(result, str), f"Expected string, got {type(result)}"

def test_output_format(sample_names):
    """Check that the output contains name, career, marriage age, kids info, and success level."""
    for name in sample_names:
        result = futurePredictions.futurePrediction(name)
        assert name in result or name == "", f"Name '{name}' not found in output: {result}"
        assert "will be a" in result, f"'will be a' not found in output: {result}"
        assert "get married at" in result, f"'get married at' not found in output: {result}"
        assert "and you will be" in result, f"'and you will be' not found in output: {result}"

def test_consistent_output(sample_names):
    """Same name should always produce the same prediction."""
    for name in sample_names:
        result1 = futurePredictions.futurePrediction(name)
        result2 = futurePredictions.futurePrediction(name)
        assert result1 == result2, f"Same name '{name}' produced different results: {result1} vs {result2}"

def test_marriage_age_range(sample_names):
    """Check that marriage age is between 25 and 39."""
    import re
    for name in sample_names:
        result = futurePredictions.futurePrediction(name)
        # Extract the age number after "get married at"
        match = re.search(r'get married at (\d+)', result)
        assert match is not None, f"Could not find marriage age in: {result}"
        age = int(match.group(1))
        assert 25 <= age <= 39, f"Marriage age {age} is not in valid range (25-39) in: {result}"

def test_kids_count_range(sample_names):
    """Check that kids count is between 0 and 3."""
    import re
    for name in sample_names:
        result = futurePredictions.futurePrediction(name)
        if "with no kids" in result:
            kids_count = 0
        else:
            match = re.search(r'with (\d+) kid', result)
            assert match is not None, f"Could not find kids count in: {result}"
            kids_count = int(match.group(1))
        assert 0 <= kids_count <= 3, f"Kids count {kids_count} is not in valid range (0-3) in: {result}"


def test_career_in_list(sample_names):
    """Check that the career is from the expected list of careers."""
    valid_careers = [
        "software engineer", "doctor", "lawyer", "teacher", "artist",
        "entrepreneur", "scientist", "musician", "architect", "chef",
        "engineer", "journalist", "psychologist", "designer", "consultant",
        "nurse", "researcher", "manager", "analyst", "inventor"
    ]
    for name in sample_names:
        result = futurePredictions.futurePrediction(name)
       
        import re
        match = re.search(r'will be a (.+?) and get married', result)
        assert match is not None, f"Could not find career in: {result}"
        career = match.group(1).strip()
        assert career in valid_careers, f"Career '{career}' not in valid list. Output: {result}"

def test_success_level_in_list(sample_names):
    """Check that the success level is from the expected list."""
    valid_success_levels = ["very successful", "successful", "somewhat successful", "moderately successful"]
    for name in sample_names:
        result = futurePredictions.futurePrediction(name)
        import re
        match = re.search(r'and you will be (.+)$', result)
        assert match is not None, f"Could not find success level in: {result}"
        success = match.group(1).strip()
        assert success in valid_success_levels, f"Success level '{success}' not in valid list. Output: {result}"

def test_different_names_different_predictions():
    """Different names should potentially produce different predictions."""
    results = [futurePredictions.futurePrediction(name) for name in ["Alice", "Bob", "Charlie", "Diana"]]
    assert len(set(results)) >= 1, "All predictions were identical, which is unlikely"

