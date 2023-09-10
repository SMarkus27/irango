# Third-Party Library
from decouple import config


class ProductsMongoDBRepository:
    _mongodb_database = config("MONGODB_PRODUCTS_DATABASE")
    _mongodb_collection = config("MONGODB_PRODUCTS_COLLECTION")
