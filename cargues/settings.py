"""
Django settings for strauss project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from django.urls import reverse

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7@&t*g#1ko*pj@lyxw^)#c8&48%8bod-)%59oogorcqy%7a^nr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['192.168.1.198']
#ALLOWED_HOSTS = ['localhost']
ALLOWED_HOSTS = ['poseidon.intelibpo.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.inicial',
    'app.cargueArchivos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cargues.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cargues.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'straussdb',
        'USER': 'intelibpo',
        'PASSWORD': '2r9qWsZ/<5?,Pkp/',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'OPTIONS': {
            'options': '-c search_path=strauss_asignaciones'
        }
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'straussdb',
#         'USER': 'intelibpo',
#         'PASSWORD': '2r9qWsZ/<5?,Pkp/',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#         'OPTIONS': {
#             'options': '-c search_path=strauss'
#         }
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'straussdb',
#         'USER': 'intelibpo',
#         'PASSWORD': '2r9qWsZ/<5?,Pkp/',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#         'OPTIONS': {
#             'options': '-c search_path=strauss_vincular'
#         }
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

STATIC_URL = '/static/'


MEDIA_URL = '/upload/'

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'upload')

#LOGIN_REDIRECT_URL = '/app/cargueArchivos/templates/archivos/index'
LOGIN_REDIRECT_URL = 'index'
