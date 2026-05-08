import os


cwd = "/home/maverick"


def ls_func():
    elements = os.listdir(cwd)

    for element in elements:
        is_file = os.path.isfile(element)
        if is_file:
            print(f"- {element}")
        else:
            print(f"= {element}")


def cd_func(cur_dir: str):
    global cwd

    if not cur_dir.startswith("/home/maverick") and cur_dir.startswith("/"):
        cur_dir = f"{cwd}{cur_dir}"

    try:
        os.chdir(cur_dir)
        cwd = os.getcwd()
    except Exception as e:
        print(f"Invalid path: {cur_dir}")

def pwd_func():
    print(cwd)

def mkdir_func(new_dir: str):
    try:
        os.mkdir(new_dir)
    except Exception as e:
        print(f"Error creating folder: {e}")


def main():
    running = True

    while running:
        inp = input(f"{cwd}> ")

        commands = inp.split()

        if len(commands) == 0:
            print("Invalid input!")
            continue

        match commands[0]:
            case "ls":
                if len(commands) == 2:
                    ls_func()
                elif len(commands) == 1:
                    ls_func()
                else:
                    print("Invalid arguments")
            case "cd":
                if len(commands) == 2:
                    cd_func(commands[1])
                else:
                    print("Invalid arguments")
            case "pwd":
                if len(commands) == 1:
                    pwd_func()
                else:
                    print("Invalid arguments")
            case "mkdir":
                if len(commands) == 2:
                    mkdir_func(commands[1])
                else:
                    print("Invalid arguments")
            case "q" | "quit":
                running = False
            case _:
                print(f"Invalid command: {commands[0]}")


if __name__ == '__main__':
    main()
