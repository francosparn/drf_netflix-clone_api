from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.films.models import Film, FavoriteFilm
from apps.films.api.reviews import Review
from apps.films.api.serializers import FilmSerializer, FavoriteFilmSerializer, ReviewFilmSerializer

from netflix_clone.permissions import IsAdminOrReadOnly, IsAuthenticatedOrReadOnly


class FilmViewSet(viewsets.ModelViewSet):
    # Access permissions for administrators or authenticated users
    permission_classes = [IsAdminOrReadOnly | IsAuthenticatedOrReadOnly]
    serializer_class = FilmSerializer
    # Get all films
    queryset = Film.objects.all()
    # For searches instead of ID the "slug" field is used
    lookup_field = 'slug'


class FavoriteFilmViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteFilmSerializer
    # Get all your favorite films
    queryset = FavoriteFilm.objects.all()
    
    # Get user favorite films
    def get_queryset(self):
        return FavoriteFilm.objects.filter(user=self.request.user)
    
    # Save user favorite film
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewFilmSerializer

    def get_queryset(self):
        # Get all user reviews
        return Review.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Save review associated with the user who created it
        serializer.save(user=self.request.user)

    def has_object_permission(self, request, view, obj):
        # Check if the authenticated user is the owner of the review
        return obj.user == request.user