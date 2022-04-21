"""
Django settings for ayvuSite project.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from django.contrib.messages import constants
from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
APPS_DIR = BASE_DIR / 'ayvuSite'


BASE_APPS = [
    # 'material',
    # 'material.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # Required by Debug toolbar
    'django.contrib.postgres',  # Postgres advanced functionality
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'simple_history',
]

PROJECT_APPS = [
    'ayvuSite.users.apps.UsersConfig',
    'languages.apps.LanguagesConfig',
    'categories.apps.CategoriesConfig',
    'pages.apps.PagesConfig',
    'blog.apps.BlogConfig',
    'base.apps.BaseConfig',
]

INSTALLED_APPS = BASE_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  #: On top after security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',  #: Django debug toolbar
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'ayvuSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
                #: Project libraries
                # 'sitefilters': 'ayvuSite.templatetags.sitefilters',
            }
        },
    },
]

WSGI_APPLICATION = 'ayvuSite.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# STATIC
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = BASE_DIR / 'staticfiles'
# http://whitenoise.evans.io/en/stable/django.html#instructions-for-amazon-cloudfront
STATIC_HOST = os.environ.get('DJANGO_CDN_HOST', '')
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = STATIC_HOST + '/static/'
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(APPS_DIR / 'static')]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
# Whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
# MEDIA_ROOT = str(BASE_DIR / 'media/')
MEDIA_ROOT = str(APPS_DIR / 'media/')
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'


# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"


# https://docs.djangoproject.com/en/3.2/releases/3.2/#customizing-type-of-auto-created-primary-keys
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SIMPLE_HISTORY_HISTORY_ID_USE_UUID = True
SIMPLE_HISTORY_DATE_INDEX = "Composite"
SIMPLE_HISTORY_HISTORY_CHANGE_REASON_USE_TEXT_FIELD = True
SIMPLE_HISTORY_FILEFIELD_TO_CHARFIELD = True


MESSAGE_TAGS = {
    constants.ERROR: 'red accent-3 red-text text-lighten-5',
    constants.WARNING: 'amber darken-4',
    constants.DEBUG: 'cyan accent-2',
    constants.SUCCESS: 'lime accent-3',
    constants.INFO: 'blue-grey',
}


# DJANGO REST FRAMEWORK
# ------------------------------------------------------------------------------
# https://www.django-rest-framework.org/
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # Use Django's standard `django.contrib.auth` permissions,
        # or allow read-only access for unauthenticated users.
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.IsAuthenticated'
    ],
}


# MATERIAL DESIGN ADMIN
# ------------------------------------------------------------------------------
# https://github.com/MaistrenkoAnton/django-material-admin

MATERIAL_ADMIN_SITE = {
    'HEADER': 'Ayvu Site Admin Area',  # Admin site header
    'TITLE': 'Ayvu Admin',  # Admin site titlein/logout pages (path to static should be specified)
    'SHOW_THEMES':  True,  # Show default admin themes button
    'TRAY_REVERSE': False,  # Hide object-tools and additional-submit-line by default
    'NAVBAR_REVERSE': False,  # Hide side navbar by default
    'SHOW_COUNTS': True,  # Show instances counts for each model
    'APP_ICONS': {
        # Set icons for applications(lowercase), including 3rd party apps,
        # {'application_name': 'material_icon_name', ...}
        'sites': 'send',
        'blog': 'description',
    },
    'MODEL_ICONS': {
        # Set icons for models(lowercase), including 3rd party models,
        # {'model_name': 'material_icon_name', ...}
        'site': 'contact_mail',
    }
}

# Development / Production server settings:
# if os.environ.get("CAPROVER") is None:
#     from .env.local_settings import *
# else:
#     from .env.settings_caprover import *

