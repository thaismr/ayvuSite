from rest_framework import serializers
from .models import BlogPost
from ayvuSite.users.serializers import UserSerializer


# Serializers define the API representation.
class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = ['url', 'title', 'slug', 'author', 'summary', 'content']
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
