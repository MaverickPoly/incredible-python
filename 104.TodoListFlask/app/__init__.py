from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.config import Config


# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # Initialize extensions with auth
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Configure login
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to access this page"

    # Register blueprints
    from app.blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.blueprints.todo import bp as todos_bp
    app.register_blueprint(todos_bp, url_prefix="/todos")

    # Register error handlers
    register_error_handlers(app)

    # Register CLI commands
    register_commands(app)

    return app


def register_error_handlers(app):
    pass


def register_commands(app):
    import click

    @app.cli.command("init-db")
    def init_db():
        """Initialize the database"""
        db.create_all()
        click.echo("Database initialized.")
