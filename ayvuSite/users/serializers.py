from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()


# Serializers define the API representation.
class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['url', 'bio']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'user_profile', 'is_staff']
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }
