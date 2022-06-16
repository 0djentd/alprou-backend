#!/bin/bash

python -m venv .venv
source .venv/bin/activate
python -m pip install django djangorestframework django-model-utils django-simple-history
python -m pip install httpie pillow 
