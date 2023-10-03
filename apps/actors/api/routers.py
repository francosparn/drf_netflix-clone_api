from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.actors.api.views import ActorModelViewSet

router_actors = DefaultRouter()

router_actors.register(r'actors', ActorModelViewSet)

urlpatterns = [
    path('', include(router_actors.urls))
]