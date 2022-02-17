from flask import request
from flask_restx import Namespace, abort, Resource

from project.exceptions import ItemNotFound
from project.services import users_service
from project.services.users_service import UsersService
from project.setup_db import db
from project.tools.security import auth_required, compare_passwords

users_ns = Namespace("users")


@users_ns.route("/")
class UsersView(Resource):
    @auth_required
    @users_ns.response(200, "OK")
    def get(self):
        """Get all users"""
        return UsersService(db.session).get_all_users()


@users_ns.route("/<int:user_id>")
class UserView(Resource):
    @auth_required
    @users_ns.response(200, "OK")
    @users_ns.response(404, "Genre not found")
    def get(self, user_id: int):
        try:
            return UsersService(db.session).get_item_by_id(user_id)
        except:
            abort(404)

    def patch(self, user_id: int):
        req_json = request.json
        if not req_json:
            abort(400)
        if not req_json.get("id"):
            req_json["id"] = user_id
        try:
            return UsersService(db.session).update(req_json)
        except:
            abort(404)


@users_ns.route("/password/<int:user_id>")
class UserPatchView(Resource):
    @auth_required
    @users_ns.response(200, "OK")
    @users_ns.response(404, "Genre not found")
    def put(self, user_id: int):
        req_json = request.json
        password_1 = req_json.get("password_1")
        password_2 = req_json.get("password_2")
        if not password_1 or not password_2:
            abort(400)
        user = UsersService(db.session).get_item_by_id(user_id)
        if not user or not compare_passwords(user.password, password_1):
            abort(401)
        UsersService(db.session).update({'password': password_2})
        return "", 204

