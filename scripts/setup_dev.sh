#!/bin/bash

python -m venv .venv
source .venv/bin/activate
python -m pip install django djangorestframework httpie pillow
