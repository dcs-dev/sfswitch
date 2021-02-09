"""
WSGI config for sfswitch project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sfswitch.settings")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")


from django.core.wsgi import get_wsgi_application
##from whitenoise.django import DjangoWhiteNoise
from whitenoise import WhiteNoise
application = get_wsgi_application()
application  = WhiteNoise(application, 'static')
#application.add_files('sfswitch/static/images')
