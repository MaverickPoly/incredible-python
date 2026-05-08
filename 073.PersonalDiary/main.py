from jinja2 import Environment, FileSystemLoader

import argparse
from datetime import datetime
import re
import os
import webbrowser

from write_window import WriterApp


FILENAME = "diary.txt"
HTML_TEMPLATE_FILE = "template.html"
HTML_OUTPUT_FILE = "index.html"


def handle_write_diary():
    content = ""
    def send_text(txt: str):
        nonlocal content
        content = txt

    _ = WriterApp(send_text)

    if not content:
        print("No content was provided(")
        return
    else:
        today = datetime.today().strftime("%d-%m-%y")
        with open(FILENAME, "a") as file:
            file.write("=" * 30 + "\n")
            file.write(today + "\n")
            file.write(content + "\n")

def _read_diary_file() -> str:
    with open(FILENAME, "r") as file:
        content = file.read()
        return content


def handle_read_diary():
    content = _read_diary_file()
    print(content)


def handle_open_web():
    env = Environment(loader=FileSystemLoader("."))

    pattern = r"^\d{2}-\d{2}-\d{2}$"
    # [(date, content)...]
    data = []
    content = _read_diary_file().split("\n")

    current_date, current_content = None, None
    for line in content:
        if line == "=" * 30:
            current_date, current_content = None, None
            continue

        if re.match(pattern, line):
            current_date = line
        else:
            current_content = line

        if current_date and current_content:
            data.append((current_date, current_content))


    template = env.get_template(HTML_TEMPLATE_FILE)
    rendered_html = template.render(data=data)

    with open(HTML_OUTPUT_FILE, "w") as file:
        file.write(rendered_html)

    abs_filepath = os.path.abspath(HTML_OUTPUT_FILE)
    webbrowser.open(f"file://{abs_filepath}")


def main():
    parser = argparse.ArgumentParser(description="Daily Diary CLI App!")

    subparsers = parser.add_subparsers(dest="command")

    write_parser = subparsers.add_parser("write", help="Write new diary entry")
    read_parser = subparsers.add_parser("read", help="Read all diary entries")
    web_parser = subparsers.add_parser("web", help="Open a webview")

    args = parser.parse_args()

    match args.command:
        case "write":
            handle_write_diary()
        case "read":
            handle_read_diary()
        case "web":
            handle_open_web()


if __name__ == '__main__':
    main()
