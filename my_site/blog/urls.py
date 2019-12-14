from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [

    # /blog/
    path('', views.IndexView.as_view(), name='index'),

    # /blog/create_post/
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),

    # /blog/<slug>/edit_post/
    path('<slug:slug>/edit_post/', views.EditPostView.as_view(), name='edit_post'),

    # /blog/<slug>/delete_post/
    path('<slug:slug>/delete_post', views.DeletePostView.as_view(), name='delete_post'),

    # /blog/slug/
    path('<slug:slug>/', views.DetailView.as_view(), name='view_post'),
]
