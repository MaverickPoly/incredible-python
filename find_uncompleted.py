import os


projects = [False] * 300

elements = os.listdir(os.getcwd())

for element in elements:
    full_path = os.path.join(os.getcwd(), element)
    is_dir = os.path.isdir(full_path)

    if is_dir:
        split = element.split(".")
        if len(split) != 2:
            continue

        num, title = split
        if not num: continue

        num = num.lstrip("0")
        num = int(num)
        projects[num - 1] = True


print("Projects not yet completed:")
for i in range(100):
    if not projects[i]:
        print(i + 1)
