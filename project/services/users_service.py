from flask_restx import abort

from project.dao.user import UserDAO
from project.exceptions import ItemNotFound
from project.schemas.user import UserSchema
from project.services.base import BaseService
from project.tools.security import generate_password_digest


class UsersService(BaseService):
    def get_item_by_id(self, pk):
        user = UserDAO(self._db_session).get_by_id(pk)
        if not user:
            raise ItemNotFound
        return UserSchema().dump(user)

    def get_all_users(self):
        users = UserDAO(self._db_session).get_all()
        return UserSchema(many=True).dump(users)

    def get_item_by_email(self, email):
        user = UserDAO(self._db_session).get_by_email(email)
        if not user:
            raise ItemNotFound
        return user

    def create(self, data_in):
        user = UserDAO(self._db_session).get_by_email(data_in.get("email"))
        if user:
            abort(400, "Email already taken")
        user_pass = data_in.get("password")
        if user_pass:
            data_in["password"] = generate_password_digest(user_pass)
        UserDAO(self._db_session).create(data_in)
        return "User successfully created", 200

    def update(self, data_in):
        user = UserDAO(self._db_session).update(data_in)
        return UserSchema().dump(user)


