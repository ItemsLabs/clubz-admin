#!/bin/bash
set -e

if [ "$1" = "server" ]; then
  python manage.py migrate
  python manage.py createcachetable
  python manage.py collectstatic --noinput
  gunicorn -b :8000 mobile_api.wsgi --timeout 240
else

  if [ "$1" = "celery-worker" ]; then
    celery -A mobile_api worker --concurrency=15  -l warn
  else

    if [ "$1" = "celery-beat" ]; then
      rm -f celerybeat.pid
      celery -A mobile_api beat -l warn --scheduler django_celery_beat.schedulers:DatabaseScheduler
    fi

  fi

fi
