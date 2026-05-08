import argparse
import json
import random
import string

FILENAME = "urls.json"
COMBINATIONS = string.ascii_lowercase + string.ascii_uppercase + string.digits

def _generate_uid(size=10) -> str:
    result = "".join(random.choices(COMBINATIONS, k=size))
    return result


def shorten_url(url: str):
    urls = fetch_urls()
    ids_list = [element["uid"] for element in urls]

    uid = _generate_uid()
    while uid in ids_list:
        uid = _generate_uid()

    new_data = {"url": url, "uid": uid}
    urls.append(new_data)

    with open(FILENAME, "w") as file:
        json.dump(urls, file)


def fetch_urls() -> list[dict]:
    with open(FILENAME, "r") as file:
        data = json.load(file)
        return data

def get_url(uid: str):
    urls = fetch_urls()

    for element in urls:
        if element["uid"] == uid:
            return element["url"]
    return ""


def main():
    parser = argparse.ArgumentParser(description="Basic URL Shortener!")

    subparsers = parser.add_subparsers(dest="command")

    shorten_parser = subparsers.add_parser("shorten", help="Shorten the url")
    shorten_parser.add_argument("url", help="URL to shorten")

    fetch_parser = subparsers.add_parser("fetch", help="Fetch all shortened urls")

    get_url_parser = subparsers.add_parser("get_url", help="Get url with specific uid")
    get_url_parser.add_argument("uid", help="Shortened url 'uid' to access original url")

    args = parser.parse_args()

    match args.command:
        case "shorten":
            shorten_url(args.url)
            print("URL Shortened successfully!")
        case "fetch":
            urls = fetch_urls()
            print("URLS:")
            for element in urls:
                print(f"{element['uid']}: {element['url']}")
        case "get_url":
            url = get_url(args.uid)
            if url:
                print(url)
            else:
                print("Invalid url!")


if __name__ == '__main__':
    main()
