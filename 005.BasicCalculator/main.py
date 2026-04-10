import argparse


def main():
    parser = argparse.ArgumentParser(description="CLI Calculator")

    parser.add_argument("num1", type=float, help="Number 1")
    parser.add_argument("num2", type=float, help="Number 2")

    parser.add_argument("-a", "--add", action="store_true", help="Addition.")
    parser.add_argument("-s", "--subtract",
                        action="store_true", help="Subtraction.")
    parser.add_argument("-m", "--multiply",
                        action="store_true", help="Multiplication.")
    parser.add_argument(
        "-d", "--divide", action="store_true", help="Division.")

    args = parser.parse_args()
    number1, number2 = args.num1, args.num2

    result = 0
    if args.add:
        result = number1 + number2
    elif args.subtract:
        result = number1 - number2
    elif args.multiply:
        result = number1 * number2
    elif args.divide:
        if number2 == 0:
            print("Cannot divide by zero!")
            return
        result = number1 / number2
    print(result)


if __name__ == "__main__":
    main()
