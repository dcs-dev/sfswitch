import os
import sys
import logging.config
from celery import signals
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse
    

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = 'test'

##BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)
# DEBUG = False
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
    'sfswitch',
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

# Add in request context processor
# from django.conf import global_settings
#TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
#    'django.template.context_processors.request',
#)

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

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['PG_DB_NAME'],
        'USER': os.environ['PG_USERNAME'],
        'PASSWORD': os.environ['PG_PASSWORD'],
        'HOST': os.environ['PG_HOST'],
        'PORT': os.environ['PG_PORT'],
    }
}

# Celery settings
BROKER_POOL_LIMIT = 1
BROKER_URL = os.environ['BROKER_URL']
CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']
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
#STATIC_ROOT = 'static'
#STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

#TODO: These might be able to be removed. Check later.
STATIC_TMP = os.path.join(BASE_DIR, 'static')
os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



DJANGO_APP_DOMAIN = os.environ['DJANGO_APP_DOMAIN']

# OAuth configuration for Web app
SALESFORCE_REDIRECT_URI = 'https://' + DJANGO_APP_DOMAIN + '/oauth_response'
SALESFORCE_API_VERSION = os.environ['SALESFORCE_API_VERSION']
SALESFORCE_CONSUMER_KEY = os.environ['SALESFORCE_CONSUMER_KEY']
SALESFORCE_CONSUMER_SECRET = os.environ['SALESFORCE_CONSUMER_SECRET']


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
 
## Celery Logging Setup
@signals.setup_logging.connect
def on_celery_setup_logging(**kwargs):
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(asctime)s %(process)d/%(thread)d %(name)s %(funcName)s %(lineno)s %(levelname)s %(message)s',
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
            'celery': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
                'stream':sys.stdout
            }
        },
        'loggers': {
            'celery': {
                'handlers': ['celery'],
                'level': 'DEBUG',
                'propagate': False
            },
            'dcs-sftoolkit': {
                'handlers': ['celery'],
                'level': 'DEBUG',
            },
        },
    }

    logging.config.dictConfig(config)
