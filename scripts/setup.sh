#!/bin/bash

set -e

python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

manage.py check
manage.py createsuperuser
manage.py makemigrations
manage.py migrate
manage.py collectstatic --no-input
manage.py runserver
