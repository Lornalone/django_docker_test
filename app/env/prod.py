from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_app_db',
        'USER': 'django_app_user',
        'PASSWORD': 'explosif',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}