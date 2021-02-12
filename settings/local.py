import os
from settings.base import *
from decouple import config


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = 'test'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG


# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False

ALLOWED_HOSTS = ['*', '127.0.0.1', 'sftoolkit.test']


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres', # os.environ['PG_DB_NAME']
        'USER': 'postgres', # os.environ['PG_USERNAME']
        'PASSWORD': 'sFt007k1t', # os.environ['PG_PASSWORD']
        'HOST': 'localhost', # os.environ['PG_HOST']
        'PORT': '5432'
    }
}

# Celery settings
CELERY_BROKER_POOL_LIMIT = 1
BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
# REDISTOGO_URL = 'redis://localhost:6379/0'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/


STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATIC_ROOT = 'static'

STATICFILES_DIRS = [
    # os.path.join(PROJECT_PATH, 'static'),
    os.path.join(BASE_DIR, 'sfswitch' 'static')
]


# Replace this value with the URL from ngrok when running locally
# **NOTE: This must match the value in the connected app in Salesforce
# ngrok http 8000
DJANGO_APP_DOMAIN =  'dcs.ngrok.io'


SALESFORCE_API_VERSION = config('SALESFORCE_API_VERSION', default='50')
SALESFORCE_CONSUMER_KEY  = config('SALESFORCE_CONSUMER_KEY', default='')
SALESFORCE_CONSUMER_SECRET  = config('SALESFORCE_CONSUMER_SECRET', default='')
SALESFORCE_REDIRECT_URI = 'https://' + DJANGO_APP_DOMAIN + '/oauth_response'




