import requests
from yoncrawler.util.logger import getMyLogger

def basic_request(url):
    mylogger = getMyLogger()
    mylogger.info(
        f"Crawl {url}"
    )

    try:
        response = requests.get(url)
        mylogger.info(response)
        encoding = response.encoding
        if encoding == "ISO-8859-1":
            response.encoding = 'euc-kr'

    except Exception as e:
        mylogger.error(
            f"{url} crawl exception\n" + e.__str__()
        )
        return None
    
    return response.text
    # mylogger.debug(self.html)