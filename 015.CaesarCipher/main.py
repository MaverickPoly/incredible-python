import string
import argparse

alphabet = string.ascii_uppercase + string.ascii_lowercase + \
    string.digits + string.punctuation


def encrypt(shift: int, text: str):
    shift %= len(alphabet)
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    mapping = {alphabet[i]: shifted_alphabet[i] for i in range(len(alphabet))}

    result = "".join(
        [mapping[char] if char in mapping else char for char in text])
    return result


def decrypt(shift: int, text: str):
    shift %= len(alphabet)
    shift = len(alphabet) - shift
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    mapping = {alphabet[i]: shifted_alphabet[i] for i in range(len(alphabet))}

    result = "".join(
        [mapping[char] if char in mapping else char for char in text])
    return result


def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher")

    subparsers = parser.add_subparsers(dest="command")

    encrypt_parser = subparsers.add_parser("encrypt")
    encrypt_parser.add_argument("shift", type=int, help="Shift number")
    encrypt_parser.add_argument("text", help="Text to encrypt")

    decrypt_parser = subparsers.add_parser("decrypt")
    decrypt_parser.add_argument("shift", type=int, help="Shift number")
    decrypt_parser.add_argument("text", help="Text to decrypt")

    args = parser.parse_args()

    if args.command == "encrypt":
        result = encrypt(args.shift, args.text)
        print(f"Encrypted text: {result}")
    elif args.command == "decrypt":
        result = decrypt(args.shift, args.text)
        print(f"Decrypted text: {result}")


if __name__ == "__main__":
    main()
