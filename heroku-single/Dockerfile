#build web app
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY /vue_app ./
RUN npm install
RUN npm run build

#setup flask app
FROM tiangolo/uwsgi-nginx-flask:python3.8 as production-stage

#serve static/index.html
ENV STATIC_INDEX 1

#heroku
# RUN echo ${PORT}
#ENV LISTEN_PORT 9000

#COPY ./python_app/nginx.conf /etc/nginx/conf.d/nginx.conf

# ENV PORT 11000

COPY default.conf.template /etc/nginx/conf.d/default.conf
# RUN /bin/bash -c "envsubst '\$PORT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf"

COPY ./python_app /app
RUN mkdir /app/static
COPY --from=build-stage /app/dist /app/static

# CMD /bin/bash -c "envsubst '\$PORT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf" && nginx -g 'daemon off;'