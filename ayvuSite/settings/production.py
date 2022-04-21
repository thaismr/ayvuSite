# For production, check:
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
from .base import *
import django_heroku

DEBUG = False

INSTALLED_APPS = BASE_APPS

django_heroku.settings(locals())
