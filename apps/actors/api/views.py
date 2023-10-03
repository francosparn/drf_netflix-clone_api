from rest_framework import viewsets

from apps.actors.models import Actor
from apps.actors.api.serializers import ActorSerializer

from netflix_clone.permissions import IsAdminOrReadOnly, IsAuthenticatedOrReadOnly


class ActorModelViewSet(viewsets.ModelViewSet):
    # Access permissions for administrators or authenticated users
    permission_classes = [IsAdminOrReadOnly, IsAuthenticatedOrReadOnly]
    # Get all actors
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    # For searches instead of ID the "slug" field is used 
    lookup_field = 'slug'