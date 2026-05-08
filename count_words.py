import os
import pprint
from collections import OrderedDict

cwd = os.getcwd()
reserved = [".venv"]
strip_chars = "\t\n ()\"'[]{}.-:$#,/@"

def func(path: str, d: dict):
    dirs = os.listdir(path)

    for element in dirs:
        p = os.path.join(path, element)
        is_file = os.path.isfile(p)

        if is_file:
            name, ext = os.path.splitext(element)
            if ext != ".py":
                continue

            with open(p, "r") as file:
                content = file.read().split()
                for word in content:
                    word = word.strip(strip_chars)
                    if not word: continue
                    if word not in d:
                        d[word] = 0
                    d[word] += 1
        else:
            if element not in reserved:
                func(p, d)
    return d


result = func(cwd, {})
sorted_result = OrderedDict(sorted(result.items(), key=lambda x: x[1], reverse=True))
pprint.pprint(sorted_result)

