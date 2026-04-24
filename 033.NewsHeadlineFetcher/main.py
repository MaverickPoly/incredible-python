import argparse
import os
import pprint
import datetime

import dotenv
import requests


dotenv.load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")
# print(API_KEY)
# print(os.environ.get("NEWS_API_KEY"))

COUNTRY_URL = "https://newsapi.org/v2/top-headlines"
# https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=...

QUERY_URL = "https://newsapi.org/v2/everything"
# https://newsapi.org/v2/everything?q=tesla&from=2026-03-21&sortBy=publishedAt&apiKey=...

class News:
    def __init__(self, author, content, description, publishedAt, source, title, url, urlToImage):
        self.author = author
        self.content = content
        self.description = description
        self.published_at = publishedAt
        self.source = source
        self.title = title
        self.url = url
        self.url_to_image = urlToImage


def display_new(new: News):
    print(f"""
{f'==== {new.title} - {new.author} ====' if new.author else f'==== {new.title} ===='}
{new.content}

{new.description}

- Published: {new.published_at}
{new.url}
""")


def main():
    parser = argparse.ArgumentParser(description="")

    subparsers = parser.add_subparsers(dest="command")

    country_parser = subparsers.add_parser("country", help="Fetch news for a specific country")
    country_parser.add_argument("country", help="Country")

    query_parser = subparsers.add_parser("query", help="Fetch news for with a specific query")
    query_parser.add_argument("query", help="Query")

    args = parser.parse_args()

    if args.command == "country":
        try:
            url = COUNTRY_URL + f"?country={args.country}&apiKey={API_KEY}"
            response = requests.get(url)
            json_data = response.json()
            articles = json_data.get("articles", [])
            # pprint.pprint(json_data)
            news = [News(**element) for element in articles]

            if news:
                for new in news:
                    display_new(new)
            else:
                print("No news found(")
        except Exception as e:
            print(f"Failed to fetch news: {e}")
    elif args.command == "query":
        try:
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            url = QUERY_URL + f"?q={args.query}&from={today}&sortBy=publishedAt&apiKey={API_KEY}"
            response = requests.get(url)
            json_data = response.json()
            articles = json_data.get("articles", [])
            # pprint.pprint(json_data)
            news = [News(**element) for element in articles]

            if news:
                for new in news:
                    display_new(new)
            else:
                print("No news found(")
        except Exception as e:
            print(f"Failed to fetch news: {e}")


if __name__ == '__main__':
    main()
