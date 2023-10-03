from django.db import models

from apps.actors.models import Actor
from apps.genders.models import Gender
from apps.languages.models import Language
from apps.users.models import User


class Film(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    average_rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    release = models.PositiveIntegerField(blank=True, null=True)
    languages = models.ManyToManyField(Language, related_name='films', blank=True)
    actors = models.ManyToManyField(Actor, related_name='films_actor', blank=True)
    genders = models.ManyToManyField(Gender, related_name='films', blank=True)
    image = models.ImageField(upload_to='films', blank=True, null=True)
    link = models.URLField(unique=True)
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title
    

class FavoriteFilm(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='favorite_films')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_films')
    
    class Meta:
        verbose_name_plural = 'Favorites Films'
        
    def __str__(self):
        return self.film