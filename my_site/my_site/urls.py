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
from registration.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [

    # /
    path('', include('homepage.urls')),

    # /blog/
    path('blog/', include('blog.urls')),

    # /login/
    path('login/', RedirectView.as_view(pattern_name='login', permanent=True)),

    # /my_cv/
    path('my_cv/', include('my_cv.urls')),

    # /registration/
    path('registration/', include('django.contrib.auth.urls')),
    path('registration/', include('registration.urls')),

    # /repositories/
    path('repositories/', include('repositories.urls')),

    # /admin/
    path('admin/', include([
        # path('password_reset/', PasswordResetView.as_view(), name='admin_password_reset'),
        path('password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
        path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='admin_password_reset_confirm'),
        path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='admin_password_reset_complete'),
        # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='admin_password_reset_confirm'),
        # path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='admin_password_reset_complete'),
        path('', admin.site.urls),
    ])),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [

        # /api/
        path('api/', include('api.urls')),

        # /__debug__/
        path('__debug__/', include(debug_toolbar.urls)),
    ]

# handler404 = 'my_site.views.error_404'
# handler500 = 'my_site.views.error_500'
