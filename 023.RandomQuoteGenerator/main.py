from random import choice
import requests
import pprint

URL = "https://dummyjson.com/quotes"

class Quote:
    def __init__(self, id: int, author: str, quote: str):
        self.id = id
        self.author = author
        self.quote = quote

    @staticmethod
    def from_dict(d: dict) -> Quote:
        return Quote(d["id"], d["author"], d["quote"])


def main():
    response = requests.get(URL)

    json_data = response.json()
    quotes = [Quote.from_dict(quote_dict) for quote_dict in json_data["quotes"]]

    # Get Random Quote
    random_quote = choice(quotes)
    print(f"------ Random quote ------")
    print(random_quote.quote)
    print(f"Author: {random_quote.author}")
    # pprint.pprint(json_data["quotes"])


if __name__ == '__main__':
    main()
