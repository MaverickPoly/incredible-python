import os

"""
Counts the total number of lines of code I have written throughout this huge project.
"""


cwd = os.getcwd()


def walk_dirs(directory):
    elements = os.listdir(directory)

    lines_of_code = 0


    for element in elements:
        is_dir = os.path.isdir(element)

        if not is_dir:
            root, extension = os.path.splitext(element)

            if extension == ".py":
                with open(os.path.join(directory, element), "r") as file:
                    content = file.read().split("\n")
                    size = len(content)
                    print(f"{os.path.join(directory, element)}: {size}")
                    # print(content)
                    lines_of_code += size
        else:
            print(element)
            lines_of_code += walk_dirs(os.path.join(directory, element))

    return lines_of_code


result = walk_dirs(cwd)
print(result)
