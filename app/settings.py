"""
Django settings for app project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

ROXY_VERSION = "2.0.0"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SITE_ID = int(os.environ.get('MEMEX_SITE_ID', '1'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('MEMEX_SECRET_KEY', 'xpje7*g@ok-fj!9-(%2d=q86x31o5ehy%%q*8sktscosqp&p%k')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('MEMEX_DEBUG', 'True') == 'True')

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = os.environ.get('MEMEX_ALLOWED_HOSTS', '').split(',')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':   os.environ.get('MEMEX_DATABASES_DEFAULT_ENGINE', 'django.db.backends.mysql'),
        'NAME':     os.environ.get('MEMEX_DATABASES_DEFAULT_NAME', 'memex_app'),
        'USER':     os.environ.get('MEMEX_DATABASES_DEFAULT_USER', 'memex'),
        'PASSWORD': os.environ.get('MEMEX_DATABASES_DEFAULT_PASSWORD', ''),
        'HOST':     os.environ.get('MEMEX_DATABASES_DEFAULT_HOST', ''),
        'PORT':     os.environ.get('MEMEX_DATABASES_DEFAULT_PORT', ''),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL =  os.environ.get('MEMEX_STATIC_URL', '/static/')

TEMPLATE_DIRS = os.environ.get('MEMEX_TEMPLATE_DIRS', '').split(',')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
}

MEMEX_API_URL = os.environ.get('MEMEX_API_URL', '')
MEMEX_API_TOKEN = os.environ.get('MEMEX_API_TOKEN', '')

LOGIN_URL = os.environ.get('MEMEX_LOGIN_URL', 'auth_login')
