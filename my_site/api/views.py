from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post
from rest_framework import viewsets
from .serializers import UserSerializer, BlogPostSerializer


# ViewSets define the view behavior.
class UserViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    login_url = '/registration/login/'

    queryset = User.objects.all()
    serializer_class = UserSerializer

class BlogPostViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    login_url = '/registration/login/'

    queryset = Post.objects.all().order_by('-pub_date')
    serializer_class = BlogPostSerializer
