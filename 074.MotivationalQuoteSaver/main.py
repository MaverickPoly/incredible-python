import random
import sqlite3
import argparse


DATABASE_FILE = "./quotes.db"


class Quote:
    def __init__(self, id: int, quote: str, author: str):
        self.id = id
        self.quote = quote
        self.author = author

    @staticmethod
    def from_tuple(t: tuple[str, str, str]):
        return Quote(int(t[0]), t[1], t[2])

    def __repr__(self):
        return f"\"{self.quote}\" - {self.author}"



def init_db():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            author TEXT NOT NULL
        )
        """)


def fetch_quotes():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cur = conn.cursor()
        cur.execute("""
        SELECT * FROM quotes
        """)
        return [Quote.from_tuple(t) for t in cur.fetchall()]

def add_quote(quote: str, author: str):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO quotes (content, author) VALUES (?, ?)
        """, (quote, author))


def main():
    parser = argparse.ArgumentParser(description="Motivational Quote Saver")
    init_db()

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add new quote")
    add_parser.add_argument("quote", help="Quote content")
    add_parser.add_argument("author", help="Quote author")

    fetch_parser = subparsers.add_parser("fetch", help="Fetch all quotes")
    fetch_parser.add_argument("-r", "--random", action="store_true", help="Random quote")

    args = parser.parse_args()

    if args.command == "add":
        add_quote(args.quote, args.author)
    elif args.command == "fetch":
        quotes = fetch_quotes()
        if args.random:
            print(random.choice(quotes))
        else:
            print("==== Quotes ====")
            for quote in quotes:
                print(quote)


if __name__ == '__main__':
    main()
