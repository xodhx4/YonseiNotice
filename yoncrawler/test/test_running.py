import sys
import os
parent_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(os.path.join(parent_dir, '..'))
import pytest
import datetime
import requests
from bs4 import BeautifulSoup
from yoncrawler.crawlers.base_cralwer import BaseCrawler
from yoncrawler.crawlers import yonsei_crawler, cs_crawler, sb_crawler, ec_crawler, as_crawler
from yoncrawler.util.request_module import basic_request
from yoncrawler.util.logger import getMyLogger
from yoncrawler.db.simple_db import TinyDBSaver

tmp = os.path.join(os.path.dirname(__file__), 'tmp')

def simple_running(crawler):
    def fn():
        try:
            n = crawler()
            n.start()
            assert True
        except Exception as e:
            pytest.fail(e)

    return fn

def page_running(crawler, page):
    def fn():
        try:
            n = crawler(page=page)
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

# def test_YonseiCrawler_page_runnnig():
#     fn = page_running(yonsei_crawler.NoticeCrawler, page=2)
#     fn()

# def test_CsCrawler_page_runnnig():
#     fn = page_running(cs_crawler.CsNoticeCrawler, page=2)
#     fn()

# def test_SbCrawler_page_runnnig():
#     fn = page_running(sb_crawler.SbNoticeCrawler, page=2)
#     fn()

# def test_AsNoticeCrawler_running():
#     fn = simple_running(as_crawler.AsNoticeCrawler)
#     fn()

# def test_AsGraduateNoticeCrawler_running():
#     fn = simple_running(as_crawler.AsGraduateNoticeCrawler)
#     fn()

# def test_AsCareerCrawler_running():
#     fn = simple_running(as_crawler.AsCareerCrawler)
#     fn()

# def test_AsNoticeCrawler_page_running():
#     fn = page_running(as_crawler.AsNoticeCrawler, 2)
#     fn()

# def test_AsGraduateNoticeCrawler_page_running():
#     fn = page_running(as_crawler.AsGraduateNoticeCrawler, 2)
#     fn()

# def test_AsCareerCrawler_page_running():
#     fn = page_running(as_crawler.AsCareerCrawler, 2)
#     fn()