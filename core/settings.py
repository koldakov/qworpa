"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

from django.contrib.messages import constants as messages
import environ

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

PROJECT_NAME = 'qworpa'

ENV = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV.get_value('QW_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV.get_value('QW_DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ENV.get_value('QW_ALLOWED_HOSTS', cast=list)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',
    'corsheaders',
    'rest_framework',
    'accounts',
    'api',
    'authentications',
    'blogs',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': ENV.get_value('BF_PSQL_NAME', default=PROJECT_NAME),
        'USER': ENV.get_value('BF_PSQL_USER', default=PROJECT_NAME),
        'PASSWORD': ENV.get_value('BF_PSQL_PASSWORD'),
        'HOST': ENV.get_value('BF_PSQL_HOST'),
        'PORT': ENV.get_value('BF_PSQL_PORT', default='5432'),
    },
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
STATIC_ROOT = BASE_DIR / 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

##################
# RECAPTCHA #
##################

RECAPTCHA_PUBLIC_KEY = ENV.get_value('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = ENV.get_value('RECAPTCHA_PRIVATE_KEY')

##################
# AUTHENTICATION #
##################
AUTH_USER_MODEL = 'accounts.User'

LOGIN_REDIRECT_URL = '/sign-in/'

AUTHENTICATION_BACKENDS = [
    'authentications.backends.AuthenticationBackend',
]

JWT_AUTH_KEY = ENV.get_value('QW_JWT_AUTH_KEY')

CORS_ALLOWED_ORIGINS = ENV.get_value('QW_CORS_ALLOWED_ORIGINS', cast=list)

if DEBUG is False:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

PROJECT_URL = ENV.get_value('QW_PROJECT_URL')

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = ENV.get_value('DEFAULT_FROM_EMAIL')

EMAIL_HOST_USER = ENV.get_value('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = ENV.get_value('EMAIL_HOST_PASSWORD')

EMAIL_HOST = ENV.get_value('EMAIL_HOST')

EMAIL_PORT = ENV.get_value('EMAIL_PORT', cast=int, default=587)

EMAIL_USE_TLS = True

LANGUAGES = (
    ('en', 'English'),
)

TINYMCE_API_KEY = ENV.get_value('TINYMCE_API_KEY')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s | %(name)s | %(levelname)s | %(funcName)s:%(lineno)s | %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'ui': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
