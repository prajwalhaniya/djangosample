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

- After running `python3 manage.py runserver` you may get several warnings related to migrations. so run `python3 manage.py migrate`. Once you run these command, the warnings must go away.

- use `pip freeze > requirements.txt`

