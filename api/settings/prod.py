# coding: utf-8
from .basic import *

ENV_MODE = 'prod'
DEBUG = False
WSGI_APPLICATION = 'settings.wsgi.application'

ALLOWED_HOSTS = ['@SERVER_HOST@']  # 部署时替换

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '172.18.0.1',
        'NAME': 'content',
        'USER': 'root',
        'PASSWORD': '@MYSQL_PASSWORD@'  # 部署时替换
    }
}

STATIC_URL = 'http://content-justworld-1259680493.cos.ap-shanghai.myqcloud.com/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

ADMIN_PATH = '@ADMIN_PATH@'  # 部署时替换
