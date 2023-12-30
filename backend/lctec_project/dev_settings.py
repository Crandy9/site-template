# same settings as production but with debug to true and ssl redirects off
# useful for running vs code or python debugger
# needed to run local Django dev server over http



'''
TO START DEV SERVER:
DJANGO_SETTINGS_MODULE=lctec_project.dev_settings python manage.py runserver


access the api at
http://localhost:8000/api/lctecadmin-6A6573757363687269737469736B696E67/login/?next=/api/lctecadmin-6A6573757363687269737469736B696E67/
'''

from .settings import * 

# for development
DEBUG = True

SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False