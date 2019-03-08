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

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'dev.sqlite3'),
#         'Options': {
#             'timeout': 20,
#         }
#     },
# }

# DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'my_site',
    #     'USER': 'master_username',
    #     'PASSWORD': get_env_variable('MY_SITE_DATABASE_PASSWORD'),
    #     'HOST': get_env_variable('MY_SITE_ENDPOINT'),
    #     'PORT': '3306',
    #     'OPTIONS': {
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    #         'isolation_level': 'read committed',
    #     },
    #     'TEST': {
    #         'NAME': 'my_site_test_database',
    #     }
    # }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'my_site',
        'USER': 'walker',
        'PASSWORD': 'Lapt0p.Pa55w0rd',
        'HOST': '',
        'PORT': '',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
#     '../static/',
# ]
