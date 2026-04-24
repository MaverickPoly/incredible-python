"""
Student Grade Calculator for my lyceum :)
"""

def is_float(txt: str):
    try:
        float(txt)
        return True
    except:
        return False


def main():
    number = input("The number of subjects: ")

    if not number.isdigit():
        print("Invalid input!")
        return

    number = int(number)

    grades = []
    for i in range(number):
        grade = input(f"Grade of subject {i + 1}: ")
        if not is_float(grade):
            print("Invalid input!")
            return
        grade = float(grade)
        if grade <= 0 or grade > 5:
            print("Invalid grade!")
            return
        grades.append(grade)

    average = round(sum(grades) / len(grades), 2)

    print(f"Average: {average}")
    print(f"Performance: {round(average * 20, 2)}")  # out of 100


if __name__ == '__main__':
    main()
