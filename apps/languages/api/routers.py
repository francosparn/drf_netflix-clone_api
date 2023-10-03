from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.languages.api.views import LanguageViewSet

router_languages = DefaultRouter()

router_languages.register(r'languages', LanguageViewSet)

urlpatterns = [
    path('', include(router_languages.urls)),
]