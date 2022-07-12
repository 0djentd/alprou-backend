[![Django CI](https://github.com/0djentd/alprou-backend/actions/workflows/django.yml/badge.svg)](https://github.com/0djentd/alprou-backend/actions/workflows/django.yml)

# Alprou (backend)
![screenshot](screenshot_alprou_backend.png)
## Description
Backend server for [Alprou](https://github.com/0djentd/alprou).

## Installation
```
git clone https://github.com/0djentd/alprou_backend.git
cd alprou_backend
git pull --recurse-submodules
pipenv install
```

Then create files named `django_key` and `db_config.py`.

```
pipenv shell
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```
