# django-app

### Configure Enviroment


1. mkdir janez_django
2. cd janez_django
3. python3.6 -m venv env
4. source env/bin/activate
5. pip install django
6. pip install djangorestframework
7. django-admin startproject api .
8. cd api
9. django-admin startapp music
10. cd ..
11. python manage.py migrate
12. python manage.py createsuperuser --email admin@example.com --username admin
13. python manage.py runserver


