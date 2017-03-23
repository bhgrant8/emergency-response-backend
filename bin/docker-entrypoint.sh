#!/bin/bash

python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn emergency_response_api.wsgi:application -b :8000 --timeout 90 -w 5
# python manage.py runserver 0.0.0.0:8000
