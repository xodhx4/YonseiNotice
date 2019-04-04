FROM python:3.7
RUN mkdir /yoncrawler
ADD . /yoncrawler
RUN pip install -r /yoncrawler/requirements.txt
CMD pytest /yoncrawler
