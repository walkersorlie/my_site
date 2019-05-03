from django.urls import include, path
from . import views
import django.http


app_name = 'registration'

urlpatterns = [

    # /registration/account/
    path('account/', views.DetailView.as_view(), name='view-account'),
]
