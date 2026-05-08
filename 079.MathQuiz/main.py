import random
import time


OPERATIONS = ["+", "-", "*", "/"]

def generate_problem() -> str:
    operation = random.choice(OPERATIONS)
    if operation == "*":
        number1 = random.randint(-20, 20)
        number2 = random.randint(-20, 20)
    elif operation == "/":
        number1 = random.randint(4, 1000)
        divisors = []
        for i in range(1, number1 + 1):
            if number1 % i == 0:
                divisors.append(i)

        number2 = random.choice(divisors)
    else:
        number1 = random.randint(-100, +200)
        number2 = random.randint(-100, +200)

    return f"{number1} {operation} {number2}"


def main():
    try:
        print("======== Math Quiz Generator ========")
        n = int(input("Enter the number of problems: "))

        problems = [generate_problem() for _ in range(n)]
        correct_lst = [False] * n

        start_time = time.time()

        for i in range(n):
            problem = problems[i]
            result = eval(problem)
            answer = int(input(f"{i + 1}. {problem} = "))

            if answer == result:
                correct_lst[i] = True

        end_time = time.time()
        duration = round(end_time - start_time)

        # Display wrong problems
        print()
        print(f"Performance: {sum(correct_lst)}/{n}")
        print(f"Duration: {duration} seconds")
        print("Problems you got wrong:")
        for i in range(n):
            if not correct_lst[i]:
                result = eval(problems[i])
                print(f"{problems[i]} = {result}")
    except ValueError as e:
        print(f"Invalid value: {e}")


if __name__ == '__main__':
    main()
