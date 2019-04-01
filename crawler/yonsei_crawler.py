from base_cralwer import BaseCrawler, basic_crawl
import datetime
import requests
from bs4 import BeautifulSoup
from logger import getMyLogger

mylogger = getMyLogger()

class YonseiCrawler(BaseCrawler):

    def __init__(self):
        # https://www.yonsei.ac.kr/sc/support/notice.jsp
        # TODO : web page change
        super().__init__()
        self.html = None
        self._datetime = datetime.datetime.now()
        self.crawl_method = basic_crawl
    
        
    def crawl(self):
        self.html = self.crawl_method(self.url)
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
        self.sublist = [x['href'] for x in self.data]
        # mylogger.debug(self.board_list)

    def save(self):
        # TODO
        if self.db is None:
            mylogger.info(self.data)

    def __str__(self):
        return f"<Yonsei Crawler> | Datetime : {self._datetime} | Address : {self.url}"

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

class NoticeCrawler(YonseiCrawler):

    def __init__(self):
        super().__init__()
        self.url = "https://www.yonsei.ac.kr/sc/support/notice.jsp"
        self.sub_crawler = NoticeMainCrawler

    def __str__(self):
        return f"<Notice Crawler> | Datetime : {self._datetime} | Address : {self.url}"

class ExternalCrawler(YonseiCrawler):

    def __init__(self):
        super().__init__()
        self.url = "https://www.yonsei.ac.kr/sc/support/etc_notice.jsp"
        self.sub_crawler = NoticeMainCrawler
        # from test_crawler import EmptyCrawler
        # self.sub_crawler = EmptyCrawler

    def __str__(self):
        return f"<External Crawler> | Datetime : {self._datetime} | Address : {self.url}"

class NoticeMainCrawler(BaseCrawler):

    def __init__(self):
        super().__init__()
        self.html = None
        self.crawl_method = basic_crawl


    def crawl(self):
        self.html = self.crawl_method(self.url)
        # mylogger.debug(self.html)

    def parse(self):
        try:
            soup = BeautifulSoup(self.html, 'html.parser')
        except Exception as e:
            mylogger.warn(e)
            
        board_view = soup.find('dl', {'class' : 'board_view'})
        title = soup.find('title').text
        date = board_view.find('span', {'class' : 'date'}).text
        cont_area = board_view.find('div', {'class' : 'cont_area'})
        data = {'title' : title, 'date' : date, 'cont_area' : cont_area}

        self._set_data(data)
    
    def save(self):
        # TODO
        if self.db is None:
            mylogger.info(self.data)
    
    def __str__(self):
        return f"<Notice Main Crawler> |  Address : {self.url}"

if __name__=='__main__':
    n = ExternalCrawler()
    n.start()
