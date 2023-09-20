from flask import request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from flask_smorest import Blueprint

from src.domain.schemas.users.schema import UsersSchema
from src.services.users.service import UsersService

users = Blueprint("users", "users", description="users")


@users.post("/register")
@users.arguments(UsersSchema)
def create_user(user_data: dict):
    return UsersService.create_user(user_data)


@users.post("/login")
@users.arguments(UsersSchema)
def login(user_data: dict):
    return UsersService.auth_user(user_data)


@users.post("/logout")
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    return UsersService.logout(jti)
