from .base import *

secrets = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))

DEBUG = True

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'config.wsgi.dev.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


INSTALLED_APPS += [
    'storages',
]

#DB
DATABASES = secrets['DATABASES']
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

DEFAULT_FILE_STORAGES = 'config.storages.S3DefaultStorage'
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']
