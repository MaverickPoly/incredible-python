import os


"""
Makes a file distribution by their types
Example:
.py: 114
.html: 19
.json: 8
.txt: 7
.png: 6
.csv: 5
.db: 5
.js: 3
.mp3: 2
.md: 1
.pdf: 1
.css: 1
"""


cwd = os.getcwd()

collection = {}
ignore_folders = [".venv", "__pycache__", ".idea", ".git"]

def walk_dirs(directory):
    elements = os.listdir(directory)

    for element in elements:
        full_path = os.path.join(directory, element)
        is_folder = os.path.isdir(full_path)

        if is_folder and element not in ignore_folders:
            walk_dirs(full_path)
        else:
            root, extension = os.path.splitext(element)

            if not extension:
                continue

            if extension in collection:
                collection[extension].append(root)
            else:
                collection[extension] = [root]


walk_dirs(cwd)
# print(collection)

collection = dict(sorted(collection.items(), key=lambda val: len(val[1]), reverse=True))
for ext, el in collection.items():
    print(f"{ext}: {len(el)}")
