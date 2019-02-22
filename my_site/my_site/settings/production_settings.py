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

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

MY_APPS = [
    'blog.apps.BlogConfig',
    'homepage.apps.HomepageConfig',
    'registration.apps.RegistrationConfig',
    'widget_tweaks',
]


INSTALLED_APPS += MY_APPS


"""
Will need to change this. Add EMAIL_BACKEND
"""
# https://simpleisbetterthancomplex.com/tutorial/2016/09/19/how-to-create-password-reset-view.html
# EMAIL_BACKEND =


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "production_static")

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
#     '../static/',
# ]
