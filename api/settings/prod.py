# coding: utf-8
from .basic import *

ENV_MODE = 'prod'
DEBUG = False
WSGI_APPLICATION = 'settings.wsgi.application'

ALLOWED_HOSTS = ['.justworld.top']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'NAME': 'content',
        'USER': 'root',
        'PASSWORD': 'HelloWorld.1'
    }
}
