from rest_framework import serializers
from .models import Status
import app_auth.serializers as auth_serializers


class StatusUserSerializer(auth_serializers.UserSerializer):

    class Meta:
        model = auth_serializers.User
        fields = ('username', 'first_name')


class StatusSerializer(serializers.ModelSerializer):

    user = StatusUserSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True, format='%b. %d, %Y, %H:%M')

    class Meta:
        model = Status
        fields = ('id', 'user', 'content', 'created_at')
        extra_kwargs = {
            'id': {'read_only': True}
        }
