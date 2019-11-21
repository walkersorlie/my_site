from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'registration'

urlpatterns = [

    # /registration/account/
    path('account/', views.DetailView.as_view(), name='view_account'),
]
