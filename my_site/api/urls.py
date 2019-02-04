from django.urls import include, path
from rest_framework import routers
from django.contrib.auth.models import User
from blog.models import Post
from api import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.BlogPostViewSet)
router.register(r'repos', views.RepoViewSet)

# app_name = 'api'
urlpatterns = router.urls
