import random


def get_response(text: str):
    rules = {
        "hi,hello,hey": ["Hello! How can I help you?", "Hello dude!", "Greetings!"],
        "how are you": ["I am doing great! Thanks for asking!", "I am just a program but I am doing great!"],
        "your name": ["I am Sparky, your friendly python assistant!", "You can call me Sparky."],
        "bye,goodbye,exit": ["Goodbye", "Have a great day!", "See you!"],
        "weather": ["The weather is sunny!", "The weather is good as always!"],
    }

    for key in rules.keys():
        lst = key.split(",")
        for item in lst:
            if text in item:
                return rules[key]

    return ["Sorry, I cannot understand that command yet :("]


def main():
    running = True
    while running:
        user_input = input("Enter a command: ").strip().lower()
        if user_input in ["quit", "stop", "bye", "exit"]:
            running = False
        responses = get_response(user_input)
        response = random.choice(responses)

        print("Sparky:", response)


if __name__ == '__main__':
    main()
