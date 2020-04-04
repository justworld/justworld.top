# coding: utf-8
from .basic import *

ENV_MODE = 'prod'
DEBUG = False
WSGI_APPLICATION = 'settings.wsgi.application'

ALLOWED_HOSTS = ['@SERVER_HOST@']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '172.18.0.1',
        'NAME': 'content',
        'USER': 'root',
        'PASSWORD': '@MYSQL_PASSWORD@'
    }
}
