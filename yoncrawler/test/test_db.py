import sys
import os
import json
parent_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(os.path.join(parent_dir, '..'))
import pytest
import datetime
from yoncrawler.db.base_db import NotSupportedError
from yoncrawler.db.simple_db import JsonSaver

def test_JsonSaver_create_listOfDict():
    try:
        listOfDict = [{'href': 'https://www.yonsei.ac.kr/sc/support/notice.jsp?mode=view&article_no=174085&board_wrapper=%2Fsc%2Fsupport%2Fnotice.jsp&pager.offset=0&board_no=15', 'title': '[외국어학당] 2019-2학기 정규 프로그램 등록 안내', 'category': '외국어학당', 'date': '2019.03.26'}, {'href': 'https://www.yonsei.ac.kr/sc/support/notice.jsp?mode=view&article_no=174084&board_wrapper=%2Fsc%2Fsupport%2Fnotice.jsp&pager.offset=0&board_no=15', 'title': '[외국어학당] 연세대 재학생을 위한 Zoom-Live English 강좌안내', 'category': '외국어학당', 'date': '2019.03.26'}, {'href': 'https://www.yonsei.ac.kr/sc/support/notice.jsp?mode=view&article_no=174015&board_wrapper=%2Fsc%2Fsupport%2Fnotice.jsp&pager.offset=0&board_no=15', 'title': '교직과정 이수자를 위한 심폐소생술 특강', 'category': '교육과학대', 'date': '2019.03.25'}, {'href': 'https://www.yonsei.ac.kr/sc/support/notice.jsp?mode=view&article_no=174014&board_wrapper=%2Fsc%2Fsupport%2Fnotice.jsp&pager.offset=0&board_no=15', 'title': '[외국어학당] 서포터즈 FLI-er 5기 모집 안내', 'category': '외국어학당', 'date': '2019.03.25'}, {'href': 'https://www.yonsei.ac.kr/sc/support/notice.jsp?mode=view&article_no=173975&board_wrapper=%2Fsc%2Fsupport%2Fnotice.jsp&pager.offset=0&board_no=15', 'title': '2019-1학기 분할납부 4회 신청자 2차 납부(4-2 Tuition installment payment guideline)  만료', 'category': '총무처 재무회계팀', 'date': '2019.03.22'}, {'href': 'https://www.yonsei.ac.kr/sc/support/notice.jsp?mode=view&article_no=173875&board_wrapper=%2Fsc%2Fsupport%2Fnotice.jsp&pager.offset=0&board_no=15', 'title': '2020-1학기 해외파견프로그램(교환학생) 설명회 및 전형 일정 안내', 'category': '국제처 국제교류팀', 'date': '2019.03.19'}, {'href': 'https://www.yonsei.ac.kr/sc/support/notice.jsp?mode=view&article_no=173874&board_wrapper=%2Fsc%2Fsupport%2Fnotice.jsp&pager.offset=0&board_no=15', 'title': '[YDEC] 2019-1 Adobe CC ID 신청 안내', 'category': 'YDEC', 'date': '2019.03.19'}, {'href': 'https://www.yonsei.ac.kr/sc/support/notice.jsp?mode=view&article_no=173841&board_wrapper=%2Fsc%2Fsupport%2Fnotice.jsp&pager.offset=0&board_no=15', 'title': '2019 고등교육혁신원 워크스테이션 모집', 'category': '고등교육혁신원', 'date': '2019.03.18'}, {'href': 'https://www.yonsei.ac.kr/sc/support/notice.jsp?mode=view&article_no=173775&board_wrapper=%2Fsc%2Fsupport%2Fnotice.jsp&pager.offset=0&board_no=15', 'title': 'Y-IBS과학원 석박사과정 입학설명회 안내  만료', 'category': 'Y-IBS과학원', 'date': '2019.03.15'}, {'href': 'https://www.yonsei.ac.kr/sc/support/notice.jsp?mode=view&article_no=173714&board_wrapper=%2Fsc%2Fsupport%2Fnotice.jsp&pager.offset=0&board_no=15', 'title': '2019학년도 여름 계절제 수강 희망 교과목 수요조사 안내  만료', 'category': '교무처 학사지원팀   ', 'date': '2019.03.14'}]
        path = os.path.dirname(__file__)
        if os.path.exists(os.path.join(path, "test.json")):
            os.remove(os.path.join(path,  "test.json"))
            print("Remove File")
        filepath = JsonSaver(dir_path=path).create(listOfDict, "test")
        with open(filepath) as f:
            data = json.load(f)
        assert listOfDict == data
    except Exception as e:
        pytest.fail(e)

def test_JsonSaver_read():
    with pytest.raises(NotSupportedError):
        JsonSaver().read()

def test_JsonSaver_update():
    with pytest.raises(NotSupportedError):
        JsonSaver().update()

def test_JsonSaver_delete():
    with pytest.raises(NotSupportedError):
        JsonSaver().delete()



