# Standard Library
from typing import List, Union

# Third-Party Libraries
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorCursor
from pymongo.results import UpdateResult, DeleteResult

# IRango
from src.core.interfaces.repositories.mongodb.base.interface import (
    IBaseMongoDBRepository,
)
from src.infrastructures.mongodb.infrastructure import MongoDBInfrastructure


class BaseMongoDBRepository(MongoDBInfrastructure, IBaseMongoDBRepository):
    _mongodb_database = None
    _mongodb_collection = None
    _mongodb_collection_in_connection: AsyncIOMotorCollection = None

    @classmethod
    async def _set_mongodb_base_collection(cls) -> AsyncIOMotorCollection:
        if not (cls._mongodb_database and cls._mongodb_collection):
            raise Exception("Hey you forgot something. Try again")

        client = cls.get_client()
        database = client[cls._mongodb_database]
        collections = database[cls._mongodb_collection]
        return collections

    @classmethod
    async def _get_mongodb_base_collection(cls) -> AsyncIOMotorCollection:
        if cls._mongodb_collection_in_connection is None:
            cls._mongodb_collection_in_connection = (
                await cls._set_mongodb_base_collection()
            )
        return cls._mongodb_collection_in_connection

    @classmethod
    async def insert_one(cls, data) -> None:
        mongodb_collection: AsyncIOMotorCollection = (
            await cls._get_mongodb_base_collection()
        )
        await mongodb_collection.insert_one(data)

    @classmethod
    async def find_one(cls, query: dict, projection: dict) -> dict:
        mongodb_collection: AsyncIOMotorCollection = (
            await cls._get_mongodb_base_collection()
        )
        result = await mongodb_collection.find_one(query, projection)
        return result

    @classmethod
    async def find_all_paginated(
        cls, query: dict, projection: dict, skip: int, limit: int, sort: tuple = None
    ) -> Union[List, 0]:
        mongodb_collection: AsyncIOMotorCollection = (
            await cls._get_mongodb_base_collection()
        )
        total_items = await mongodb_collection.count_documents(query)

        if not total_items:
            return [], 0

        result: AsyncIOMotorCursor = mongodb_collection.find(query, projection)

        if sort:
            result.sort(*sort)

        result.skip(skip).limit(limit)

        return await result.to_list(limit), total_items

    @classmethod
    async def update_one(
        cls,
        query: dict,
        update_data: dict,
        array_filters: list = None,
        upsert: bool = False,
    ) -> UpdateResult:
        mongodb_collection: AsyncIOMotorCollection = (
            await cls._get_mongodb_base_collection()
        )
        result = await mongodb_collection.update_one(
            query, {"$set": update_data}, array_filters=array_filters, upsert=upsert
        )
        return result

    @classmethod
    async def delete_one(cls, query: dict) -> DeleteResult:
        mongodb_collection: AsyncIOMotorCollection = (
            await cls._get_mongodb_base_collection()
        )
        return await mongodb_collection.delete_one(query)
