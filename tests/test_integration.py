import pytest
from datetime import datetime
from src.fortuneluckpredictor import (
    fortune,
    futurePredictions,
    compatibility_score,
    luckyNumber,
    predictDay
)

class TestFortuneLuckPredictorIntegration:
    """Integration tests for Fortune Luck Predictor.
    
    Tests interactions between different components and complete user workflows.
    """

    def test_complete_user_session(self):
        """Test a complete user session getting multiple predictions."""
        # Same user should get consistent future predictions
        name = "Alice"
        future1 = futurePredictions.futurePrediction(name)
        future2 = futurePredictions.futurePrediction(name)
        assert future1 == future2, "Future predictions should be consistent for same user"

        # Lucky number should be within valid range and consistent within same day
        num1 = luckyNumber.get_lucky_number()
        num2 = luckyNumber.get_lucky_number()
        assert 1 <= num1 <= 100, f"Lucky number {num1} outside valid range"
        assert num1 == num2, "Lucky numbers should be consistent within same day"

        # Day prediction should work for current day
        today = datetime.now().strftime("%A")
        day_prediction = predictDay.predict_day(today)
        assert isinstance(day_prediction, str)
        assert today in day_prediction

        # Fortune should be non-empty
        user_fortune = fortune.fortune()
        assert user_fortune and isinstance(user_fortune, str)

    def test_cross_feature_consistency(self, monkeypatch):
        """Test consistency across different features when time/date is fixed."""
        # Fix the datetime to ensure consistent results
        fixed_date = datetime(2025, 11, 4, 12, 0)
        class FixedDateTime(datetime):
            @classmethod
            def now(cls, tz=None):
                return fixed_date
        monkeypatch.setattr("src.fortuneluckpredictor.luckyNumber.datetime", FixedDateTime)
        monkeypatch.setattr("src.fortuneluckpredictor.predictDay.datetime", FixedDateTime)

        # Get predictions for a fixed user
        name = "TestUser"
        
        # All features should work together without interfering
        future = futurePredictions.futurePrediction(name)
        assert isinstance(future, str)

        lucky = luckyNumber.get_lucky_number()
        assert isinstance(lucky, int)

        day = predictDay.predict_day(fixed_date.strftime("%A"))
        assert isinstance(day, str)

        fort = fortune.fortune()
        assert isinstance(fort, str)

    def test_relationship_validations(self):
        """Test relationship-based features work together correctly."""
        # Test multiple compatibility checks
        pairs = [
            ("Alice", "Bob"),
            ("Charlie", "Diana"),
            ("Bob", "Alice"),  # Reversed pair
        ]
        
        scores = {}
        for n1, n2 in pairs:
            result = compatibility_score.compatibility_score(n1, n2)
            scores[(n1, n2)] = result

        # Verify symmetry of compatibility scores
        assert scores[("Alice", "Bob")] == scores[("Bob", "Alice")], \
            "Compatibility scores should be symmetric"

        # Check all scores are properly formatted
        for result in scores.values():
            assert result.startswith("Compatibility score: "), \
                "All results should start with 'Compatibility score: '"
            score = int(result.split(".")[0].split(": ")[1])
            assert 0 <= score <= 9, f"Score {score} outside valid range"

    def test_error_propagation(self):
        """Test error handling across components."""
        # Invalid day name should raise ValueError
        with pytest.raises(ValueError):
            predictDay.predict_day("InvalidDay")

        # Invalid lucky number range should raise TypeError
        with pytest.raises(TypeError):
            luckyNumber.get_lucky_number(None)

        # Future predictions and compatibility should handle special characters
        special_name = "Test@User#123"
        assert futurePredictions.futurePrediction(special_name)
        assert compatibility_score.compatibility_score(special_name, "Normal Name")

    @pytest.mark.parametrize("day", ["Monday", "tuesday", "WED", "Thu", "Friday"])
    def test_multiple_predictions_same_day(self, day):
        """Test getting multiple types of predictions for the same day."""
        # Get day prediction
        day_result = predictDay.predict_day(day)
        assert day.lower() in day_result.lower()

        # Get fortune and ensure it's valid
        fort = fortune.fortune()
        assert isinstance(fort, str) and fort

        # Get lucky number and verify it's in range
        num = luckyNumber.get_lucky_number()
        assert 1 <= num <= 100