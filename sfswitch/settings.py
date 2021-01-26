import os
import urlparse

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
    # ('Ben Edwards', 'ben@edwards.nz'),
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
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'sfswitch.urls'

WSGI_APPLICATION = 'sfswitch.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'sFt007k1t',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# Celery settings
BROKER_POOL_LIMIT = 1

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

#SALESFORCE_CONSUMER_KEY = os.environ['3MVG9ysJNY7CaIHnlveju4dkFeSJ.PpYyY.AZZPCG1KoJljzBHd1YP_89QLaxM9A43z8eD.TH3NBNFnM3PGvv']
#SALESFORCE_CONSUMER_SECRET = os.environ['1A9A2AB3FA44789E4342B673FF84F1047CDC225EE94F9025B81B59E9A0BCB0F0']
#SALESFORCE_REDIRECT_URI = os.environ['https://127.0.0.1']
#SALESFORCE_API_VERSION = int(os.environ['49.0'])

SALESFORCE_CONSUMER_KEY = '3MVG9ysJNY7CaIHnlveju4dkFeSJ.PpYyY.AZZPCG1KoJljzBHd1YP_89QLaxM9A43z8eD.TH3NBNFnM3PGvv'
SALESFORCE_CONSUMER_SECRET = '1A9A2AB3FA44789E4342B673FF84F1047CDC225EE94F9025B81B59E9A0BCB0F0'
SALESFORCE_REDIRECT_URI = 'https://fe3a9dc08996.ngrok.io'
SALESFORCE_API_VERSION = '49.0'
