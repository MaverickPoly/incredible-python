import csv
import os.path
from datetime import datetime


def from_input() -> dict[str, str]:
    try:
        number_of_birthdays = int(input("Enter the number of birthdays: "))
        print("Enter birthdays in format 'mm-dd'")

        birthdays = {}

        for i in range(number_of_birthdays):
            name = input("Enter name of a person: ")
            birthday = input(f"Enter birthday {i + 1}: ")
            birthdays[name] = birthday

        return birthdays
    except ValueError as e:
        print(f"Invalid input: {e}")
        return {}


def from_file() -> dict[str, str]:
    try:
        filepath = input("Enter filepath: ")

        if not os.path.exists(filepath):
            print("Invalid filepath!")
            return {}

        file, ext = os.path.splitext(filepath)
        print(ext)
        if ext != ".csv":
            print("Only csv file is supported!")
            return {}


        birthdays = {}
        with open(filepath, "r") as file:
            reader = csv.reader(file)
            for line in reader:
                name, birthday = line
                birthdays[name] = birthday
        return birthdays
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}


def display(birthdays: dict[str, str]):
    today = datetime.today().strftime("%m-%d")

    for name, birthday in birthdays.items():
        if birthday == today:
            print(f"{name} - {birthday}")


def main():
    choice = input("From file (1) or input (2): ")

    if choice == "1":
        display(from_file())
    elif choice == "2":
        display(from_input())
    else:
        print("Invalid choice!")


if __name__ == '__main__':
    main()
