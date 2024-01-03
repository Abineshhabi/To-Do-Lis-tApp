import random

def roll_dice():
    return random.randint(1, 6)  # Change the range for different types of dice

def main():
    while True:
        input("Press Enter to roll the dice... (Press 'q' to quit)")

        roll_result = roll_dice()
        print(f"You rolled: {roll_result}")

        choice = input("Roll again? (Press 'q' to quit)").lower()
        if choice == 'q':
            break

if __name__ == "__main__":
    main()
