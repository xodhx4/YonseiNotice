from yoncrawler.db.base_db import BaseDB, NotSupportedError, checkDir
from yoncrawler.util.logger import getMyLogger
from tinydb import TinyDB, where
import os

mylogger = getMyLogger()

class TinyDBSaver(BaseDB):
    def __init__(self, table_name, db_name=None, dir_path=os.getcwd()):
        super().__init__()
        self.dir = checkDir(dir_path)
        self.filename = table_name.replace(" ", "_") + ".json"
        try:
            self.connect()
        except Exception as e:
            mylogger.warn(e)
            return None

    def connect(self):
        path = os.path.join(self.dir, self.filename)

        self.database = TinyDB(path)

    def create(self, data):
        if isinstance(data, list):
            for x in data:
                self.database.insert(x)
        else:
            self.database.insert(data)

    def read(self, field, value):
        result = self.database.search(where(field)==value)
        if len(result) == 0:
            return None
        return result

    def update(self):
        raise NotSupportedError("JsonSaver", "update")

    def delete(self):
        raise NotSupportedError("JsonSaver", "delete")
