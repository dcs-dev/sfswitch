import os
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = 'test'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get('DEBUG', False) == '1'
DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG
# PYTHONIOENCODING="UTF-8"

ADMINS = (
    ('Dupont Circle Solutions', 'dev@dupontcirclesolutions.com')
)

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False

ALLOWED_HOSTS = ['*', '127.0.0.1', 'sftoolkit.test']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'enable_disable',
)

MIDDLEWARE_CLASSES = (
    # 'sslify.middleware.SSLifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Add in request context processor
from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.template.context_processors.request',
)

ROOT_URLCONF = 'sfswitch.urls'

WSGI_APPLICATION = 'sfswitch.wsgi.application'

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
BROKER_POOL_LIMIT = 1
BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
# REDISTOGO_URL = 'redis://localhost:6379/0'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)

# STATIC_ROOT = 'staticfiles'
STATIC_ROOT = 'static'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# SALESFORCE_REDIRECT_URI = os.environ['SALESFORCE_REDIRECT_URI']


# Replace this value with the URL from ngrok when running locally
# **NOTE: This must match the value in the connected app in Salesforce
# ngrok http 8000
LOCAL_PROXY_DOMAIN = '7f0944a98dd2.ngrok.io'
SALESFORCE_OAUTH_DOMAIN = LOCAL_PROXY_DOMAIN

SALESFORCE_OAUTH_DOMAIN = os.environ['SALESFORCE_OAUTH_DOMAIN']

# OAuth configuration for Web app
SALESFORCE_REDIRECT_URI = 'https://' + SALESFORCE_OAUTH_DOMAIN + '/oauth_response'
SALESFORCE_API_VERSION = int(os.environ['SALESFORCE_API_VERSION'])
SALESFORCE_CONSUMER_KEY = os.environ['SALESFORCE_CONSUMER_KEY']
SALESFORCE_CONSUMER_SECRET = os.environ['SALESFORCE_CONSUMER_SECRET']

# SALESFORCE_CONSUMER_KEY = '3MVG9Kip4IKAZQEVXeYMkMmDZFE7wRJE95oDlNnw7K_UOzkaTv9nKYuXXQqzhXUua5AJzsOy1IbeZeXZCMFcx'
# SALESFORCE_CONSUMER_SECRET = '38A767732BB51833692D1DD5760D59B9CDFEC068B13F6B1A907820340EBF8B72'
# # SALESFORCE_API_VERSION = '41'
# SALESFORCE_API_VERSION = '38'


