from base_cralwer import BaseCrawler, basic_crawl
import datetime
import requests
from bs4 import BeautifulSoup
from logger import getMyLogger

mylogger = getMyLogger()

class ExternalCrawler(BaseCrawler):
    # https://www.yonsei.ac.kr/sc/support/etc_notice.jsp

    def __init__(self):
        super().__init__()
        self.html = None
        self._datetime = datetime.datetime.now()
        self.url = "https://www.yonsei.ac.kr/sc/support/etc_notice.jsp"
        self.sub_crawler = None
        self.crawl_method = basic_crawl

    def crawl(self):
        self.html = self.crawl_method(self.url)
        mylogger.debug(self.html)


    def parse(self):
        # TODO
        try:
            soup = BeautifulSoup(self.html, 'html.parser')
        except Exception as e:
            mylogger.warn(e)


    def save(self):
        # TODO
        if self.db is None:
            mylogger.info(self.data)

    def __str__(self):
        return f"<External Crawler> | Datetime : {self._datetime} | Address : {self.url}"

    
if __name__ == "__main__":
    n = ExternalCrawler()
    n.start()