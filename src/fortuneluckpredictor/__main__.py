"""
Entry point for the fortuneluckpredictor package when run as a script.
"""

from .fortune import fortune


def main() -> None:
    """
    Fetch a fortune and print it to the console.
    """
    print(fortune()) # in terminal: python -m fortuneluckpredictor will call this function


if __name__ == "__main__":
    main()
