import json
import random
import time

WORDS_FILE = "words.json"  # File containing a list of English words for use


def load_words() -> list[str]:
    with open(WORDS_FILE, "r") as file:
        words = json.load(file)
        return words

def generate_words(n: int) -> str:
    words = load_words()
    return " ".join(random.choices(words, k=n))


def main():
    try:
        n = int(input("Number of words: "))

        words = generate_words(n)
        print(words)
        print("Type...")

        start = time.time()
        inp = input()
        end = time.time()

        # Count the correct words
        words_lst = words.split()
        inp_lst = inp.split()
        correct_count = 0
        for word, inp in zip(words_lst, inp_lst):
            if word == inp:
                correct_count += 1


        duration = end - start  # In Seconds
        wpm = round(n / (duration / 60))

        print(f"\nYour WPM: {wpm}")
        print(f"Correct: {correct_count}/{n}")
    except ValueError as e:
        print("Invalid input!")


if __name__ == '__main__':
    main()
