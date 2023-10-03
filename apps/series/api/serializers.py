from rest_framework import serializers

from apps.series.models import Serie, FavoriteSerie
from apps.series.api.reviews import Review
from apps.actors.models import Actor
from apps.genders.models import Gender
from apps.languages.models import Language


class SerieSerializer(serializers.ModelSerializer):
    # Show text type values instead of ID
    actors = serializers.SlugRelatedField(many=True, queryset=Actor.objects.all(), slug_field='full_name')
    genders = serializers.SlugRelatedField(many=True, queryset=Gender.objects.all(), slug_field='name')
    languages = serializers.SlugRelatedField(many=True, queryset = Language.objects.all(), slug_field='name')
    
    class Meta:
        model = Serie
        fields = ['id', 'title', 'description', 'slug', 'season', 'chapter', 'average_rating', 'release', 'languages', 'actors', 'genders', 'image', 'link']
        

class FavoriteSerieSerializer(serializers.ModelSerializer):
    # Show value as text string instead of ID
    serie_name = serializers.StringRelatedField(source='serie.title', read_only=True)

    class Meta:
        model = FavoriteSerie
        fields = ['id', 'serie', 'serie_name']


class ReviewSerieSerializer(serializers.ModelSerializer):
    # Show value as text string instead of ID
    serie_name = serializers.StringRelatedField(source='serie.title', read_only=True)
    
    class Meta:
        model = Review
        fields = ['rating', 'serie', 'serie_name']