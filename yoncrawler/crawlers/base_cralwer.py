from yoncrawler.util.logger import getMyLogger
from abc import ABC, abstractmethod
import copy

class BaseCrawler(ABC):

    def __init__(self):
        self._url = None
        self._db = None
        self._data = None
        self._sublist = None
        self._sub_crawler = None
        self.filter_key = None
        self.subject = None
        self.name = None
        self.logger = getMyLogger()

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def db(self):
        return self._db
    
    @db.setter
    def db(self, db):
        db_instance = db(db_name=self.subject,
            table_name=self.name)
        self._db = db_instance
    
    @property
    def sub_crawler(self):
        return self._sub_crawler

    @sub_crawler.setter
    def sub_crawler(self, crw):
        self._sub_crawler = crw
    
    @property
    def sublist(self):
        return self._sublist

    @sublist.setter
    def sublist(self, subs):
        self._sublist = subs

    @property
    def data(self):
        return self._data
    
    def _set_data(self, data):
        data = self.reduce_duplicate(data)
        self._data = data
        if isinstance(data, list):
            self.sublist = [x['href'] for x in data]
        
    def call_sub_crawler(self):
        # TODO : Add multi sub_crawler for next page
        if self._sub_crawler is None:
            if self._sublist is not None:
                raise NotImplementedError
        elif self.db is not None:
            # TODO Change to multithread friendly with thread pool
            for sub_url in self._sublist:
                sub_crawler = self._sub_crawler()
                sub_crawler.url = sub_url
                sub_crawler.name = self.name + "__" + sub_crawler.name
                sub_crawler._db = self.db
                sub_crawler.db.table_name = sub_crawler.name
                sub_crawler.db.connect()
                sub_crawler.start()

    def start(self):
        self.logger.info(f"{self}\n Crawl Start")
        self.request()
        self.parse()
        self.save()
        self.call_sub_crawler()
        self.logger.info(f"{self}\n Crawl End")
    
    @abstractmethod
    def request(self):
        raise NotImplementedError
    
    @abstractmethod
    def parse(self):
        raise NotImplementedError

    def save(self):
        if self.db is None:
            self.logger.info(f"{self.subject} | {self.name} | {self.url} | {self.db} | Insert Suceess")
            return self.data
        self.db.create(self.data)
        self.logger.info(f"{self.subject} | {self.name} | {self.url} | {self.db} | Insert Suceess")
    
    def reduce_duplicate(self, data):
        if self.db is not None and self.filter_key is not None:
            data = list(filter(lambda x: self.db.read(self.filter_key, x[self.filter_key]) is None, data))
            if len(data) == 0:
                data = None
        return data

