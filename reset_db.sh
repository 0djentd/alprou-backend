#!/bin/bash

fd -t d -HI __pycache__ -X rm -r 
fd -t d -HI .mypy_cache -X rm -r 
fd -t d -HI migrations -X rm -r 

mkdir core/migrations
mkdir api/migrations
touch core/migrations/__init__.py
touch api/migrations/__init__.py

rm db.sqlite3
