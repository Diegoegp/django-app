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
$ pip install django-cors-headers
```

```
$ django-admin startproject api .
$ cd api
$ django-admin startapp music
```

```
$ python manage.py createsuperuser --email jamserv@gmail.com --username janez
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
    'corsheaders'
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

### 4. deploy

```
$ python manage.py migrate
```

```
$ python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 30, 2019 - 22:38:42
Django version 2.2, using settings 'api.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

### 5. django shell (optional)
```
$ python manage.py shell
```

```
$ from api.music.models import Songs
$ song1 = Songs(title = 'Rubia Sol Morena Luna', artist = 'Caramelos de Cianuro')
$ song1.save()
```


### 6. front-end
###### Pre-Install
* NodeJS https://nodejs.org/es/download/
```
$ npm install --save
```

```
$ npm run serve
```
