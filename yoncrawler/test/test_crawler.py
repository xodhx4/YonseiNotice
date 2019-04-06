import sys
import os
parent_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(os.path.join(parent_dir, '..'))
import pytest
import datetime
import requests
from bs4 import BeautifulSoup
from yoncrawler.crawlers.base_cralwer import BaseCrawler
from yoncrawler.crawlers import yonsei_crawler, cs_crawler, sb_crawler
from yoncrawler.util.request_module import basic_request
from yoncrawler.util.logger import getMyLogger
from yoncrawler.db.simple_db import TinyDBSaver
from yoncrawler.db.mongo_db import MongoDBSaver

tmp = os.path.join(os.path.dirname(__file__), 'tmp')
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
    fn = crawler_test_templete(yonsei_crawler.NoticeCrawler)
    fn()
              
def test_ExternalCrawler_start():
    fn = crawler_test_templete(yonsei_crawler.ExternalCrawler)
    fn()


def test_ScholarshipCrawler_start():
    fn = crawler_test_templete(yonsei_crawler.ScholarshipCrawler)
    fn()

def test_CsNoticeCrawler_start():
    fn = crawler_test_templete(cs_crawler.CsNoticeCrawler)
    fn()

def test_CsGraduateNoticeCrawler_start():
    fn = crawler_test_templete(cs_crawler.CsGraduateNoticeCrawler)
    fn()


def test_CsScholarshipCrawler_start():
    fn = crawler_test_templete(cs_crawler.CsScholarshipCrawler)
    fn()

def test_SbNoticeCrawler_start():
    fn = crawler_test_templete(sb_crawler.SbNoticeCrawler)
    fn()

def test_SbCareerCrawler_start():
    fn = crawler_test_templete(sb_crawler.SbCareerCrawler)
    fn()

def crawler_test_templete(crawler):
    def fn():
        try:
            n = crawler()
            n.start()
            n._db = TinyDBSaver(db_name = n.subject, table_name=n.name, dir_path=tmp)
            n.start()
            n._db = MongoDBSaver(db_name=n.subject, table_name=n.name)
            n.start()
            assert True
        except Exception as e:
            pytest.fail(e)
    
    return fn
