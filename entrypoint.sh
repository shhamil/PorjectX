#! /bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata extrasens.json
python manage.py collectstatic --no-input
exec gunicorn config.wsgi:application -b 0.0.0.0:8000 --reload
