# Third-Party Library
import pymongo as pymongo
from decouple import config

# IRango
from src.core.interfaces.infrastructures.mongodb.interface import IMongoDBInfrastructure


class MongoDBInfrastructure(IMongoDBInfrastructure):
    mongodb_client = None
    mongodb_url_connection: str = config("MONGODB_URL_CONNECTION")

    @classmethod
    def get_client(cls):
        try:
            if cls.mongodb_client is None:
                cls.mongodb_client = pymongo.MongoClient(cls.mongodb_url_connection)
            return cls.mongodb_client

        except Exception as error:
            print(f"error: {error}")
            raise error
