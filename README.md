![CI/CD](https://github.com/swe-students-fall2025/3-python-package-team_boreal/actions/workflows/ci.yml/badge.svg)
# Fortune Luck Predictor

A Python package that returns lucky numbers, fortunes, and horoscope-like results.
## Team

- Pranathi Chinthalapani — prc9852@nyu.edu ([GitHub](https://github.com/PranathiChin))
- Sam Rawdon — sr6360@nyu.edu ([GitHub](https://github.com/SamRawdon))
- May Zhou — zz4206@nyu.edu ([GitHub](https://github.com/zz4206))
- Hanjun Deng — hd2432@nyu.edu ([GitHub](https://github.com/Deng-Hanjun))
- William Chan — wc2184@nyu.edu ([GitHub](https://github.com/wc2184))

## What is it?


Fortune Luck Predictor provides:
- Fortunes: Random fortune cookie-style messages
- Future Predictions: Predicts career, marriage age, number of kids, and success level
- Day Predictions: Get day-specific fortunes for any day of the week
- Compatibility Scores: Calculate compatibility between two names
- Lucky Numbers: Generate weighted lucky numbers based on the current date and time

## Installation

From PyPI:
```bash
pip install fortuneluckpredictor
```

From source:
```bash
git clone https://github.com/swe-students-fall2025/3-python-package-team_boreal.git
cd 3-python-package-team_boreal
pip install -e .
```

## How to Run

### Interactive Mode

Run the package as a module:
```bash
python -m fortuneluckpredictor
```

Or if you need to set PYTHONPATH:
```bash
PYTHONPATH=src python -m fortuneluckpredictor
```

This launches an interactive menu with all available functions.

### Using as a Package

Import and use the functions in your Python code:

```python
from fortuneluckpredictor.fortune import get_fortune
from fortuneluckpredictor.futurePredictions import futurePrediction
from fortuneluckpredictor.predictDay import predict_day
from fortuneluckpredictor.compatibility_score import compatibility_score
from fortuneluckpredictor.luckyNumber import get_lucky_number

# Get a fortune
print(get_fortune())

# Predict your future
print(futurePrediction("Alice"))

# Predict a day
print(predict_day("Monday"))

# Check compatibility
print(compatibility_score("Alice", "Bob"))

# Get a lucky number
print(get_lucky_number((1, 100)))
```

## Development

Set up the development environment:
```bash
pipenv install --dev
pipenv shell
pip install -e .
```

Run tests:
```bash
pytest tests/
```

## Links

- GitHub: https://github.com/swe-students-fall2025/3-python-package-team_boreal
- PyPI: https://pypi.org/project/fortuneluckpredictor/
