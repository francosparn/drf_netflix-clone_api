from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.series.models import Serie, FavoriteSerie
from apps.series.api.reviews import Review
from apps.series.api.serializers import SerieSerializer, FavoriteSerieSerializer, ReviewSerieSerializer

from netflix_clone.permissions import IsAdminOrReadOnly, IsAuthenticatedOrReadOnly


class SerieViewSet(viewsets.ModelViewSet):
    # Access permissions for administrators or authenticated users
    permission_classes = [IsAdminOrReadOnly | IsAuthenticatedOrReadOnly]
    serializer_class = SerieSerializer
    # Get all series
    queryset = Serie.objects.all()
    # For searches instead of ID the "slug" field is used
    lookup_field = 'slug'
    

class FavoriteSerieViewSet(viewsets.ModelViewSet):
    # To access the view you must be authenticated
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteSerieSerializer
    # Get all series
    queryset = FavoriteSerie.objects.all()
    
    # Get user favorite series
    def get_queryset(self):
        return FavoriteSerie.objects.filter(user=self.request.user)
    
    # Save user favorite serie
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
class ReviewViewSet(viewsets.ModelViewSet):
    # To access the view you must be authenticated
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerieSerializer

    def get_queryset(self):
        # Get all user reviews
        return Review.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Save review associated with the user who created it
        serializer.save(user=self.request.user)

    def has_object_permission(self, request, view, obj):
        # Check if the authenticated user is the owner of the review
        return obj.user == request.user