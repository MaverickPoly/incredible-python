import csv


class Todo:
    def __init__(self, title: str, completed: bool = False):
        self.title = title
        self.completed = completed

    def to_lst(self) -> list:
        return [self.title, self.completed]


FILENAME = "todos.csv"
todos: list[Todo] = []

# Utility functions


def save_todos():
    try:
        with open(FILENAME, "w") as file:
            writer = csv.writer(file)
            for todo in todos:
                writer.writerow(todo.to_lst())
    except Exception as e:
        print(f"Failed to save todos: {e}")


def load_todos():
    global todos
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            todos = [Todo(line[0], line[1] == "True") for line in reader]
    except Exception as e:
        print(f"Failed to load todos: {e}")


def get_todo_id(instruction: str) -> int:
    todo_id = input(f"Enter todo id to {instruction}: ")
    if not todo_id.isdigit():
        print("Invalid todo id!")
        return -1
    todo_id = int(todo_id)
    if todo_id > 0 and todo_id <= len(todos):
        return todo_id
    return -1


def main():
    load_todos()
    print("======== Welcome to CLI Todo List app ========")

    running = True
    while running:
        print("""\n
1. View Todos
2. Add Todo
3. Delete Todo
4. Complete Todo
5. Uncomplte Todo
6. Quit
""")
        option = input("Select an option: ")
        if option not in "123456":
            print("Invalid option!")
            continue

        option = int(option)

        match option:
            case 1:
                print(f"----- Todos {len(todos)} -----")
                for i, todo in enumerate(todos):
                    print(
                        f'{i + 1}) {todo.title} - {"✅" if todo.completed else "❌"}')
            case 2:
                title = input("Enter a todo title: ")
                if title == "":
                    print("Invalid title!")
                    continue
                new_todo = Todo(title)
                todos.append(new_todo)
                save_todos()
                print("Added new todo successfully!")
            case 3:
                todo_id = get_todo_id("delete")
                if todo_id == -1:
                    continue
                todos.pop(todo_id - 1)
                save_todos()
                print("Deleted todo successfully!")
            case 4:
                todo_id = get_todo_id("complete")
                if todo_id == -1:
                    continue
                todos[todo_id - 1].completed = True
                save_todos()
                print("Completed todo successfully!")
            case 5:
                todo_id = get_todo_id("uncomplete")
                if todo_id == -1:
                    continue
                todos[todo_id - 1].completed = False
                save_todos()
                print("Uncompleted todo successfully!")
            case 6:
                running = False

    print("\nQuitting...")


if __name__ == "__main__":
    main()
