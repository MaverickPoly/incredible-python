def is_leap_year(year: int):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def main():
    try:
        year = int(input("Enter a year to check: "))
        if is_leap_year(year):
            print("LEAP")
        else:
            print("NOT LEAP")
    except ValueError as e:
        print(f"Invalid year!")


if __name__ == '__main__':
    main()
