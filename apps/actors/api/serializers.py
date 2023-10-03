from rest_framework import serializers

from apps.actors.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'full_name', 'slug']