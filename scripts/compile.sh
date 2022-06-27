#!/bin/bash

set -e

source .venv/bin/activate
./manage.py collectstatic --no-input
mkdir -p frontend/templates/frontend
cp static/alprou-frontend/index.html frontend/templates/frontend/index.html
sed -i 's/href="\//href="\/static\/alprou-fronten\//g' frontend/templates/frontend/index.html
sed -i 's/src="\//src="\/static\/alprou-fronten\//g' frontend/templates/frontend/index.html

