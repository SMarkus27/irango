# Standard Library
from abc import ABCMeta, abstractmethod

# Third-Party Library
from pymongo.results import DeleteResult, UpdateResult


class IBaseMongoDBRepository(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def insert_one(cls, data) -> None:
        pass

    @classmethod
    @abstractmethod
    def find_one(cls, query: dict, projection: dict) -> dict:
        pass

    @classmethod
    @abstractmethod
    def update_one(
        cls,
        query: dict,
        update_data: dict,
        array_filters: list = None,
        upsert: bool = False,
    ) -> UpdateResult:
        pass

    @classmethod
    @abstractmethod
    def delete_one(cls, query: dict) -> DeleteResult:
        pass
