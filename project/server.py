from flask import Flask, render_template
from flask_cors import CORS
from flask_restx import Api

from project.config import DevelopmentConfig, TestingConfig
from project.setup_db import db
from project.views import genres_ns, directors_ns, movies_ns, users_ns
from project.views.auth import auth_ns

api = Api(
    authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    title="Flask Course Project 3",
    doc="/docs",
)
# Нужно для работы с фронтендом
cors = CORS()


def create_app(DevelopmentConfig):
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object(DevelopmentConfig)

    @app.route('/')
    def index():
        return render_template('index.html')

    cors.init_app(app)
    db.init_app(app)
    api.init_app(app)

    # Регистрация эндпоинтов
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(users_ns)
    api.add_namespace(auth_ns)

    return app
