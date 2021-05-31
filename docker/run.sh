#!/usr/bin/env bash

cd /s107_photofind/ || exit 1
python manage.py migrate
python manage.py collectstatic --noinput
daphne -b 0.0.0.0 -p 8091 --access-log /var/log/s107_photofind/daphne_access.log ya.asgi:application
