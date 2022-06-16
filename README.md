# Alprou (backend)
## Description
Backend server for [Alprou](https://github.com/0djentd/alprou).

## Installation
```
git clone https://github.com/0djentd/alprou_backend.git
cd alprou_backend
./scripts/setup_dev.sh
```

Then create file named ```django_key```.

```
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
```