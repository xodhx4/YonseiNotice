
from yoncrawler.crawlers.base_cralwer import BaseCrawler
from yoncrawler.util import logger, request_module, parse_module
import datetime
import requests
from bs4 import BeautifulSoup


mylogger = logger.getMyLogger()

class CsCrawler(BaseCrawler):

    def __init__(self):
        # TODO : web page change
        super().__init__()
        self.html = None
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
        
        board = soup.find('table', {'class' : 'board04'})

        # Change 2nd 번호 to 날짜
        def fix(table):
            name = table.find('tr').find_all('th')[2]
            name.string = "날짜"
            return table

        data = parse_module.table_parser(board, fix)

        base_url = "http://cs.yonsei.ac.kr/"
        for x in data:
            x['href'] = base_url + x['href']
            
        self._set_data(data)
        self.sublist = [x['href'] for x in self.data]

    def save(self):
        # TODO
        if self.db is None:
            mylogger.info(self.data)

    def __str__(self):
        return f"<Computer Science Crawler> | Datetime : {self._datetime} | Address : {self.url}"

class CsMainCrawler(BaseCrawler):

    def __init__(self):
        super().__init__()
        self.html = None
        self.request_method = request_module.basic_request

    def request(self):
        self.html = self.request_method(self.url)
        # mylogger.debug(self.html)

    def parse(self):
        try:
            soup = BeautifulSoup(self.html, 'html.parser')
        except Exception as e:
            mylogger.warn(e)

        board = soup.find("table", {"class" : "board05"})
        data = {}
        data['title'] =  board.find("th", {"class" : "subject"}).text
        data['number'] = board.find("td", {"class" : "hit"}).\
            find("strong").text
        data['content'] = str(soup.find("div", {"class" : "b_cont01"}))

        self._set_data(data)
        # mylogger.debug(self.data)
    
    def save(self):
        # TODO
        if self.db is None:
            mylogger.info(self.data)
    
    def __str__(self):
        return f"<Cs Main Crawler> |  Address : {self.url}"

class CsNoticeCrawler(CsCrawler):

    def __init__(self):
        super().__init__()
        self.url = "http://cs.yonsei.ac.kr/sub05_1.php"
        self.sub_crawler = CsMainCrawler
        # from test_crawler import EmptyCrawler
        # self.sub_crawler = EmptyCrawler 

    def __str__(self):
        return f"<CS Faculty Notice Crawler> | Datetime : {self._datetime} | Address : {self.url}"

class CsGraduateNoticeCrawler(CsCrawler):

    def __init__(self):
        super().__init__()
        self.url = "http://cs.yonsei.ac.kr/sub05_1.php?nSeq=2"
        # from test_crawler import EmptyCrawler
        # self.sub_crawler = EmptyCrawler 
        self.sub_crawler = CsMainCrawler

    def __str__(self):
        return f"<CS Graduate School Notice Crawler> | Datetime : {self._datetime} | Address : {self.url}"

class CsScholarshipCrawler(CsCrawler):

    def __init__(self):
        super().__init__()
        self.url = "http://cs.yonsei.ac.kr/sub05_1.php?nSeq=3"
        # from test_crawler import EmptyCrawler
        # self.sub_crawler = EmptyCrawler 
        self.sub_crawler = CsMainCrawler

    def __str__(self):
        return f"<CS Scholarship Notice Crawler> | Datetime : {self._datetime} | Address : {self.url}"


    
if __name__=="__main__":
    crawlers = [
        CsNoticeCrawler, 
        CsGraduateNoticeCrawler, 
        CsScholarshipCrawler
        ]

    for n in crawlers:
        n().start()
