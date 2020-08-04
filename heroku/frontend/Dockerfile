FROM node:lts-alpine as build-stage
WORKDIR /app
COPY /hello ./
RUN npm install
RUN npm run build
COPY /Procfile .

FROM nginx as production-stage
RUN mkdir /app
COPY --from=build-stage /app/dist /app

COPY default.conf.template /etc/nginx/conf.d/default.conf.template
COPY nginx.conf /etc/nginx/nginx.conf

CMD /bin/bash -c "envsubst '\$PORT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf" && nginx -g 'daemon off;'