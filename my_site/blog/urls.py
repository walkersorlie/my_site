from django.urls import path

from . import views

urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    path('<str:slug>/', views.view_post, name='view_post'),
]
