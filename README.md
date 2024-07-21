NOTES
---

`Commands`

- python3 -m venv .venv
- source .venv/bin/activate
- sudo python3 -m pip install --upgrade pip
- python3 -m pip install django~=5.0.0
- django-admin startproject django_project .
- python3 manage.py runserver
- python3 -m pip install black

// start app
- python3 manage.py startapp posts

// start migrations for an app
- python3 manage.py makemigrations posts


- After running `python3 manage.py runserver` you may get several warnings related to migrations. so run `python3 manage.py migrate`. Once you run these command, the warnings must go away.

- use `pip freeze > requirements.txt`

To make use of Django-admin, we must first create a superuser
-  python3 manage.py createsuperuser


#### postgreSQL

- sudo su - postgres
- psql
- select version();
- \conninfo - gets connection information
- \password postgres (reset password for postgres user)
- \q (quit)
