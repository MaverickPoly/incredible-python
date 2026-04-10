from random import randint


def main():
    print("Welcome to number guessing game!")
    print("================================")

    running = True
    current_round = 0

    while running:
        current_round += 1
        print(f"\n====== Round {current_round} ======")
        random_number = randint(1, 99)

        attempts = 0

        while True:
            guess = input("Take a guess: ")

            if not guess.isdigit():
                print("Invalid guess! Try again...")
                continue

            guess = int(guess)
            attempts += 1
            if guess == random_number:
                print("Correct!")
                print(f"The answer was {random_number}")
                print(f"It took you {attempts} attempts to find it.")
                break
            elif guess > random_number:
                print("Too high!")
            else:
                print("Too low!")

        choice = input("Do you wanna play again(y/n): ")
        if choice.lower() == "n":
            running = False

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
