FROM tiangolo/uwsgi-nginx-flask:python2.7

RUN apt-get update && apt-get install -y libmysqlclient-dev python-bs4

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
