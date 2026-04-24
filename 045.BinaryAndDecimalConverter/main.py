def binary_to_decimal(binary):
    size = len(binary)
    binary = str(binary)
    result = 0

    for i in range(size):
        if binary[i] == "1":
            result += 2 ** (size - i - 1)
    return result

def decimal_to_binary(decimal):
    result = ""

    while decimal:
        remainder = decimal % 2
        result += str(remainder)
        decimal //= 2

    return result[::-1]


def main():
    binaries = []
    for i in range(1, 10):
        binary_val = decimal_to_binary(i)
        print(f"{i}: {binary_val}")
        binaries.append(binary_val)

    print()
    for binary in binaries:
        print(f"{binary}: {binary_to_decimal(binary)}")


if __name__ == '__main__':
    main()
