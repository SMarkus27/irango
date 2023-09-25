# Standard Library
from abc import ABCMeta, abstractmethod

# IRango
from src.repositories.users.repository import UsersRepository


class IUsersService(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def create_user(
        cls, user_data: dict, user_repository=UsersRepository
    ):
        pass

    @classmethod
    @abstractmethod
    def auth_user(
        cls, user_data: dict, user_repository=UsersRepository
    ):
        pass
