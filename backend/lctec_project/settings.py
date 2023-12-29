from pathlib import Path
import os

import environ
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# look for .env outside of repo dir
env = environ.Env()
env_path = Path(__file__).resolve().parent.parent.parent
env_file = env_path / '.env'
environ.Env.read_env(env_file)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# for production
DEBUG = False

SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# can find the endpoint's secret by running `stripe listen` in CLI
# STRIPE_WEBHOOK_SECRET = env("STRIPE_WEBHOOK_SECRET")

# stripe data
# STRIPE_PK = env("STRIPEPK")
# STRIPE_SK = env("STRIPESK")
# STRIPE_DOMAIN = env("STRIPE_DOMAIN")

# add digitalocean vps ip 
ALLOWED_HOSTS = ['localhost', 
                '127.0.0.1']


# rest framework global settings
# authentication classes: https://www.django-rest-framework.org/api-guide/settings/#default_authentication_classes
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    # permission policy: https://www.django-rest-framework.org/api-guide/permissions/#setting-the-permission-policy
    # can override these in views. Don't forget to add a comma
    'DEFAULT_PERMISSION_CLASSES': (
        # allow anyone to access api data
        # 'rest_framework.permissions.AllowAny', 
        # do not allow anyone to access API endpoints unless user is authenticated
        # 'rest_framework.permissions.IsAuthenticated', 
        # allow full access to authenticated users, but allow read-only access to unauthenticated users
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer', # makes api views JSON data only
    ),
}



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    # djoser is a REST implementation of Django authentication system. Provides token based authentication
    'djoser',
]

# set my custom user model (appname.Django model name)
# AUTH_USER_MODEL = 'lctec_user.Lctec_User'


# add custom backend, if it fails, Django will use default backend
# also may be needed for admin page
#  to set custom backend, use this syntax:
# appname.backendfilepyname.modelname
# AUTHENTICATION_BACKENDS = (
    # 'sheriff_crandy_project.lctec_backend.Lctec_Backend',
    # 'django.contrib.auth.backends.ModelBackend',
    #'lctec_user.lctec_backend.Lctec_Backend',
    #)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# frontend server. Change to live server address for production
# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1:8080",
#     "http://localhost:8080",
#     "https://sheriffcrandymusic.local:9443",
#     "https://sheriffcrandymusic.com"
# ]

# required to accomodate howlerjs `Accept-Ranges`: `bytes`` header
# XMLHttpRequest (xhr) object
# needed for seeking the audio when html5 = true
# CORS_ALLOW_METHODS = [
#     'DELETE',
#     'GET',
#     'OPTIONS',
#     'PATCH',
#     'POST',
#     'PUT'
# ]

# CORS_ALLOW_HEADERS = [
#     'accept-ranges',
#     'accept',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
#     'authorization'
# ]


ROOT_URLCONF = 'lctec_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lctec_project.wsgi.application'


# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Simple Mail Transfer Protocol SMPT config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = True
# email address that sends emails  
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD generated by Google. First you have to enable 2-step verification
# Go to Google-> manage Google account -> Security -> Sigining in to Google -> App passwords ->
# if you can't find app passwords. Search for it in the searchbar above
# click select app and choose Mail or Other -> select device name (make a custom name) -> generate -> get password and put it in .env file
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD') 

EMAIL_ACTIVE_FIELD = 'is_active'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

# media dir for files. This dir is created when the first model objects are created (either through admin page or otherwise)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# receive error details of exceptions raised in the request/response cycle.
# https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-ADMINS
ADMINS = [('Linden', 'lctechnology@protonmail.com')]

# managers get broken link notifications
MANAGERS = [('Linden', 'lctechnology@protonmail.com')]

# logging 
# https://docs.python.org/3.10/library/logging.html
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False, # django has default loggers that we can use

    # shows how you want to display message 
    'formatters': {
        'main_formatter': {
            # we want time, level, module and message 
            # use format of attribute name founde here: https://docs.python.org/3.10/library/logging.html
            'format': "\n{asctime} - {levelname} - {module} - {message}\n\n",

            'style': "{",
            # '()': CustomJsonFormatter, using custom class in logging_formatters.py
        }
    },

    # where to store/write messages
    'handlers': {

        # file handler, writes logs to file
        'file': {
            'level': 'DEBUG', # show all logging levels from DEBUG and up (DEBUG 10, INFO 20, WARNING 30 , ERROR 40 , CRITICAL 50)
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'backend_logger/logs.txt', # file that this handler will write log to
            'formatter': 'main_formatter',
        },

    },

   # logger object
    'loggers': {
        'main': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG', # show all logging levels from INFO and up (INFO 20, WARNING 30 , ERROR 40 , CRITICAL 50)
        },
    }
}