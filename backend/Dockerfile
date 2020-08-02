From python:3.8-alpine

WORKDIR /backend

ADD . /backend

RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	;
RUN install --no-cache-dir -r requirements.txt; \
	apk del .build-deps;

CMD ["uwsgi", "app.ini"]