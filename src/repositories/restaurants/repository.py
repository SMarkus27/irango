# Third-Party Library
from decouple import config
from motor.motor_asyncio import AsyncIOMotorCollection

# IRango
from src.repositories.bases.mongodb.repository import BaseMongoDBRepository


class RestaurantsRepository(BaseMongoDBRepository):
    _mongodb_database = config("MONGODB_RESTAURANTS_DATABASE")
    _mongodb_collection = config("MONGODB_RESTAURANTS_DATABASE")
