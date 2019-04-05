from yoncrawler.db.base_db import BaseDB, NotSupportedError, checkDir
from yoncrawler.util.logger import getMyLogger
from pymongo import MongoClient

mylogger = getMyLogger()

class MongoDBSaver(BaseDB):
    def __init__(self, db_name, table_name):
        super().__init__()
        self.db_name = db_name.replace(" ", "_")
        self.table_name = table_name.replace(" ", "_")

        try:
            self.database = self.connect()
        except Exception as e:
            mylogger.warn(e)
            return None

    def connect(self):
        client = MongoClient("mongodb://mongo:27017/")
        db = client[self.db_name]
        collection = db[self.table_name]
        return collection

    def create(self, data):
        if isinstance(data, list):
            result = self.database.insert_many(data)
        elif isinstance(data, dict):
            result = self.database.insert_one(data)
        else:
            mylogger.warn("Data type is Not correct")
        mylogger.debug(result)

    def read(self, field, value):
        result = self.database.find_one({field : value})
        return result

    def update(self):
        raise NotSupportedError("MongoSaver", "update")

    def delete(self):
        raise NotSupportedError("MongoSaver", "delete")