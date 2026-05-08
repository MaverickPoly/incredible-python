from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import login_user, current_user, login_required, logout_user

from app import db
from app.models import User


bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Some fields are missing!", "error")
            return redirect(url_for("auth.login"))

        user: User = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            # login_user(user, remember=True)
            login_user(user)
            flash("Logged in successfully!", "success")
            return redirect(url_for("main.index"))
        flash("Invalid credentials!", "error")
        return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if not username or not email or not password:
            flash("Some fields are missing!", "error")
            return redirect(url_for("auth.register"))

        if password != confirm_password:
            flash("Passwords do not match!", "error")
            return redirect(url_for("auth.register"))

        user = User.query.filter_by(username=username, email=email).first()
        if user:
            flash("User with that username or email already exists!", "error")
            return redirect(url_for("auth.register"))
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("auth.login"))
    else:
        return render_template("auth/register.html")


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out!", "info")
    return redirect(url_for("main.index"))
