questions = [
    {
        "prompt": "What is the correct file extension for Python bulk_files?",
        "options": ["A. py", "B. js", "C. html", "D. txt"],
        "answer": "A",
    },
    {
        "prompt": "Which keyword is used to create function in Python?",
        "options": ["A. void", "B. def", "C. func", "D. int"],
        "answer": "B",
    },
    {
        "prompt": "Which data type is used to store 'True' and 'False'?",
        "options": ["A. int", "B. str", "C. bool", "D. float"],
        "answer": "C",
    },
    {
        "prompt": "Which keyword is used to identify the type of a variable?",
        "options": ["A. typeof", "B. getType", "C. id", "D. type"],
        "answer": "D",
    }
]


def main():
    print("====== Welcome to quiz app ======")
    print("=" * 40)

    score = 0

    for i, question in enumerate(questions):
        print(f"\nQuestion {i + 1}: {question['prompt']}")
        for option in question["options"]:
            print(option)
        user_inp = input("Answer: ").upper()

        if user_inp == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer:", question["answer"])

    print(f"\nScore: {score}")


if __name__ == "__main__":
    main()
