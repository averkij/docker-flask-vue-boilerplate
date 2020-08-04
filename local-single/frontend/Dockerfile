#build web app
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY /hello ./
RUN npm install
RUN npm run build

FROM python:3.8-alpine3.11 as production-stage

#setup python app
RUN mkdir /app
WORKDIR /app
ADD ./app /app
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers;
RUN pip install -r requirements.txt;
RUN apk del .build-deps;

#install uWSGI
RUN apk add --no-cache uwsgi-python3
COPY uwsgi.ini /etc/uwsgi/

#install nginx
COPY install-nginx-alpine.sh /
RUN sh /install-nginx-alpine.sh

EXPOSE 80
EXPOSE 443

ENV UWSGI_PLUGIN python3

# Which uWSGI .ini file should be used, to make it customizable
ENV UWSGI_INI /app/uwsgi.ini

# By default, run 2 processes
ENV UWSGI_CHEAPER 2

# By default, when on demand, run up to 16 processes
ENV UWSGI_PROCESSES 16

# By default, allow unlimited file sizes, modify it to limit the file sizes
# To have a maximum of 1 MB (Nginx's default) change the line to:
# ENV NGINX_MAX_UPLOAD 1m
ENV NGINX_MAX_UPLOAD 0

# By default, Nginx will run a single worker process, setting it to auto
# will create a worker for each CPU core
ENV NGINX_WORKER_PROCESSES 1

# By default, Nginx listens on port 80.
# To modify this, change LISTEN_PORT environment variable.
# (in a Dockerfile or with an option for `docker run`)
ENV LISTEN_PORT 80

# Used by the entrypoint to explicitly add installed Python packages 
# and uWSGI Python packages to PYTHONPATH otherwise uWSGI can't import Flask
ENV ALPINEPYTHON python3.8

RUN apk add --no-cache supervisor
COPY supervisord-alpine.ini /etc/supervisor.d/supervisord.ini

COPY start.sh /start.sh
RUN chmod +x /start.sh

#COPY entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh
#ENTRYPOINT ["sh", "/entrypoint.sh"]

#copy frontend
RUN mkdir /web
COPY --from=build-stage /app/dist /web
COPY nginx.conf /etc/nginx/nginx.conf

WORKDIR /web

CMD ["/start.sh"]