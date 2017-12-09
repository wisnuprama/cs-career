from .models import Friendship
from app_auth.serializers import UserSerializer
from rest_framework import serializers


class FriendshipSerializer(serializers.ModelSerializer):

    user1 = UserSerializer(read_only=True)
    user2 = UserSerializer(read_only=True)

    class Meta:
        model = Friendship
        fields = ('user1', 'user2', 'created_at')
