import random


words = ["JavaScript", "Microsoft", "Computer", "Backend", "Networking"]


def main():
    print("====== Hangman Game ======")
    print("Find the word...\n")

    word = random.choice(words).lower()
    found = [False] * len(word)
    attempts = 0

    while True:
        print()
        for i in range(len(word)):
            if found[i]:
                print(word[i], end="")
            else:
                print("_", end="")

        print()

        char = input("Enter a letter: ").lower()
        if len(char) != 1:
            print("Invalid input!")
            continue

        false_cnt = 0
        found_cnt = 0
        for i in range(len(word)):
            if word[i] == char:
                if not found[i]:
                    found_cnt += 1
                found[i] = True

            if not found[i]:
                false_cnt += 1

        if found_cnt > 0:
            print(f"Found {found_cnt} matches.")
        else:
            print("No matches.")
            attempts += 1

        if false_cnt == 0:
            break

    print(f"\nThe word: {word}")
    print(f"Attempts: {attempts}")


if __name__ == "__main__":
    main()
