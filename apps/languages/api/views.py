from rest_framework import viewsets

from apps.languages.models import Language
from apps.languages.api.serializers import LanguageSerializer

from netflix_clone.permissions import IsAdminOrReadOnly, IsAuthenticatedOrReadOnly


class LanguageViewSet(viewsets.ModelViewSet):
    # Access permissions for administrators or authenticated users
    permission_classes = [IsAdminOrReadOnly | IsAuthenticatedOrReadOnly]
    # Get all languages
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    # For searches instead of ID the "slug" field is used
    lookup_field = 'slug'