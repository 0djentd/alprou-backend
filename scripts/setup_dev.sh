#!/bin/bash

python -m venv .venv
source .venv/bin/activate
python -m pip install django djangorestframework django-cors-headers django-model-utils django-simple-history django-taggit
python -m pip install httpie pillow 
