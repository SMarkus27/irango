# Standard Library
from abc import ABCMeta, abstractmethod


class IRedisInfrastructure(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def get_client(cls):
        pass
