from fortune import fortune
from futurePredictions import futurePrediction
from compatibility_score import compatibility_score
from luckyNumber import get_lucky_number
from predictDay import predict_day

def main() -> None:
    while True:
        print("\n✨🔮✨==============================✨🔮✨")
        print("   Welcome to Fortune Luck Predictor!   ")
        print("✨🔮✨==============================✨🔮✨")
        print("        (づ｡◕‿‿◕｡)づ  ✨  🧙‍♂️  🍀  🦄  ")
        print("1. Get your fortune ✨")
        print("2. Predict your future 🔮")
        print("3. Predict your day ☀️")
        print("4. Compatibility score 💞")
        print("5. Get your lucky number 🍀")
        print("6. Exit 🚪")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            print("\nYour fortune:")
            print(fortune())
        elif choice == "2":
            name = input("Enter your name: ").strip()
            print(futurePrediction(name))
        elif choice == "3":
            day = input("Enter a day of the week: ").strip()
            try:
                print(predict_day(day))
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "4":
            name1 = input("Enter the first name: ").strip()
            name2 = input("Enter the second name: ").strip()
            print(compatibility_score(name1, name2))
        elif choice == "5":
            print("Your lucky number:")
            print(get_lucky_number())
        elif choice == "6":
            print("Goodbye! ✨")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
