"""
Django settings for chatbot project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l!_i_ksb1gr0w__npz4dy7a&+7p*lgwr*r66i&p49fogitj!p)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['image-recognition-chatbot-t44m.onrender.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
]

AUTHENTICATION_BACKENDS = [
    
    'allauth.account.auth_backends.AuthenticationBackend', 
]
AUTH_USER_MODEL =  "user.CustomUser"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware", 
]


ROOT_URLCONF = 'chatbot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'chatbot.wsgi.application'
#Social login settings

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id':'',
            'secret': '',
          
        },
        'SCOPE': ['profile','email',],
         'AUTH_PARAMS': {'access_type': 'online'},
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': True,
    },
    'github': {
        'APP': {
            'client_id': '',
            'secret': '',
           
        }
    }
   
}

SOCIALACCOUNT_LOGIN_ON_GET=True
LOGIN_REDIRECT_URL = 'success'
LOGIN_URL = 'login'
SOCIALACCOUNT_AUTO_SIGNUP = True

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

import os
import dj_database_url


DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://image_recognition_db_itl9_user:PXDi1Z4jlHXDaVvNyyhfegCKYTVgslau@dpg-cu4vlihu0jms73fcf570-a.oregon-postgres.render.com/image_recognition_db_itl9',
        conn_max_age=600,
        ssl_require=True
    )
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

WEBHOOK_ENDPOINT_SECRET = ''
STRIPE_API_KEY = ''
DOMAIN = 'http://localhost:8000'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Directory where collected static files will be stored
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',  # 'danger' corresponds to Bootstrap's alert-danger
}
