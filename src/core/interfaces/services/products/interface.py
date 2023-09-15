# Standard Library
from abc import ABCMeta, abstractmethod

# IRango
from src.repositories.products.repository import ProductsRepository
from src.repositories.restaurants.repository import RestaurantsRepository


class IProductsService(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    async def create_product(
        cls,
        payload: dict,
        restaurant_repository=RestaurantsRepository,
        product_repository=ProductsRepository,
    ):
        pass

    @classmethod
    @abstractmethod
    async def find_one_product(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        pass

    @classmethod
    @abstractmethod
    async def find_all_product(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        pass

    @classmethod
    @abstractmethod
    async def update_product(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        pass

    @classmethod
    @abstractmethod
    async def delete_product(
        cls, payload: dict, products_repository=ProductsRepository
    ):
        pass
