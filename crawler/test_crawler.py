import pytest
from base_cralwer import BaseCrawler, basic_crawl
import datetime
import requests
from bs4 import BeautifulSoup
from logger import getMyLogger

# TODO
class EmptyCrawler(BaseCrawler):

        
    def crawl(self):
        pass

    def parse(self):
        pass

    def save(self):
        print(self)

    def __str__(self):
        return "This is Empty Crawler only for test"