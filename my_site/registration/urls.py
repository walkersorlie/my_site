from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views

"""
# app_name = 'registration'
urlpatterns = [
    # https://docs.djangoproject.com/en/2.1/topics/auth/default/#using-the-views

    # /registration/login/
    path('login/', auth_views.LoginView.as_view(), name='login'),

    # /registration/logout/
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),

    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # re_path(r'^reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/MQ/set-password', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
"""
