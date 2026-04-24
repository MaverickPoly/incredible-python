import argparse


def is_palindrome(text: str):
    return text == text[::-1]


def main():
    parser = argparse.ArgumentParser(description="Palindrome Checker")

    parser.add_argument("text", help="Text to check for palindrome")

    args = parser.parse_args()

    if is_palindrome(args.text):
        print("Your text is palindrome!")
    else:
        print("Your text is NOT palindrome!")


if __name__ == '__main__':
    main()
