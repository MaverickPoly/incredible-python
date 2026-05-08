import argparse


def hash_f(source: str):
    s = 0
    for char in source:
        s += ord(char)
    return s * len(source)


def main():
    parser = argparse.ArgumentParser(description="Simple Hashing tool")

    parser.add_argument("text", help="Text to hash")

    args = parser.parse_args()

    hash_result = hash_f(args.text)
    print(hash_result)


if __name__ == '__main__':
    main()
    hash()
