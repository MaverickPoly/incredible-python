import pyperclip


FILENAME = "081.UnitTesting/main.py"

with open(FILENAME, "r") as file:
    content = file.read()
    pyperclip.copy(content)


# Just exploring docstrings ... :)
def func(a, b, c) -> bool:
    """

    :param a:
    :param b:
    :param c:
    :return:
    """