import os
from flask import Flask
from flask_cors import CORS
from app.config.db import db
from app.routes.task_routes import task_bp


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://todo_user:todo_pass@localhost:5432/todo_db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app, origins=[
        "http://localhost:5173",
        "http://localhost:3000"
    ])

    db.init_app(app)

    @app.route("/")
    def home():
        return {"message": "Todo API is running"}

    app.register_blueprint(task_bp)

    return app
