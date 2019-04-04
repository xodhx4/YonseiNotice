from yoncrawler.crawlers.base_cralwer import BaseCrawler
from yoncrawler.util import logger, request_module
import datetime
import requests
from bs4 import BeautifulSoup

mylogger = logger.getMyLogger()

class YonseiCrawler(BaseCrawler):

    def __init__(self):
        # https://www.yonsei.ac.kr/sc/support/notice.jsp
        # TODO : web page change
        super().__init__()
        self.name = "Yonsei Crawler"
        self.filter_key = 'href'
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

        board = soup.find('ul', {'class' : 'board_list'})
        # mylogger.debug(board)
        board_list = board.find_all('li', {'class' : None})

        self._set_data(list(map(self._parse_list, board_list)))
        # TODO : change safely when
        # 1. x hsa no href key
        # 2. x['href'] is None
        # 3. self.data is None
        self.sublist = [x['href'] for x in self.data]
        # mylogger.debug(self.board_list)


    def __str__(self):
        return f"<{self.name}> | Datetime : {self._datetime} | Address : {self.url}"

    def _parse_list(self, board):
        try:
            href = self.url + board.find('a')['href']
            title = board.find('strong').text.replace('\r', '').replace('\n', '').replace('\t', '').strip()
            spans = board.find_all('span', {'class' : 'tline'})
            category = spans[0].text
            date = spans[1].text
            board = {'href' : href, 'title': title, 'category' : category, 'date' : date}

            # mylogger.debug(board)
            return board
        except Exception as e:
            mylogger.warn(e)
            return None

class NoticeMainCrawler(BaseCrawler):

    def __init__(self):
        super().__init__()
        self.name = "Notice Main Crawler"
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
            
        board_view = soup.find('dl', {'class' : 'board_view'})
        title = soup.find('title').text
        date = board_view.find('span', {'class' : 'date'}).text
        cont_area = str(board_view.find('div', {'class' : 'cont_area'}))
        data = {'title' : title, 'date' : date, 'cont_area' : cont_area, 'href' : self.url}

        self._set_data(data)
    
    def __str__(self):
        return f"<{self.name}> |  Address : {self.url}"

class NoticeCrawler(YonseiCrawler):

    def __init__(self):
        super().__init__()
        self.name = "Notice Crawler"
        self.url = "https://www.yonsei.ac.kr/sc/support/notice.jsp"
        self.sub_crawler = NoticeMainCrawler

class ExternalCrawler(YonseiCrawler):

    def __init__(self):
        super().__init__()
        self.name = "External Crawler"
        self.url = "https://www.yonsei.ac.kr/sc/support/etc_notice.jsp"
        self.sub_crawler = NoticeMainCrawler
        # from test_crawler import EmptyCrawler
        # self.sub_crawler = EmptyCrawler

class ScholarshipCrawler(YonseiCrawler):

    def __init__(self):
        super().__init__()
        self.name = "Scholarship Crawler"
        self.url = "https://www.yonsei.ac.kr/sc/support/scholarship.jsp"
        self.sub_crawler = NoticeMainCrawler
        # from test_crawler import EmptyCrawler
        # self.sub_crawler = EmptyCrawler
        
    def _parse_list(self, board): 
        try: 
            href = self.url + board.find('a')['href']
            title = board.find('strong').text.replace('\r', '').replace('\n', '').replace('\t', '').strip()
            category = board.find('span', {'class' : 'title'}).find_all(text=True, recursive=False)[2]\
                .replace('\r', '').replace('\n', '').replace('\t', '').strip()
            spans = board.find_all('span', {'class' : 'tline'})
            date = spans[0].text
            start_date, end_date = date.split("~")
            board = {'href' : href, 'title': title, 'category' : category, 'start_date' : start_date, 'end_date' : end_date}

            # mylogger.debug(board)
            return board
        except Exception as e:
            mylogger.warn(e)
            return None

if __name__=='__main__':
    n = ScholarshipCrawler()
    n.start()
