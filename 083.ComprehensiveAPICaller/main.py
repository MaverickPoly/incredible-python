import pprint
import random

import requests


BASE_URL = "https://json-placeholder-olive.vercel.app"


class APICaller:
    def __init__(self, base_url: str):
        self.base_url = base_url

    @staticmethod
    def _get_request(url: str, params=None, headers=None):
        if headers is None:
            headers = {}
        if params is None:
            params = {}
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        json_data = response.json()
        return json_data

    def fetch_users(self):
        users = self._get_request(f"{self.base_url}/users")
        return users

    def fetch_posts(self):
        posts = self._get_request(f"{self.base_url}/posts")
        return posts

    def fetch_todos(self):
        todos = self._get_request(f"{self.base_url}/todos")
        return todos

    def fetch_comments(self):
        comments = self._get_request(f"{self.base_url}/comments")
        return comments



def main():
    api = APICaller(BASE_URL)

    users = api.fetch_users()
    print(f"Length: {len(users)}")
    pprint.pprint(f"User: {random.choice(users)}\n")

    posts = api.fetch_posts()
    print(f"Length: {len(posts)}")
    pprint.pprint(f"Post: {random.choice(posts)}\n")

    todos = api.fetch_todos()
    print(f"Length: {len(todos)}")
    pprint.pprint(f"Todos: {random.choice(todos)}\n")

    comments = api.fetch_comments()
    print(f"Length: {len(comments)}")
    pprint.pprint(f"Comments: {random.choice(comments)}\n")


if __name__ == '__main__':
    main()
