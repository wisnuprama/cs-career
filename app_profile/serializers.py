from rest_framework import serializers
from .models import Expertise


class ExpertiseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expertise
        fields = ('expertise', 'level')
