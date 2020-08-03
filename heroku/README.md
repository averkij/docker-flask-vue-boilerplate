# docker-flask-vue-boilerplate to heroku
Deploy to heroku

## Login

```
heroku login
heroku container login
```

## Build & push

```
heroku container:push --recursive -a <app-name>
```

## Release

```
heroku container:release backend frontend -a <app-name>
```

## Add dynos (containers)

```
heroku ps:scale backend=1 -a <app-name>
heroku ps:scale frontend=1 -a <app-name>
```

## Logs

```
heroku logs --tail
```