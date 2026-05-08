from datetime import datetime


def calculate_age():
    try:
        year = int(input("Enter your birth year: "))
        month = int(input("Enter your birth month: "))
        day = int(input("Enter your birth day: "))

        today = datetime.today()
        birth_date = datetime(year, month, day)

        age = today.year - birth_date.year

        birth_cnt = 30 * month + day
        today_cnt = 30 * today.month + today.day
        if today_cnt < birth_cnt:
            age -= 1

        print(f"Your age: {age}")
    except Exception as e:
        print(f"Error parsing input: {e}")


if __name__ == '__main__':
    calculate_age()
