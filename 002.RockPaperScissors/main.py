from random import choice


acronims = {"r": "rock", "p": "paper", "s": "scissors"}
options = ["r", "p", "s"]
win_combinations = ["rs", "pr", "sp"]

WIN = "win"
LOST = "lost"
DRAW = "draw"


def get_status(user_choice, computer_choice):
    if user_choice == computer_choice:
        return DRAW
    combined = user_choice + computer_choice
    if combined in win_combinations:
        return WIN
    return LOST


def main():
    print("Welcome to Rock Paper Scissors Game!")
    print("====================================")

    current_round = 0
    running = True
    user_score = 0
    computer_score = 0

    while running:
        current_round += 1
        print(f"\n====== Round {current_round} ======")
        computer_choice = choice(options)

        # Get User's choice
        user_choice = None
        while True:
            user_choice = input("Your choice(r, p, s): ")
            if user_choice not in options:
                print("Invalid choice! Try again...")
                continue
            break

        status = get_status(user_choice, computer_choice)
        if status == WIN:
            print("You won!")
            user_score += 1
        elif status == LOST:
            print("You lost!")
            computer_score += 1
        else:
            print("Draw!")

        print(f"You: {acronims[user_choice]} | Computer: {
            acronims[computer_choice]}")
        print(f"Your score: {user_score} | Computer Score: {computer_score}")

        again_choice = input("Do you wanna play again(y/n)? ")
        if again_choice.lower() == "n":
            running = False

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
