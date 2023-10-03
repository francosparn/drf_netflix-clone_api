from rest_framework import serializers

from apps.films.models import Film, FavoriteFilm
from apps.actors.models import Actor
from apps.genders.models import Gender
from apps.languages.models import Language
from apps.films.api.reviews import Review


class FilmSerializer(serializers.ModelSerializer):
    # Show text type values instead of ID
    actors = serializers.SlugRelatedField(many=True, queryset=Actor.objects.all(), slug_field='full_name')
    genders = serializers.SlugRelatedField(many=True, queryset=Gender.objects.all(), slug_field='name')
    languages = serializers.SlugRelatedField(many=True, queryset = Language.objects.all(), slug_field='name')

    class Meta:
        model = Film
        fields = ['id', 'title', 'description', 'slug', 'duration', 'average_rating', 'release', 'languages', 'actors', 'genders', 'image', 'link']
        

class FavoriteFilmSerializer(serializers.ModelSerializer):
    # Show value as text string instead of ID
    film_name = serializers.StringRelatedField(source='film.title', read_only=True)

    class Meta:
        model = FavoriteFilm
        fields = ['id', 'film', 'film_name']
        

class ReviewFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'rating', 'film']
    