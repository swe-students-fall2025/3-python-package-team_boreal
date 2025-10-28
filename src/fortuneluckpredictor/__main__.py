"""
Entry point for the fortuneluckpredictor package when run as a script.
"""

from .fortune import fortune
from .futurePredictions import futurePrediction


def main() -> None:
    """
    Fetch a fortune and print it to the console.
    """
    print(fortune()) 
    print(futurePrediction("Alice"))


if __name__ == "__main__":
    main()
