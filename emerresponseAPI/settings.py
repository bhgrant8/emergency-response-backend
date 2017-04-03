"""
Django settings for emerresponseAPI project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys
import requests
## imports sensitive settings from file. you need to create this as instructed in README
from . import project_config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = project_config.DJANGO_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.99.100', 'hacko-integration-658279555.us-west-2.elb.amazonaws.com']

AWS_LOAD_BALANCER = 'hacko-integration-658279555.us-west-2.elb.amazonaws.com'

ALLOWED_HOSTS.append(AWS_LOAD_BALANCER)

# Get the IPV4 address we're working with on AWS
# The Loadbalancer uses this ip address for healthchecks
EC2_PRIVATE_IP = None
try:
    EC2_PRIVATE_IP = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4', timeout=0.01).text
except requests.exceptions.RequestException:
    pass

if EC2_PRIVATE_IP:
    ALLOWED_HOSTS.append(EC2_PRIVATE_IP)


# Application definition
# if needing admin add: 'django.contrib.admin', to list

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django_nose',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework_swagger',
    'data.apps.DataConfig',
    'corsheaders',
    'crispy_forms',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'emerresponseAPI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'emerresponseAPI.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# uncomment geocoder if using endpoint
DATABASES = {
    'default': {
        'ENGINE': project_config.AWS['ENGINE'],
        'NAME': project_config.AWS['NAME'],
        'HOST': project_config.AWS['HOST'],
        'PORT': 5432,
        'USER': project_config.AWS['USER'],
        'PASSWORD': project_config.AWS['PASSWORD'],
    },
    # 'geocoder': {
    #     'ENGINE': 'django.contrib.gis.db.backends.postgis',
    #     'NAME': project_config.GEOCODE['NAME'],
    #     'HOST': project_config.GEOCODE['HOST'],
    #     'USER': project_config.GEOCODE['USER'],
    #     'PASSWORD': project_config.GEOCODE['PASSWORD'],
    #     'PORT': 5432,
    # },
}

if 'test' in sys.argv or 'test_coverage' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': project_config.AWS['ENGINE'],
            'NAME': project_config.AWS['NAME'],
            'HOST': project_config.AWS['HOST'],
            'PORT': 5432,
            'USER': project_config.AWS['USER'],
            'PASSWORD': project_config.AWS['PASSWORD'],
            'TEST': {
                    'NAME': 'fire',
                },
        }
    }

REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 50,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

SWAGGER_SETTINGS = {
    'VALIDATOR_URL': None
}



# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = "/emergency/static/"

# testing setup
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# auto includes these command line args that are run with nose
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=data',
    '--cover-html'
]

CORS_ORIGIN_ALLOW_ALL = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
