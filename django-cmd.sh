#!/bin/bash

cd /app/

echo "#####migrating database#####"
python3 manage.py makemigrations

echo "#####migrate database#######"
python3 manage.py migrate

echo "#######collecting static######"
python3 manage.py collectstatic --no-input

echo "starting wsgi with gunicorn"
gunicorn tweetersphere.wsgi:application --bind 0.0.0.0:8000