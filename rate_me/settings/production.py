from rate_me.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [
    '*',
    ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rate_my_realtor_mysql_aws',
        'USER': 'rate_my_realtor',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../rate_me/static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
