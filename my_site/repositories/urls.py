from django.urls import path
from . import views


app_name = 'repositories'
urlpatterns = [

    # /repositories/
    path('', views.IndexView.as_view(), name='index'),

    # /repositories/github_payload/
    path('github_payload/', views.payload, name='github_payload'),
]
