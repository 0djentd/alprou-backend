#!/bin/bash

python -m venv .venv
source .venv/bin/activate
python -m pip install Django djangorestframework httpie
