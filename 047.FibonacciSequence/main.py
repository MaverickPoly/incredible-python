def fibonacci_n(n):
    """
    Recursive function
    Runtime complexity: O(2^n)
    """
    if n <= 2:
        return 1
    return fibonacci_n(n - 1) + fibonacci_n(n -  2)


def generate_fibonacci(n: int):
    """Runtime complexity: O(n)"""
    sequence = [1, 1]

    for i in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def main():
    for i in range(1, 11):
        print(f"Fibonacci {i}: {fibonacci_n(i)}")

    print()
    print(generate_fibonacci(10))


if __name__ == '__main__':
    main()
