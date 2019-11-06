"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views


urlpatterns = [
    # /
    path('', include('homepage.urls')),

    # /registration/
    path('registration/', include('django.contrib.auth.urls')),
    path('registration/', include('registration.urls')),
    path('login/', RedirectView.as_view(pattern_name='login', permanent=True)),


    # /blog/
    path('blog/', include('blog.urls')),

    # /admin/
    path('admin/', admin.site.urls),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        # /api/
        path('api/', include('api.urls')),
        path('__debug__/', include(debug_toolbar.urls)),
    ]
