from flask import Blueprint, render_template



bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/")
def index():
    """Home Page"""
    return render_template("main/index.html")

