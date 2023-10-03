from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.series.api.views import SerieViewSet, FavoriteSerieViewSet, ReviewViewSet

router_series = DefaultRouter()

router_series.register(r'series', SerieViewSet, basename="series")
router_series.register(r'favorites-series', FavoriteSerieViewSet, basename="favorites-series")
router_series.register(r'reviews-series', ReviewViewSet, basename="reviews-series")

urlpatterns = [
   path('', include(router_series.urls)), 
]