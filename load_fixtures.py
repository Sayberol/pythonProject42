from sqlalchemy.exc import IntegrityError

from project.config import DevelopmentConfig
from project.dao.models import Genre, Director, Movie
from project.server import create_app
from project.setup_db import db
from project.utils import read_json

app = create_app(DevelopmentConfig)

data = read_json("fixtures.json")

with app.app_context():
    for genre in data["genres"]:
        db.session.add(Genre(id=genre["pk"], name=genre["name"]))

    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")

with app.app_context():
    for director in data["directors"]:
        db.session.add(Director(id=director["pk"], name=director["name"]))

    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")

with app.app_context():
    for movie in data["movies"]:
        db.session.add(Movie(id=movie["pk"], title=movie["title"]))

    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")
