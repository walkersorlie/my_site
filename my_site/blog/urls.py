from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # /blog/
    path('', views.IndexView.as_view(), name='index'),

    # /blog/create_post/
    path('create_post/', views.create_post, name='create-post'),

    # /blog/edit_post/
    path('<slug:slug>/edit_post', views.edit_post, name='edit-post'),
    
    # /blog/slug/
    path('<slug:slug>/', views.DetailView.as_view(), name='view-post'),
]
