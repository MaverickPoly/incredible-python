import time
import argparse


def countdown_timer(seconds: int):
    while seconds > 0:
        minutes, seconds = divmod(seconds, 60)

        formatted_text = f"{minutes:02}:{seconds:02}"
        print(formatted_text)

        time.sleep(1)
        seconds -= 1
    print("\n---- TIME IS UP! ----")


def main():
    parser = argparse.ArgumentParser(description="Countdown Timer")

    parser.add_argument("-s", "--seconds", type=int, required=True, help="The number of seconds.")
    args = parser.parse_args()
    countdown_timer(args.seconds)


if __name__ == '__main__':
    main()
