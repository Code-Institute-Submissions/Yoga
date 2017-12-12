from settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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