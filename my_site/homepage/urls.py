from django.urls import path
from . import views

app_name = 'homepage'
urlpatterns = [

    # /
    path('', views.IndexView.as_view(), name='index'),

    # /github_payload/
    path('github_payload/', views.payload, name='github_payload'),

]
