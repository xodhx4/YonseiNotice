from yoncrawler.db.base_db import BaseDB, NotSupportedError, checkDir
from yoncrawler.util.logger import getMyLogger
from tinydb import TinyDB, Query
import os

mylogger = getMyLogger()

class TinyDBSaver(BaseDB):
    def __init__(self, dir_path=os.path.dirname(__file__)):
        super().__init__()
        self.dir = checkDir(dir_path)
        self.filename = None

    def create(self, data, name):
        # TODO
        self.filename = name.replace(" ", "_") + ".json"
        path = os.path.join(self.dir, self.filename)

        self.database = TinyDB(path)
        if isinstance(data, list):
            for x in data:
                self.database.insert(x)
        else:
            self.database.insert(data)

        return path

    def read(self):
        raise NotSupportedError("JsonSaver", "read")

    def update(self):
        raise NotSupportedError("JsonSaver", "update")

    def delete(self):
        raise NotSupportedError("JsonSaver", "delete")
