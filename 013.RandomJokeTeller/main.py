import requests


URL = "https://official-joke-api.appspot.com/random_joke"


def fetch_random_joke() -> tuple[str, str]:
    response = requests.get(URL)
    data = response.json()
    return data["setup"], data["punchline"]


def main():
    print("===== Random Joke Teller =====")
    print("-" * 30)

    while True:
        choice = input("\nPress enter to display a joke...(q to quit) ")

        if choice == "q":
            break

        random_joke = fetch_random_joke()

        print(random_joke[0])
        print(random_joke[1])


if __name__ == "__main__":
    main()
