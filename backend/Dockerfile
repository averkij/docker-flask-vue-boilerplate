From python:3.8-alpine

WORKDIR /backend

ADD . /backend

RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]