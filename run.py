from project.config import DevelopmentConfig, TestingConfig
from project.dao.models import Genre
from project.server import create_app, db

app = create_app()


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
    }
