# Music API
**_django-app_**

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

### 2. Data base Conect

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


