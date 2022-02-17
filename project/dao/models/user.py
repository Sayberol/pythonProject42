from project.dao.models.base import BaseMixin
from project.setup_db import db


class User(BaseMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    favorite_genre = db.Column(db.String(255))

    def __repr__(self):
        return f"<User '{self.name.title()}'>"
