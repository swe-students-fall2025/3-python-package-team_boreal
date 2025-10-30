"""
Entry point for the fortuneluckpredictor package when run as a script.
"""

from .fortune import fortune
from .futurePredictions import futurePrediction
from .compatibility_score import compatibility_score
from .luckyNumber import get_lucky_number

def main() -> None:
    """
    Fetch a fortune and print it to the console.
    """
    print(fortune()) 
    print(futurePrediction("Alice"))
    print(compatibility_score("Ezio", "Altair"))
    print(get_lucky_number())


if __name__ == "__main__":
    main()
