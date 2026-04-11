import random


def main():
    print("---- Welcome to dice rolling simulator ----")

    while True:
        user_input = input("Press enter to roll the dice...('q' to quit)")
        if user_input == "q":
            break

        result = random.randint(1, 6)
        print(f"You rolled a: {result}")


if __name__ == "__main__":
    main()
