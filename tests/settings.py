import os

ADMINS = (
    ('test@example.com', 'Mr. Test'),
)

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.normpath(os.path.join(BASE_PATH, 'media'))

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'tastypie.db'
TEST_DATABASE_NAME = ''

# for forwards compatibility
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.%s' % DATABASE_ENGINE,
        'NAME': DATABASE_NAME,
        'TEST_NAME': TEST_DATABASE_NAME,
    }
}


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'tastypie',
]

DEBUG = True
TEMPLATE_DEBUG = DEBUG
CACHE_BACKEND = 'locmem://'
SECRET_KEY = 'verysecret'

# weaker password hashing shoulod allow for faster tests
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.CryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'py.warnings': {
            'level': 'ERROR',# change to WARNING to show DeprecationWarnings, etc.
        },
    },
}

# to make sure timezones are handled correctly in Django>=1.4
USE_TZ = True
