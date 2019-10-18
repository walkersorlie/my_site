import os
from .base_settings import *


DEBUG = False

SECURE_CONTENT_TYPE_NOSNIFF = False

SECURE_BROWSER_XSS_FILTER = True

# SESSION_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'SAMEORIGIN'


MY_APPS = [
    'blog.apps.BlogConfig',
    'homepage.apps.HomepageConfig',
    'registration.apps.RegistrationConfig',
    'widget_tweaks',
]


INSTALLED_APPS += MY_APPS


# https://simpleisbetterthancomplex.com/tutorial/2016/09/19/how-to-create-password-reset-view.html
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'walkersorlie@gmail.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_APP_PASSWORD']
EMAIL_USE_TLS = True


django_heroku.settings(locals(), db_colors=True, test_runner=False, logging=False)


"""
For local development, need this:
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
and whenever changes made in any static file, need to run collectstatic:
heroku local:run python my_site/manage.py collectstatic
"""
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

ALLOWED_HOSTS += ['127.0.0.1', 'localhost']
ADMINS = [('Walker', 'walkersorlie@gmail.com')]


# https://docs.djangoproject.com/en/2.2/topics/logging/#django.utils.log.RequireDebugFalse
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {lineno} {pathname} {funcname} {message}',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
