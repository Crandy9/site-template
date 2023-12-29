# same settings as production but with debug to true and ssl redirects off
# useful for running vs code or python debugger
# needed to run local Django dev server over http



'''
TO START DEV SERVER:
DJANGO_SETTINGS_MODULE=lctec_project.dev_settings python manage.py runserver


access the backend at 
127.0.0.1:8000
'''

from .settings import * 

# for development
DEBUG = True

SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False