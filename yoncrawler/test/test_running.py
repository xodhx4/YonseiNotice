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

tmp = os.path.join(os.path.dirname(__file__), 'tmp')
# TODO

def simple_running(crawler):
    def fn():
        try:
            n = crawler()
            n.start()
            assert True
        except Exception as e:
            pytest.fail(e)

    return fn

# def test_SbNoticeCrawler_running():
#     fn = simple_running(sb_crawler.SbNoticeCrawler)
#     fn()

# def test_SbCareerCrawler_running():
#     fn = simple_running(sb_crawler.SbCareerCrawler)
#     fn()