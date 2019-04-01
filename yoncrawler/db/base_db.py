from abc import ABC, abstractmethod
from yoncrawler.util.logger import getMyLogger

class BaseDB(ABC):

    def __init__(self):
        self.logger = getMyLogger()

    @abstractmethod
    def create(self):
        raise NotImplementedError

    @abstractmethod
    def read(self):
        raise NotImplementedError

    @abstractmethod
    def update(self):
        raise NotImplementedError

    @abstractmethod
    def delete(self):
        raise NotImplementedError

class NotSupportedError(Exception):
    def __init__(self, who, what):
        msg = f"{who} is not support method {what}."
        super().__init__(msg)
        