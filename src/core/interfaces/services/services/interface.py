# Standard Library
from abc import ABCMeta, abstractmethod

# IRango
from src.repositories.restaurants.repository import RestaurantsRepository


class IRestaurantsService(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    async def create_restaurant(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        pass

    @classmethod
    @abstractmethod
    async def find_one_restaurant(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        pass

    @classmethod
    @abstractmethod
    async def find_all_restaurant(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        pass

    @classmethod
    @abstractmethod
    async def update_restaurant(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        pass

    @classmethod
    async def delete_restaurant(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        pass
