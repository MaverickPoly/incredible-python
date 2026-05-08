from flask import Flask, render_template
from _data import *

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/projects")
def projects_page():
    projects = load_projects()
    return render_template("projects.html", projects=projects)


@app.route("/blogs")
def blogs_page():
    blogs = load_blogs()
    return render_template("blogs.html", blogs=blogs)


@app.errorhandler(code_or_exception=404)
def not_found_error(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(debug=True)
