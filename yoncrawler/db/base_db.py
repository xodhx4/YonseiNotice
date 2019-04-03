from abc import ABC, abstractmethod
from yoncrawler.util.logger import getMyLogger
import os

class BaseDB(ABC):

    def __init__(self):
        self.logger = getMyLogger()
        self.database = None

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
        


def checkDir(dir_path):
    if os.path.isdir(dir_path):
        path = dir_path
    else:
        mylogger = getMyLogger()
        mylogger.warn(f"{dir_path} Not exist, so automatically create it")
        os.makedirs(dir_path)
        path = dir_path
    if (path[-1] == '/') or (path[-1] == '\\'):
        path = path[:-1]

    return path