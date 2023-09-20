from uuid import uuid4

from flask_jwt_extended import create_access_token

from src.core.interfaces.services.users.interface import IUsersService
from src.repositories.cache.repository import CacheRepository
from src.repositories.users.repository import UsersRepository
from passlib.hash import pbkdf2_sha256


class UsersService(IUsersService):

    block_list = set()

    @classmethod
    def create_user(
        cls, user_data: dict, user_repository=UsersRepository
    ):
        email = user_data.get("email")
        query = {"email": email}
        projection = {"_id": False}

        user_info = user_repository.find_one(query, projection)

        if user_info:
            return {
                "message": f"Users with email: {email} already exist, try it a new one",
                "status_code": 200,
            }

        user_id = uuid4().__str__()
        password = user_data.get("password")
        hash_password = pbkdf2_sha256.hash(password)
        user_data.update({"user_id": user_id, "password": hash_password})

        user_repository.insert_one(user_data)

        return {"message": "User Created", "status_code": 201}

    @classmethod
    def auth_user(
        cls, user_data: dict, user_repository=UsersRepository
    ):
        email = user_data.get("email")
        query = {"email": email}
        projection = {"_id": False}

        user_info = user_repository.find_one(query, projection)

        if not user_info:
            return {
                "message": f"Users not found",
                "status_code": 204,
            }

        password = user_data.get("password")
        hash_password = user_info.get("password")

        is_valid_password = pbkdf2_sha256.verify(password, hash_password)
        is_valid_email = email == user_info.get("email")

        if is_valid_password and is_valid_email:
            identity = {
                "username": user_info.get("username"),
                "email": user_info.get("email"),
                "user_id": user_info.get("user_id")
            }
            access_token = create_access_token(identity)

            return {
                "access_token": access_token,
                "status_code": 200

            }
        return {
            "message": "Invalid password or email",
            "status_code": 400
        }

    @classmethod
    def logout(cls, jti: str, cache_repository=CacheRepository):
        cache_repository.set(jti, True)

        return {
            "message": "Logout Successfully",
            "status_code": 200
        }

    @classmethod
    def blocklist(cls, jti: str, cache_repository=CacheRepository):
        has_cached = cache_repository.get(jti)
        return has_cached
