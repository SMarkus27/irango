from unittest.mock import patch, MagicMock

from src.repositories.users.repository import UsersRepository
from src.services.users.service import UsersService


@patch.object(UsersRepository, "find_one")
def test_create_user_user_already_exist(find_one_patch: MagicMock):
    user_data = {
        "email": "email@test.com"
    }

    expected = {
                "message": f"Users with email: email@test.com already exist, try it a new one",
                "status_code": 200,
            }

    find_one_patch.return_value = True

    result = UsersService.create_user(user_data)

    assert result == expected


@patch.object(UsersRepository, "insert_one")
@patch.object(UsersRepository, "find_one")
def test_create_user_user(find_one_patch: MagicMock, insert_one_patch: MagicMock):
    password_before_hash = "1234"

    user_data = {
        "email": "email@test.com",
        "password": password_before_hash
    }

    expected = {"message": "User Created", "status_code": 201}

    find_one_patch.return_value = False

    result = UsersService.create_user(user_data)

    assert result == expected
    assert user_data.get("password") != password_before_hash
