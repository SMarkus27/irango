# Third-Party Library
from decouple import config

# IRango
from src.repositories.bases.mongodb.repository import BaseMongoDBRepository


class ProductsRepository(BaseMongoDBRepository):
    _mongodb_database = config("MONGODB_PRODUCTS_DATABASE")
    _mongodb_collection = config("MONGODB_PRODUCTS_COLLECTION")

    @classmethod
    def add_one_in_array(cls, query: dict, product_data: dict):
        mongodb_collection = (
            cls._get_mongodb_base_collection()
        )
        print(product_data)
        result = mongodb_collection.update_one(query, {"$push": product_data},  array_filters=None, upsert=True)
        return result

    @classmethod
    def delete_one_in_array(
        cls, query, product_data, array_filters=None, upsert=False
    ):
        mongodb_collection = (
            cls._get_mongodb_base_collection()
        )
        return mongodb_collection.update_one(
            query, {"$pull": product_data}, array_filters=array_filters, upsert=upsert
        )
