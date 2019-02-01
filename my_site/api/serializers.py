from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'author_id', 'title', 'pub_date', 'slug')
