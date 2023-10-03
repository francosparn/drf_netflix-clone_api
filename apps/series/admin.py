from django.contrib import admin
from apps.series.models import Serie, FavoriteSerie
from apps.series.api.reviews import Review


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ['title', 'season', 'chapter', 'average_rating', 'release', 'get_languages', 'get_actors', 'get_genders']
    list_display_links = ['title']
    list_filter = ['languages', 'genders']
    search_fields = ['title']
    list_per_page = 8
    
    # Optimizing DB queries
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('languages', 'actors', 'genders')
    
    # Get values from the Language model
    def get_languages(self, obj):
        return ', '.join([language.name for language in obj.languages.all()])
    
    get_languages.short_description = 'Languages'
    
    # Get values from the Actor model
    def get_actors(self, obj):
        return ', '.join([actor.full_name for actor in obj.actors.all()])
    
    get_actors.short_description = 'Main Actors'
    
    # Get values from the Gender model
    def get_genders(self, obj):
        return ', '.join([gender.name for gender in obj.genders.all()])
    
    get_genders.short_description = 'Genders'
    

@admin.register(FavoriteSerie)
class FavoriteSerieAdmin(admin.ModelAdmin):
    list_display = ['id', 'serie', 'user']
    list_display_links = ['serie']
    list_per_page = 10


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'serie', 'rating']
    list_display_links = ['user']
    list_per_page = 10