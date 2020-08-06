#! /usr/bin/env sh
set -e

/uwsgi-nginx-entrypoint2.sh

envsubst '\$PORT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

echo "[uwsgi]
socket = /tmp/uwsgi.sock
chmod-socket = 660
hook-master-start = unix_signal:15 gracefully_kill_them_all
need-app = true
die-on-term = true
# For debugging and testing
show-config = true" >> /etc/uwsgi/uwsgi.ini

exec "$@"