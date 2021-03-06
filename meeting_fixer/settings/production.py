"""
Django settings for meeting_fixer project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

from .base import *


DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'HOST': db_host,
        'NAME': db_name,
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': db_user,
        'PASSWORD': db_pass,
    }
}

