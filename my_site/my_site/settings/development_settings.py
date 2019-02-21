import os
from django.core.exceptions import ImproperlyConfigured
from .base_settings import *


def get_env_variable(name):
  """
  Gets the environment variable or throws ImproperlyConfigured exception
  """

  try:
    return os.environ[name]

  except KeyError:
      raise ImproperlyConfigured('Environment variable "%s" not found.' % name)

SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')


ALLOWED_HOSTS = []

# Will need to change this
# https://simpleisbetterthancomplex.com/tutorial/2016/09/19/how-to-create-password-reset-view.html
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
#     '../static/',
# ]
