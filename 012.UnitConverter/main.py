import sys


VALUE = 0.621


def is_float(string: str):
    try:
        float(string)
        return True
    except ValueError:
        return False


def get_value(text: str):
    inp = input(text)
    if not is_float(inp):
        print("Invalid value!")
        sys.exit()
    return float(inp)


def main():
    print("1. Miles to Kilometers")
    print("2. Kilometers to miles")

    choice = input("Select (1/2): ")

    if choice == "1":
        result = get_value("Miles: ") / VALUE
        print(f"{result:.2f} kilometers")
    elif choice == "2":
        result = get_value("Kilometers: ") * VALUE
        print(f"{result:.2f} miles")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
