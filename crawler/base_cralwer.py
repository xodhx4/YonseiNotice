import requests
from logger import getMyLogger
from abc import *

class BaseCrawler(ABC):

    def __init__(self):
        self._url = None
        self._db = None
        self._data = None
        self._sublist = None
        self._sub_crawler = None

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
        self._db = db
    
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
        self._data = data
        
    def call_sub_crawler(self):
        if self._sub_crawler is None:
            if self._sublist is not None:
                raise NotImplementedError
        else:
            # TODO Change to multithread friendly with thread pool
            for sub_url in self._sublist:
                sub_crawler = self._sub_crawler()
                sub_crawler.url = sub_url
                sub_crawler.start()

    def start(self):
        # TODO
        self.crawl()
        self.parse()
        self.save()
        self.call_sub_crawler()
    
    @abstractmethod
    def crawl(self):
        raise NotImplementedError
    
    @abstractmethod
    def parse(self):
        raise NotImplementedError

    @abstractmethod
    def save(self):
        raise NotImplementedError


def basic_crawl(url):
    mylogger = getMyLogger()
    mylogger.info(
        f"Crawl {url}"
    )

    try:
        response = requests.get(url)
        mylogger.info(response)
    except Exception as e:
        mylogger.error(
            f"{url} crawl exception\n" + e.__str__()
        )
    
    return response.text
    # mylogger.debug(self.html)