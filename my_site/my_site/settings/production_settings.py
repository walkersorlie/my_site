import os
from django.core.exceptions import ImproperlyConfigured
from .base_settings import *


DEBUG = False

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

# SESSION_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'


MY_APPS = [
    'blog.apps.BlogConfig',
    'homepage.apps.HomepageConfig',
    'registration.apps.RegistrationConfig',
    'widget_tweaks',
]


INSTALLED_APPS += MY_APPS


# https://simpleisbetterthancomplex.com/tutorial/2016/09/19/how-to-create-password-reset-view.html
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_HOST_USER= 'walkersorlie@gmail.com'
EMAIL_HOST_PASSWORD= os.environ['EMAIL_APP_PASSWORD']
EMAIL_USE_TLS= True
EMAIL_PORT= 587

django_heroku.settings(locals(), db_colors=True, test_runner=False)

"""
For local development, need this:
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
and whenever changes made in any static file, need to run collectstatic:
heroku local:run python my_site/manage.py collectstatic
"""

STATICFILES_STORAGE = ''
# STATICFILES_STORAGE = 'my_site.storage.ManifestStaticFilesStorage'

ALLOWED_HOSTS += ['127.0.0.1', 'localhost']


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
