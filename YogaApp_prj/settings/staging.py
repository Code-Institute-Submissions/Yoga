from settings.base import *

import dj_database_url


DEBUG = False

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}


STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_1RYq3AmEgxhKZhs2f0mR4Je8')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_t2XoBGjOb64Wru0HdQFmFJlb')

SITE_URL = 'https://stream1-project.herokuapp.com'
ALLOWED_HOSTS.append('stream1-project.herokuapp.com')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
