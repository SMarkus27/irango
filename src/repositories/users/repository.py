# Third-Party Library
from decouple import config

# IRango
from src.repositories.bases.mongodb.repository import BaseMongoDBRepository


class UsersRepository(BaseMongoDBRepository):
    _mongodb_database = config("MONGODB_USERS_DATABASE")
    _mongodb_collection = config("MONGODB_USERS_COLLECTION")
