from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post
from homepage.models import Repository


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'author_id', 'title', 'pub_date', 'slug')

class RepoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Repository
        # fields = ('repo_name', 'description', 'pushed_at', 'url')
        fields = '__all__'
