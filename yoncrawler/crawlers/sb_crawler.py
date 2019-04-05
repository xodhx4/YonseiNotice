from yoncrawler.crawlers.base_cralwer import BaseCrawler
from yoncrawler.util import logger, request_module, parse_module
import datetime
import requests
from bs4 import BeautifulSoup


mylogger = logger.getMyLogger()

class SbCrawler(BaseCrawler):

    def __init__(self):
        super().__init__()
        self.name = "School of Business Crawler"
        self.html = None
        self.filter_key = 'href'
        self._datetime = datetime.datetime.now()
        self.request_method = request_module.basic_request

    def request(self):
        self.html = self.request_method(self.url)
        # mylogger.debug(self.html)

    def parse(self):
        try:
            soup = BeautifulSoup(self.html, 'html.parser')
        except Exception as e:
            mylogger.warn(e)
        
        board = soup.find('table', {'id' : 'Board'})

        data = parse_module.table_parser(board)

        base_url = "https://ysb.yonsei.ac.kr/"
        for x in data:
            x['href'] = base_url + x['href']
        
            
        self._set_data(data)
        self.sublist = [x['href'] for x in self.data]


    def __str__(self):
        return f"<{self.name}> | Datetime : {self._datetime} | Address : {self.url}"

class SbMainCrawler(BaseCrawler):

    def __init__(self):
        super().__init__()
        self.name = "Sb Main Crawler"
        self.html = None
        self.request_method = request_module.basic_request
    
    def request(self):
        self.html = self.request_method(self.url)
        # mylogger.info(self.html)

    def parse(self):
        try:
            soup = BeautifulSoup(self.html, 'html.parser')
        except Exception as e:
            mylogger.warn(e)

        board = soup.find("div", {"class" : "BoardWrapper"})
        data = {}
        data['title'] =  board.find("div", {"id" : "BoardViewTitle"}).text
        date =  board.find("div", {"id" : "BoardViewAdd"})
        if date is not None:
            data['date'] = date.text[4:14]
        data['content'] = str(soup.find("div", {"id" : "BoardContent"}))
        data['href'] = self.url

        self._set_data(data)

    def __str__(self):
        return f"<{self.name}> | Address : {self.url}"

class SbNoticeCrawler(SbCrawler):

    def __init__(self):
        super().__init__()
        self.name = "Bs Notice Crawler"
        self.url = "https://ysb.yonsei.ac.kr/board.asp?mid=m06_01"
        self.sub_crawler = SbMainCrawler
        # from yoncrawler.test.test_crawler import EmptyCrawler
        # self.sub_crawler = EmptyCrawler

class SbCareerCrawler(SbCrawler):

    def __init__(self):
        super().__init__()
        self.name = "Bs Career Crawler"
        self.url = "https://ysb.yonsei.ac.kr/career.asp?mid=m08_03"
        self.sub_crawler = SbMainCrawler
        # from yoncrawler.test.test_crawler import EmptyCrawler
        # self.sub_crawler = EmptyCrawler

if __name__=="__main__":
    crawlers = [
        SbNoticeCrawler,
        SbCareerCrawler,
    ]

    for n in crawlers:
        n().start()