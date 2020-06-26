from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['tpbioinformatica.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8n2eegbi42sg0',
        'USER': 'wxnvmwiigwlguq',
        'PASSWORD': '1be340a2e4b24b2cdd77f0878c3d163cb0e323157c2842e878bd1cc1af1e9024',
        'HOST': 'ec2-52-72-65-76.compute-1.amazonaws.com' ,
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')
