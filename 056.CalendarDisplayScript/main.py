import calendar
import argparse


def main():
    parser = argparse.ArgumentParser(description="Calender Display Script")

    parser.add_argument("-y", "--year", type=int, help="Year to display")
    parser.add_argument("-m", "--month", type=int, help="Month to display")

    args = parser.parse_args()

    if args.year and args.month:
        year = args.year
        month = args.month

        display = calendar.month(year, month)
        print(display)
    elif args.year:
        year = args.year

        display = calendar.calendar(year)
        print(display)

if __name__ == '__main__':
    main()
