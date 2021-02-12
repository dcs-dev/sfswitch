import os
import sys
import logging.config
from celery import signals
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse
    

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


ADMINS = (
    ('Dupont Circle Solutions', 'dev@dupontcirclesolutions.com')
)

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
    'sfswitch'
)

MIDDLEWARE = (
    # 'sslify.middleware.SSLifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

ROOT_URLCONF = 'sfswitch.urls'

WSGI_APPLICATION = 'sfswitch.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# import dj_database_url


# Celery settings
# BROKER_POOL_LIMIT = 1
# BROKER_URL = 'redis://127.0.0.1:6379/0'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
# # REDISTOGO_URL = 'redis://localhost:6379/0'

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
# STATIC_ROOT = 'static'
# STATIC_URL = '/static/'
# ADMIN_MEDIA_PREFIX = '/static/admin/'
#
# STATICFILES_DIRS = (
#     os.path.join(PROJECT_PATH, 'static'),
# )

##STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# SALESFORCE_REDIRECT_URI = os.environ['SALESFORCE_REDIRECT_URI']

############################################################
# Logging Setup
############################################################
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                        'pathname=%(pathname)s lineno=%(lineno)s ' +
                        'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'stream':sys.stdout
        }
    },
    'loggers': {
        'sfswitch': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'dcs-sftoolkit': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}



