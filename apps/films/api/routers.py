from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.films.api.views import FilmViewSet, FavoriteFilmViewSet, ReviewViewSet

router_films = DefaultRouter()

router_films.register(r'films', FilmViewSet, basename="films")
router_films.register(r'favorites-films', FavoriteFilmViewSet, basename="favorites-films")
router_films.register(r'reviews-films', ReviewViewSet, basename="reviews-films")

urlpatterns = [
    path('', include(router_films.urls)),
]