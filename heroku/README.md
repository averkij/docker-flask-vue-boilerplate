# docker-flask-vue-boilerplate to heroku
Deploy to heroku

## Login

```
heroku login
heroku container:login
```

## Build & push

```
heroku container:push web -a <app-name>
heroku container:push web -a <app-name-be>
```

## Release

```
heroku container:release web -a <app-name>
heroku container:release web -a <app-name-be>
```

## Add dynos (containers)

```
heroku ps:scale web=1 -a <app-name>
heroku ps:scale web=1 -a <app-name-be>
```

## Logs

```
heroku logs --tail -a <app-name>
```