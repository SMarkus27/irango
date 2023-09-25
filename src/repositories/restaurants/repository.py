# Third-Party Library
from decouple import config

# IRango
from src.repositories.bases.mongodb.repository import BaseMongoDBRepository


class RestaurantsRepository(BaseMongoDBRepository):
    _mongodb_database = config("MONGODB_RESTAURANTS_DATABASE")
    _mongodb_collection = config("MONGODB_RESTAURANTS_COLLECTION")
