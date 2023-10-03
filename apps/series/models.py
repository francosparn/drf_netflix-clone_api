from django.db import models

from apps.languages.models import Language
from apps.actors.models import Actor
from apps.genders.models import Gender
from apps.users.models import User


class Serie(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    season = models.PositiveIntegerField(blank=True, null=True)
    chapter = models.PositiveIntegerField(blank=True, null=True)
    average_rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    release = models.PositiveIntegerField(blank=True, null=True)
    languages = models.ManyToManyField(Language, related_name='series', blank=True)
    actors = models.ManyToManyField(Actor, related_name='series_actor', blank=True)
    genders = models.ManyToManyField(Gender, related_name='series', blank=True)
    image = models.ImageField(upload_to='series', blank=True, null=True)
    link = models.URLField(unique=True)
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title
    

class FavoriteSerie(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='favorite_series')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_series')
    
    class Meta:
        verbose_name_plural = 'Favorites Series'
    
    def __str__(self):
        return self.serie