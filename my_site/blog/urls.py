from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # /blog/
    path('', views.IndexView.as_view(), name='index'),
    
    # /blog/slug/
    path('<slug:slug>/', views.DetailView.as_view(), name='view_post'),
]
