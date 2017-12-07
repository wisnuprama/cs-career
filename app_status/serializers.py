from rest_framework import serializers
from .models import Status
from app_auth.seriealizers import UserSerializer


class StatusSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Status
        fields = ('id', 'user', 'content', 'created_at')
        extra_kwargs = {
            'id': {'read_only': True}
        }
