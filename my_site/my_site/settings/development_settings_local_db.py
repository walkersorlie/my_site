import os
from .base_settings import *


DEBUG = True

ALLOWED_HOSTS = []


STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


MY_APPS = [
    'blog.apps.BlogConfig',
    'debug_toolbar',
    'django_bootstrap_breadcrumbs',
    'el_pagination',
    'homepage.apps.HomepageConfig',
    'my_cv.apps.MyCVConfig',
    'registration.apps.RegistrationConfig',
    'repositories.apps.RepositoriesConfig',
    'rest_framework',
    'widget_tweaks',
]


EL_PAGINATION_PER_PAGE = 4


INSTALLED_APPS += MY_APPS

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}


MY_MIDDLWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

MIDDLEWARE += tuple(MY_MIDDLWARE)

# Will need to change this
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'walkersorlie@gmail.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_APP_PASSWORD']
EMAIL_USE_TLS = True

INTERNAL_IPS = [
    '127.0.0.1',
]


django_heroku.settings(locals(), db_colors=True, databases=False, test_runner=False)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'my_site_db',
        'USER': 'walker',
        'PASSWORD': os.environ['LOCAL_DATABASE_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '5432',
        'TEST': {
            'NAME': 'my_site_test_db',
        }
    }
}


'''
Could make a new user on remote database and give privileges to make databases (basically what I did locally, but just do it on remote db)
'''
# DATABASES['default']['TEST'] = {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'my_site_test_db',
#         'USER': 'walker',
#         'PASSWORD': os.environ['LOCAL_DATABASE_PASSWORD'],
#         'HOST': 'localhost',
#         'PORT': '5432',
# }


# print(DATABASES)
# print(DATABASES['default'])
# print(DATABASES['TEST'])
