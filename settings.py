"""
Django settings for natural_api project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
# import environ
import os
import io
from storages.backends.s3boto3 import S3Boto3Storage
import djoser
from firebase_admin import initialize_app, credentials
from google.auth import load_credentials_from_file
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
import crontab

# loading variables from .env file
load_dotenv() 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'storages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'fcm_django',
    'django_crontab',

    'debug_toolbar',
    'teacher',
    'student',
    'school',
    'core'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

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

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Use django-environ to parse the connection string
# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql_psycopg2',
#          'NAME':'postgres',
#          'USER':'postgres',
#          'PASSWORD':'Pluem9988!',
#          'HOST':'bridgerdbforapi.cluster-custom-cbk2c84q29qh.ap-southeast-2.rds.amazonaws.com',
#          'PORT':'5432'
#      }
#     }

# DATABASES = {
#     'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'postgres',
#        'USER': 'postgres',
#        'PASSWORD': 'Pluem9988!',
#        'HOST': 'localhost',
#        'PORT': '5432',
#     }
# }


DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'railway',
       'HOST': 'monorail.proxy.rlwy.net',
       'USER': 'postgres',
       'PASSWORD': 'AyDEBNsgiiBOdoNURGIMeqnIEzaNAVdm',
       'PORT': '15052',
    }
}


# [END gaeflex_py_django_database_config]
# [END dbconfig]

# Use a in-memory sqlite3 database when testing in CI systems


SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}

DJOSER = {
    "LOGIN_FIELD": "email",
    'SERIALIZERS' : {
        'user_create': 'core.serializers.UserCreateSerializer',
        "user": "djoser.serializers.UserSerializer",
        "current_user": 'core.serializers.UserSerializer',
        "user_delete": "djoser.serializers.UserSerializer",    
        },
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=365*100),
}

AUTH_USER_MODEL = 'core.User'

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}



# STORAGE 

# Set the required AWS credentials
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = 'ap-southeast-2'  # e.g., us-east-1
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_FILE_OVERWRITE = False

# For serving static files directly from S3
# AWS_S3_URL_PROTOCOL = 'https'
# AWS_S3_USE_SSL = True
# AWS_S3_VERIFY = True

# Static and media file configuration
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_LOCATION = 'static'

class CustomFirebaseCredentials(credentials.ApplicationDefault):
    def __init__(self, account_file_path: str):
        super().__init__()
        self._account_file_path = account_file_path

    def _load_credential(self):
        if not self._g_credential:
            self._g_credential, self._project_id = load_credentials_from_file(self._account_file_path,
                                                                              scopes=credentials._scopes)
            
custom_credentials = CustomFirebaseCredentials(os.getenv("FIREBASE_JSON_PATH"))
FIREBASE_MESSAGING_APP = initialize_app(custom_credentials, name='messaging')

FCM_DJANGO_SETTINGS = {
     # an instance of firebase_admin.App to be used as default for all fcm-django requests
     # default: None (the default Firebase app)
    "DEFAULT_FIREBASE_APP": FIREBASE_MESSAGING_APP,
     # default: _('FCM Django')
    "APP_VERBOSE_NAME": "What ever name",
     # true if you want to have only one active device per registered user at a time
     # default: False
    "ONE_DEVICE_PER_USER": False,
     # devices to which notifications cannot be sent,
     # are deleted upon receiving error response from FCM
     # default: False
    "DELETE_INACTIVE_DEVICES": False,
}


CRONJOBS = [
    ('* * * * *', 'tasks.twenty_seconds'),
    # Add more cron jobs as needed
]