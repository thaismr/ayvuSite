from .base import *

# DEBUG TOOLBAR AND WINDOWS DEVELOPMENT: JS MIME TYPE
import mimetypes
mimetypes.add_type("application/javascript", ".js", True)

SECRET_KEY = 'V87bt8&8twvt85sce!c-mie%#99V^VRB#B!@#59n@9+@1v0oel&+nwlUM+w4779'

DEBUG = True
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['http://localhost:3000']

# Django debug toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

LOCAL_APPS = [
    'debug_toolbar',
]

INSTALLED_APPS += LOCAL_APPS


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db2.sqlite3',
    }
}
