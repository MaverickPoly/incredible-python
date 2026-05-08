import os
import webbrowser

from jinja2 import Environment, FileSystemLoader


HTML_FILE_TEMPLATE = "template.html"
HTML_FILE_OUTPUT = "blog.html"

def main():
    try:
        title = input("Enter blog post title: ")
        author = input("Enter blog post author: ")
        content = input("Enter blog post content: ")

        data = {
            "title": title,
            "author": author,
            "content": content
        }

        env = Environment(loader=FileSystemLoader("."))
        template = env.get_template(HTML_FILE_TEMPLATE)
        rendered_html = template.render(data)

        with open(HTML_FILE_OUTPUT, "w") as file:
            file.write(rendered_html)

        abs_filepath = os.path.abspath(HTML_FILE_OUTPUT)
        webbrowser.open(f"file://{abs_filepath}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
