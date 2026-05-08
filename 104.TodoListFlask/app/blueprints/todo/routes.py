from flask import Blueprint, render_template, url_for, request, redirect, flash, abort, jsonify
from flask_login import current_user, login_required
from app import db
from app.models import Todo


bp = Blueprint("todos", __name__, url_prefix="/todos")


@bp.route("/")
@login_required
def view():
    """Fetch and display all the todos"""
    todos = Todo.query.filter_by(user_id=current_user.id).order_by(Todo.created_at.desc())

    return render_template("todos/todos.html", todos=todos)

@bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    """Create a new todo"""
    if request.method == "POST":
        title = request.form.get("title")

        if not title:
            flash("Title not provided!", "error")
            return redirect(url_for("todo.create"))

        todo = Todo(title=title, user_id=current_user.id)
        db.session.add(todo)
        db.session.commit()

        flash("Todo created successfully!", "success")
        return redirect(url_for("todos.view"))
    else:
        return render_template("todos/create.html")


# Delete todo
@bp.route("/<int:id>/delete", methods=["DELETE"])
@login_required
def delete(id):
    todo = Todo.query.get_or_404(id)

    if todo.user_id != current_user.id:
        abort(403)

    db.session.delete(todo)
    db.session.commit()

    return jsonify({"message": "Todo deleted successfully!"})

# Toggle complete todo
# TODO: modify it to use PATCH method instead of POST
@bp.route("/<int:id>/toggle", methods=["PATCH"])
@login_required
def toggle_complete(id):
    todo = Todo.query.get_or_404(id)

    if todo.user_id != current_user.id:
        abort(403)

    todo.completed = not todo.completed
    db.session.commit()
    return jsonify({"message": "Completed status toggled successfully!"})
