# Music API
**_django-app REST Template_**

### 1. Configure Enviroment

```
$ mkdir janez_django
$ cd janez_django
```

```
$ python3.6 -m venv env
$ source env/bin/activate
```

```
$ pip install django
$ pip install djangorestframework
```

```
$ django-admin startproject api .
$ cd api
$ django-admin startapp music
$ cd ..
```
```
$ python manage.py migrate
```

```
$ python manage.py createsuperuser --email janez@gmail.com --username janez
```

```
$ python manage.py runserver
```

### 2. Data base (install driver)

```
$ sudo apt-get install python3-dev
```

```
$ sudo apt-get install python3-dev libmysqlclient-dev
```

```
$ pip install mysqlclient
```

### 3. setting.py

1. Add **'rest_framework',** line
2. Add **'api.music',** line
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api.music',
]
```
3. Data base configuration
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_study',
        'USER': 'root',
        'PASSWORD': 'pass1234',
        'HOST': '192.168.0.1',
        'PORT': '3307',
    },
}
```

### 4. django shell
```
$ python manage.py shell
```

```
$ from api.music.models import Songs
$ song1 = Songs(title = 'Rubia Sol Morena Luna', artist = 'Caramelos de Cianuro')
$ song1.save()
```
