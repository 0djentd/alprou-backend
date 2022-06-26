#!/bin/bash

set -e

cd frontend/frontend
npm install
npm run build
cd ../..
source .venv/bin/activate
./manage.py collectstatic --no-input
mkdir -p frontend/templates/frontend
cp static/index.html frontend/templates/frontend/index.html
sed -i 's/href="\//href="\/static\//g' frontend/templates/frontend/index.html
sed -i 's/src="\//src="\/static\//g' frontend/templates/frontend/index.html

