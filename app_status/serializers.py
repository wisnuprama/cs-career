from rest_framework import serializers
from .models import Status
import app_auth.serializers as auth_serializers


class StatuUserSerializer(auth_serializers.UserSerializer):

    class Meta:
        model = auth_serializers.User
        fields = ('username', 'first_name')


class StatusSerializer(serializers.ModelSerializer):

    user = StatuUserSerializer(read_only=True)

    class Meta:
        model = Status
        fields = ('id', 'user', 'content', 'created_at')
        extra_kwargs = {
            'id': {'read_only': True}
        }
