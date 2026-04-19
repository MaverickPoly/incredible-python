def start_game():
    print("--- WELCOME TO THE MYSTERY OF PYTHON WOOD ---")
    print("You wake up at the edge of a dark, misty forest.")
    print("You only have a flashlight and a sense of regret.\n")
    first_choice()


def first_choice():
    print("There are two paths ahead of you:")
    print("1. A narrow path leading into the thick trees.")
    print("2. A wider path following a dried-up riverbed.")

    choice = input("\nWhich path do you take? (1 or 2): ")

    if choice == "1":
        forest_path()
    elif choice == "2":
        river_path()
    else:
        print("Invalid choice. A wolf stares at you until you pick.")
        first_choice()


def forest_path():
    print("\nThe trees close in around you. You hear a strange humming.")
    print("You find a glowing blue mushroom.")

    choice = input("Do you 'eat' it or 'ignore' it? ").lower().strip()

    if "eat" in choice:
        print("\nPlot twist! The mushroom gives you the ability to speak to trees.")
        print("The trees guide you safely home. YOU WIN!")
    else:
        print("\nYou walk past it, but get hopelessly lost in the dark.")
        game_over("You became a permanent resident of the forest.")


def river_path():
    print("\nThe riverbed is rocky. You see an abandoned cabin.")
    print("The door is slightly ajar.")

    choice = input("Do you 'enter' or 'run' away? ").lower().strip()

    if "enter" in choice:
        print("\nInside, you find a pile of gold and a map out of the woods!")
        print("YOU WIN!")
    else:
        game_over("You ran into a bear while fleeing. Not your best move.")


def game_over(reason):
    print(f"\n💀 GAME OVER: {reason}")
    play_again = input("Try again? (y/n): ").lower()
    if play_again == 'y':
        start_game()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    start_game()
