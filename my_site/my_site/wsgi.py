"""
WSGI config for my_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

"""
IMPORTANT
Change the settigns file here to specify development or production

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings.development_settings')

"""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings.production_settings')

application = get_wsgi_application()
