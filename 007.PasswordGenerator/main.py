import argparse
import string
import random


def main():
    parser = argparse.ArgumentParser(description="Random password generator!")

    parser.add_argument("n", type=int, nargs="?",
                        default=8, help="Length of password.")
    parser.add_argument("-l", "--lowercase", action="store_true",
                        help="Include lowercase letters.")
    parser.add_argument("-u", "--uppercase", action="store_true",
                        help="Include uppercase letters.")
    parser.add_argument(
        "-d", "--digits", action="store_true", help="Include digits.")
    parser.add_argument("-p", "--punctuations",
                        action="store_true", help="Include punctuations.")

    args = parser.parse_args()

    combinations = ""
    if args.lowercase:
        combinations += string.ascii_lowercase
    if args.uppercase:
        combinations += string.ascii_uppercase
    if args.digits:
        combinations += string.digits
    if args.punctuations:
        combinations += string.punctuation

    if not combinations:
        print("Combinations is empty!")
        return

    random_password = "".join(random.choices(combinations, k=args.n))
    print("Password:")
    print(random_password)


if __name__ == "__main__":
    main()
