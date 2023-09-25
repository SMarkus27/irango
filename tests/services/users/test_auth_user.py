from unittest.mock import patch, MagicMock

import flask_jwt_extended
from flask import Flask
from flask_jwt_extended import create_access_token, JWTManager

from src.repositories.users.repository import UsersRepository
from src.services.users.service import UsersService


@patch.object(UsersRepository, "find_one")
def test_auth_user_user_not_found(find_one_patch: MagicMock):
    user_data = {
        "email": "email@test.com"
    }

    expected = {
                "message": f"Users not found",
                "status_code": 204,
            }

    find_one_patch.return_value = None

    result = UsersService.auth_user(user_data)

    assert result == expected


@patch.object(UsersRepository, "find_one")
def test_auth_user_user_invalid_password(find_one_patch: MagicMock):
    user_data = {
        "email": "email@test.com",
        "password": "1234"
    }

    expected = {
        "message": "Invalid password or email",
        "status_code": 400
            }

    user_info_mongodb = {
        "email": "email@test.com",
        "password": "$pbkdf2-sha256$29000$wphzTmnNWWvtndOak/JeSw$3xfD6qxx3W0a2k.4ScuiR1t57u65sdt0ARGjC51j2W0"
    }
    find_one_patch.return_value = user_info_mongodb

    result = UsersService.auth_user(user_data)

    assert result == expected


@patch.object(UsersRepository, "find_one")
def test_auth_user_user_invalid_password(find_one_patch: MagicMock):
    user_data = {
        "email": "email@test.co",
        "password": "string"
    }

    expected = {
        "message": "Invalid password or email",
        "status_code": 400
            }

    user_info_mongodb = {
        "email": "email@test.com",
        "password": "$pbkdf2-sha256$29000$wphzTmnNWWvtndOak/JeSw$3xfD6qxx3W0a2k.4ScuiR1t57u65sdt0ARGjC51j2W0"
    }
    find_one_patch.return_value = user_info_mongodb

    result = UsersService.auth_user(user_data)

    assert result == expected


@patch.object(UsersRepository, "find_one")
def test_auth_user(find_one_patch: MagicMock):
    user_data = {
        "email": "email@test.com",
        "password": "string"
    }

    user_info_mongodb = {
        "email": "email@test.com",
        "password": "$pbkdf2-sha256$29000$wphzTmnNWWvtndOak/JeSw$3xfD6qxx3W0a2k.4ScuiR1t57u65sdt0ARGjC51j2W0"
    }

    find_one_patch.return_value = user_info_mongodb

    app = Flask(__name__)
    with app.app_context():
        app.config["JWT_SECRET_KEY"] = "xaps"

        jwt = JWTManager(app)

        result = UsersService.auth_user(user_data)

        assert result.get("status_code") == 200
