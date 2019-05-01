import sys
import os
parent_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(os.path.join(parent_dir, '..'))
import pytest
import datetime
import requests
from bs4 import BeautifulSoup
from yoncrawler.crawlers.base_cralwer import BaseCrawler
from yoncrawler.crawlers import yonsei_crawler, cs_crawler, sb_crawler, ec_crawler
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

def test_EcNoticeCrawler_running():
    fn = simple_running(ec_crawler.EcNoticeCrawler)
    fn()

def test_EcGraduateNoticeCrawler_running():
    fn = simple_running(ec_crawler.EcGraduateNoticeCrawler)
    fn()

def test_EcSeminarCrawler_running():
    fn = simple_running(ec_crawler.EcSeminarCrawler)
    fn()

def test_EcCareerCrawler_running():
    fn = simple_running(ec_crawler.EcCareerCrawler)
    fn()

def test_EcNoticeCrawler_page_running():
    fn = page_running(ec_crawler.EcNoticeCrawler, 2)
    fn()

def test_EcGraduateNoticeCrawler_page_running():
    fn = page_running(ec_crawler.EcGraduateNoticeCrawler, 1)
    fn()

def test_EcSeminarCrawler_page_running():
    fn = page_running(ec_crawler.EcSeminarCrawler, 2)
    fn()

def test_EcCareerCrawler_page_running():
    fn = page_running(ec_crawler.EcCareerCrawler, 2)
    fn()