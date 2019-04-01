from yoncrawler.db.base_db import BaseDB, NotSupportedError
from yoncrawler.util.logger import getMyLogger
import os
import json

mylogger = getMyLogger()

class JsonSaver(BaseDB):
    def __init__(self, dir_path=os.path.dirname(__file__)):
        super().__init__()
        self.dir = checkDir(dir_path)
        self.filename = None

    def create(self, data, name):
        # TODO
        self.filename = name.replace(" ", "_") + ".json"
        path = os.path.join(self.dir, self.filename)

        with open(path, 'a') as json_file:
            json.dump(data, json_file)

        return path

    def read(self):
        raise NotSupportedError("JsonSaver", "read")

    def update(self):
        raise NotSupportedError("JsonSaver", "update")

    def delete(self):
        raise NotSupportedError("JsonSaver", "delete")


def checkDir(dir_path):
    if os.path.isdir(dir_path):
        path = dir_path
    else:
        mylogger.warn(f"{dir_path} Not exist, so automatically create it")
        os.makedirs(dir_path)
        path = dir_path
    if (path[-1] == '/') or (path[-1] == '\\'):
        path = path[:-1]

    return path
