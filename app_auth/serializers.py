from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(read_only=True, source='get_full_name')

    class Meta:
        model = User
        fields = ('npm', 'username', 'full_name', 'email', 'role', 'angkatan')
