# Standard Library
from abc import ABCMeta, abstractmethod

# IRango
from src.repositories.restaurants.repository import RestaurantsRepository


class IRestaurantsService(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def create_restaurant(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        pass

    @classmethod
    @abstractmethod
    def find_one_restaurant(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        pass

    @classmethod
    @abstractmethod
    def find_all_restaurant(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        pass

    @classmethod
    @abstractmethod
    def update_restaurant(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        pass

    @classmethod
    def delete_restaurant(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        pass
