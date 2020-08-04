#build web app
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY /hello ./
RUN npm install
RUN npm run build

FROM python:3.8-alpine3.11 as production-stage

#install nginx
COPY install-nginx-alpine.sh /
RUN sh /install-nginx-alpine.sh

EXPOSE 80
EXPOSE 443

#ENV LISTEN_PORT 80
#ENV ALPINEPYTHON python3.8

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