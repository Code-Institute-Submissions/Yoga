from YogaApp_prj.settings.base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_1RYq3AmEgxhKZhs2f0mR4Je8')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_t2XoBGjOb64Wru0HdQFmFJlb')

