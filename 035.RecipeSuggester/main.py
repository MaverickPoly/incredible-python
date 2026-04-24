"""
Frankly, I do not know exactly how to implement recipe suggester mechanism.
Therefore, I decided to simply implement an application that fetches a list of recipes from a remote API
than selects a random one among them :(
"""

import argparse
import os

import dotenv
import requests

dotenv.load_dotenv()
API_NINJAS_API=os.getenv("API_NINJAS_API")

URL = "https://api.api-ninjas.com/v3/recipe"


def main():
    parser = argparse.ArgumentParser(description="Recipe Suggester!")

    parser.add_argument("title", help="Title of a recipe")
    args = parser.parse_args()

    response = requests.get(f"{URL}?title={args.title}", headers={"X-Api-Key": API_NINJAS_API})
    response.raise_for_status()

    json_data = response.json()

    for idx, recipe in enumerate(json_data, start=1):
        print(f"====== Recipe {idx} ======")
        print(recipe["title"])
        print("Instruction:")
        for j, instruction in enumerate(recipe["instructions"], start=1):
            print(f"{j}. {instruction}")
        print("Ingredients:")
        for ingredient in recipe["ingredients"]:
            print(f"- {ingredient['name']}")
        print()


if __name__ == '__main__':
    main()
