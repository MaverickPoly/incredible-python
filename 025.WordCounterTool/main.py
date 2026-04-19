import argparse
import os.path


def main():
    parser = argparse.ArgumentParser(description="Word Counter CLI")

    subparsers = parser.add_subparsers(dest="command")

    file_parser = subparsers.add_parser("file")
    file_parser.add_argument("-f", "--filepath", required=True, help="File path")

    text_parser = subparsers.add_parser("text")
    text_parser.add_argument("text", help="Text to count words")

    args = parser.parse_args()

    match args.command:
        case "file":
            filepath = args.filepath
            if not os.path.exists(filepath):
                print("Invalid filepath!")
            else:
                with open(filepath, "r") as file:
                    word_count = 1
                    for line in file:
                        word_count += len(line.split())
                print(word_count)
        case "text":
            text = args.text
            word_count = len(text.split())
            print(word_count)


if __name__ == '__main__':
    main()
