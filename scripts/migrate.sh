set -o allexport; source .env; \
python manage.py migrate $1; \
set +o allexport