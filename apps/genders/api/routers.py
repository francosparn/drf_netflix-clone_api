from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.genders.api.views import GenderModelViewSet

router_genders = DefaultRouter()

router_genders.register(r'genders', GenderModelViewSet)

urlpatterns = [
    path('', include(router_genders.urls))
]