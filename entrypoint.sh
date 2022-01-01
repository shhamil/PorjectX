#! /bin/bash

exec gunicorn config.wsgi:application -b 0.0.0.0:8000 --reload
