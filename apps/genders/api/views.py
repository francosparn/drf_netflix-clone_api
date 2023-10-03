from rest_framework import viewsets

from apps.genders.models import Gender
from apps.genders.api.serializers import GenderSerializer

from netflix_clone.permissions import IsAdminOrReadOnly, IsAuthenticatedOrReadOnly


class GenderModelViewSet(viewsets.ModelViewSet):
    # Access permissions for administrators or authenticated users
    permission_classes = [IsAdminOrReadOnly | IsAuthenticatedOrReadOnly]
    # Get all genders
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    # For searches instead of ID the "slug" field is used 
    lookup_field = 'slug'