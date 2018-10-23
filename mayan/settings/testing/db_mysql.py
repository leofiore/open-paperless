from __future__ import unicode_literals
import os

from .base import *  # NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME', 'mayan_edms'),
        'USER': os.getenv('DATABASE_USER', 'root'),
        'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
        'PASSWORD': os.getenv('DATABASE_PASS', ''),
        'PORT': os.getenv('DATABASE_PORT', '3306'),
    }
}

BROKER_URL = os.getenv('REDIS_URL', 'redis://127.0.0.1:6379/0')
CELERY_RESULT_BACKEND = os.getenv('REDIS_URL', 'redis://127.0.0.1:6379/0')
