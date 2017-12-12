from rest_framework import serializers
from .models import User
from app_profile.serializers import ExpertiseSerializer


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True, source='get_full_name')
    expertise = ExpertiseSerializer(read_only=True, many=True, source='user.expert')

    class Meta:
        model = User
        fields = ('npm', 'username', 'full_name', 'email', 'role', 'angkatan',
                  'token_linkedin', 'link_linkedin', 'expertise', 'lastseen_at')
