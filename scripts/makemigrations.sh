set -o allexport; source .env; \
python manage.py makemigrations $1; \
set +o allexport