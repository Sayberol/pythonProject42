from flask import request
from flask_restx import Namespace, Resource, abort


from project.services import UsersService
from project.setup_db import db
from project.tools.security import login_user, refresh_user_token

auth_ns = Namespace("auth")


@auth_ns.route("/login")
class AuthView(Resource):
    def post(self):
        req_json = request.json
        if not req_json:
            abort(400)
        try:
            user = UsersService(db.session).get_item_by_email(email=req_json.get("email"))
            tokens = login_user(request.json, user)
            return tokens, 200
        except:
            abort(401)

    def put(self):
        req_json = request.json
        if not req_json:
            abort(400)
        try:
            tokens = refresh_user_token(req_json)
            return tokens, 200
        except:
            abort(401)


@auth_ns.route('/register')
class AuthRegisterView(Resource):
    def post(self):
        req_json = request.json
        if not req_json:
            abort(400)
        return UsersService(db.session).create(req_json)
