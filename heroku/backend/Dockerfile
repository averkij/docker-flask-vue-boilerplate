From python:3.8-alpine

WORKDIR /backend

ADD . /backend

RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	;
RUN pip install -r requirements.txt;
RUN apk del .build-deps;

CMD ["uwsgi", "uwsgi.ini"]