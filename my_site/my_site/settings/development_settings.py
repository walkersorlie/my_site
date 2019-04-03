import os
from .base_settings import *


DEBUG = True

ALLOWED_HOSTS = []

MY_APPS = [
    'blog.apps.BlogConfig',
    'debug_toolbar',
    'homepage.apps.HomepageConfig',
    'registration.apps.RegistrationConfig',
    'rest_framework',
    'widget_tweaks',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

INSTALLED_APPS += MY_APPS

MY_MIDDLWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

MIDDLEWARE += tuple(MY_MIDDLWARE)

# Will need to change this
# https://simpleisbetterthancomplex.com/tutorial/2016/09/19/how-to-create-password-reset-view.html
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only

INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'my_site',
        'USER': 'walker',
    }
}

django_heroku.settings(locals(), databases=False)
