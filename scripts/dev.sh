set -o allexport; source .env; \
# python manage.py makemigrations
# python manage.py migrate; \
gunicorn --reload -b :8082 mobile_api.wsgi --timeout 240; \
# celery -A mobile_api worker -l info
# celery -A mobile_api beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
set +o allexport