from sqlalchemy.orm import scoped_session

from project.dao.models.user import User


class UserDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_id(self, pk):
        return self._db_session.query(User).filter(User.id == pk).one_or_none()

    def get_all(self):
        return self._db_session.query(User).all()

    def get_by_email(self, email):
        return self._db_session.query(User).filter(User.email == email).one_or_none()

    def create(self, data_in):
        user = User(**data_in)
        self._db_session.add(user)
        self._db_session.commit()
        return user

    def update(self, data_in):
        user = self.get_by_id(data_in.get("id"))
        if user:
            if data_in.get("password"):
                user.password = data_in.get("password")
            if data_in.get("role"):
                user.role = data_in.get("role")
            if data_in.get("name"):
                user.name = data_in.get("name")
            if data_in.get("surname"):
                user.surname = data_in.get("surname")
