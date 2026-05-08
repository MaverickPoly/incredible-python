import json
import os


BASE_DIR = os.getcwd()

def read_json_file(folder, filename):
    file_path = os.path.join(BASE_DIR, folder, filename)

    print(file_path)
    with open(file_path, "r") as file:
        return json.load(file)


def load_projects():
    return read_json_file("_data", "projects.json")


def load_blogs():
    return read_json_file("_data", "blogs.json")
