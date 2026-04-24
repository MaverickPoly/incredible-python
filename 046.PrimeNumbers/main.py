def is_prime(number: int) -> bool:
    if number <= 1: return False
    if number <= 3: return True
    if number % 2 == 0 or number % 3 == 0: return False
    i = 5

    while i * i <= number:
        if number % i == 0 or (number + 2) % i == 0:
            return False
        i += 6
    return True


def is_prime_2(number: int) -> bool:
    i = 2
    while i * i <= number:
        if number % i == 0: return False
        i += 1
    return True


def generate_primes(n):
    """
    Sieve of Eratosthenes algorithm would be the most viable approach here.
    But unfortunately, I do not know it :(
    Thus, I will try to use some other algorithm of mine...
    """
    current = 2
    cnt = 0
    primes = []

    while cnt != n:
        if is_prime(current):
            primes.append(current)
            cnt += 1
        current += 1
    return primes


def main():
    for i in range(1, 30):
        print(f"is_prime({i}) -> {is_prime(i)}")

    print()
    print(generate_primes(10))

if __name__ == '__main__':
    main()

