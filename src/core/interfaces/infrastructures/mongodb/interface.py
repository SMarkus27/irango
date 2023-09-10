# Standard Library
from abc import ABCMeta, abstractmethod


class IMongoDBInfrastructure(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def get_client(cls):
        pass
