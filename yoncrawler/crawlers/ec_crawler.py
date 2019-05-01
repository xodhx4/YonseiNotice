from yoncrawler.crawlers.base_cralwer import BaseCrawler
from yoncrawler.util import logger, request_module, parse_module
import datetime
import requests
from bs4 import BeautifulSoup


mylogger = logger.getMyLogger()
SUBJECT = "Economics"

class EcCrawler(BaseCrawler):

    def __init__(self):
        super().__init__()
        self.subject = SUBJECT
        self.name = "Economics Crawler"
        self.html = None
        self.base_url = None
        self.filter_key = 'href'
        self._datetime = datetime.datetime.now()
        self.request_method = request_module.basic_request
        self.sub_crawler = EcMainCrawler

    def request(self):
        self.html = self.request_method(self.url)
        # mylogger.debug(self.html)

    def parse(self):
        try:
            soup = BeautifulSoup(self.html, 'html.parser')
        except Exception as e:
            mylogger.warning(e)
        
        board = soup.find('table', {'class' : 'board-table'})

        def fix(table):
            for tag in table.find_all('tr', {'class' : 'c-board-top-wrap'}):
                tag.extract()
            return table

        data = parse_module.table_parser(board, fix)

        for x in data:
            x['href'] = self.base_url + x['href']
        
            
        self._set_data(data)
        # mylogger.debug(data)

    def set_page(self, page):
        self.page = page
        self.url = self.base_url
        if isinstance(self.page, int):
            self.url = self.base_url + "?article.offset=" + str((self.page-1)*10)
        

    def __str__(self):
        return f"<{self.name}> | Datetime : {self._datetime} | Address : {self.url}"

class EcMainCrawler(BaseCrawler):

    def __init__(self):
        super().__init__()
        self.subject = SUBJECT
        self.name = "Ec Main Crawler"
        self.html = None
        self.request_method = request_module.basic_request
    
    def request(self):
        self.html = self.request_method(self.url)
        # mylogger.info(self.html)

    def parse(self):
        try:
            soup = BeautifulSoup(self.html, 'html.parser')
        except Exception as e:
            mylogger.warning(e)

        board = soup.find("div", {"class" : "board-write-wrap"})
        value_list = board.find_all('dd')
        data = {}
        data['title'] =  value_list[0].text
        data['date'] = value_list[1].text
        data['writer'] = value_list[2].text
        data['content'] = str(value_list[3])
        data['attachment'] = ''
        if len(value_list) == 5:
            data['attachment'] = str(value_list[4])
        data['href'] = self.url

        self._set_data(data)
        mylogger.debug(data)

    def __str__(self):
        return f"<{self.name}> | Address : {self.url}"

class EcNoticeCrawler(EcCrawler):

    def __init__(self, page=None):
        super().__init__()
        self.name = "Ec Faculty Notice Crawler"
        self.base_url = "https://economics.yonsei.ac.kr/economics/community/under_notice.do"
        self.set_page(page)
        # from yoncrawler.test.test_crawler import EmptyCrawler
        # self.sub_crawler = EmptyCrawler

class EcGraduateNoticeCrawler(EcCrawler):

    def __init__(self, page=None):
        super().__init__()
        self.name = "Ec Graduate School Notice Crawler"
        self.base_url = "https://economics.yonsei.ac.kr/economics/community/grad_notice.do"
        self.set_page(page)
        # from yoncrawler.test.test_crawler import EmptyCrawler
        # self.sub_crawler = EmptyCrawler

class EcSeminarCrawler(EcCrawler):

    def __init__(self, page=None):
        super().__init__()
        self.name = "Ec Seminar & conference Crawler"
        self.base_url = "https://economics.yonsei.ac.kr/economics/community/seminar.do"
        self.set_page(page)
        # from yoncrawler.test.test_crawler import EmptyCrawler
        # self.sub_crawler = EmptyCrawler

class EcCareerCrawler(EcCrawler):

    def __init__(self, page=None):
        super().__init__()
        self.name = "Ec Career Crawler"
        self.base_url = "https://economics.yonsei.ac.kr/economics/community/job.do" 
        self.set_page(page)
        # from yoncrawler.test.test_crawler import EmptyCrawler
        # self.sub_crawler = EmptyCrawler

if __name__=="__main__":
    crawlers = [
        EcNoticeCrawler,
        EcGraduateNoticeCrawler,
        EcSeminarCrawler,
        EcCareerCrawler,
    ]

    for n in crawlers:
        n().start()
        print(n.data)