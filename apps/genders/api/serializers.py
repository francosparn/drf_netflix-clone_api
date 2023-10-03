from rest_framework import serializers
from apps.genders.models import Gender

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['id', 'name', 'slug']