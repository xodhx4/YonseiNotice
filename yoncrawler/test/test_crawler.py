import sys
import os
parent_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(os.path.join(parent_dir, '..'))
import pytest
import datetime
import requests
from bs4 import BeautifulSoup
from yoncrawler.crawlers.base_cralwer import BaseCrawler
from yoncrawler.crawlers import yonsei_crawler, cs_crawler
from yoncrawler.util.request_module import basic_request
from yoncrawler.util.logger import getMyLogger

# TODO
class EmptyCrawler(BaseCrawler):

        
    def request(self):
        pass

    def parse(self):
        pass

    def save(self):
        print(self)

    def __str__(self):
        return "This is Empty Crawler only for test"

def test_NoticeCrawler_start():
    try:    
        n = yonsei_crawler.NoticeCrawler()
        n.start()
        assert True
    except Exception as e:
        pytest.fail(e)
    
def test_ExternalCrawler_start():
    try:
        n = yonsei_crawler.ExternalCrawler()
        n.start()
        assert True
    except Exception as e:
        pytest.fail(e)


def test_ScholarshipCrawler_start():
    try:
        n = yonsei_crawler.ScholarshipCrawler()
        n.start()
        assert True
    except Exception as e:
        pytest.fail(e)

def test_CsNoticeCrawler_start():
    try:
        n = cs_crawler.CsNoticeCrawler()
        n.start()
        assert True
    except Exception as e:
        pytest.fail(e)

def test_CsGraduateNoticeCrawler_start():
    try:
        n = cs_crawler.CsGraduateNoticeCrawler()
        n.start()
        assert True
    except Exception as e:
        pytest.fail(e)


def test_CsScholarshipCrawler_start():
    try:
        n = cs_crawler.CsScholarshipCrawler()
        n.start()
        assert True
    except Exception as e:
        pytest.fail(e)

