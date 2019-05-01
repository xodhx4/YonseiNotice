from yoncrawler.crawlers import cs_crawler, sb_crawler, yonsei_crawler, ec_crawler
from yoncrawler.db import simple_db

def _getCrawlerWithNoneDB(crawler):
    n = crawler()
    n.start()
    return n.data

def _getCrawlerWithTinyDB(crawler):
    n = crawler()
    n.db = simple_db.TinyDBSaver
    n.start()
    return n.data

def getYonseiNotice():
    return _getCrawlerWithNoneDB(yonsei_crawler.NoticeCrawler)

def getYonseiExternal():
    return _getCrawlerWithNoneDB(yonsei_crawler.ExternalCrawler)

def getYonseiScholarship():
    return _getCrawlerWithNoneDB(yonsei_crawler.ScholarshipCrawler)

def getCsNotice():
    return _getCrawlerWithNoneDB(cs_crawler.CsNoticeCrawler)

def getCsGraduateNotice():
    return _getCrawlerWithNoneDB(cs_crawler.CsGraduateNoticeCrawler)

def getCsScholarship():
    return _getCrawlerWithNoneDB(cs_crawler.CsScholarshipCrawler)

def getSbNotice():
    return _getCrawlerWithNoneDB(sb_crawler.SbNoticeCrawler)

def getSbCareer():
    return _getCrawlerWithNoneDB(sb_crawler.SbCareerCrawler)

def getEcNotice():
    return _getCrawlerWithNoneDB(ec_crawler.EcNoticeCrawler)

def getEcGraduateNotice():
    return _getCrawlerWithNoneDB(ec_crawler.EcGraduateNoticeCrawler)

def getEcSeminar():
    return _getCrawlerWithNoneDB(ec_crawler.EcSeminarCrawler)

def getEcCareer():
    return _getCrawlerWithNoneDB(ec_crawler.EcCareerCrawler)

def getYonseiNoticeJson():
    return _getCrawlerWithTinyDB(yonsei_crawler.NoticeCrawler)

def getYonseiExternalJson():
    return _getCrawlerWithTinyDB(yonsei_crawler.ExternalCrawler)

def getYonseiScholarshipJson():
    return _getCrawlerWithTinyDB(yonsei_crawler.ScholarshipCrawler)

def getCsNoticeJson():
    return _getCrawlerWithTinyDB(cs_crawler.CsNoticeCrawler)

def getCsGraduateNoticeJson():
    return _getCrawlerWithTinyDB(cs_crawler.CsGraduateNoticeCrawler)

def getCsScholarshipJson():
    return _getCrawlerWithTinyDB(cs_crawler.CsScholarshipCrawler)

def getSbNoticeJson():
    return _getCrawlerWithTinyDB(sb_crawler.SbNoticeCrawler)

def getSbCareerJson():
    return _getCrawlerWithTinyDB(sb_crawler.SbCareerCrawler)

def getEcNoticeJson():
    return _getCrawlerWithTinyDB(ec_crawler.EcNoticeCrawler)

def getEcGraduateNoticeJson():
    return _getCrawlerWithTinyDB(ec_crawler.EcGraduateNoticeCrawler)

def getEcSeminarJson():
    return _getCrawlerWithTinyDB(ec_crawler.EcSeminarCrawler)

def getEcCareerJson():
    return _getCrawlerWithTinyDB(ec_crawler.EcCareerCrawler)
