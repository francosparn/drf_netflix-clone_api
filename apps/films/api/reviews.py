from django.db import models
from django.db.models import Avg


class Review(models.Model):
    # Field to give a rating from 1 to the films
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    
    rating = models.IntegerField(choices=RATING_CHOICES)
    film = models.ForeignKey('films.Film', on_delete=models.CASCADE, related_name='reviews_films')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='reviews_films')
    
    class Meta:
        verbose_name_plural = 'Reviews'
        # Set the film and user fields as unique so that they are not repeated in the database
        unique_together = ('film', 'user')
    
    # Method to save a review
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Calculates the average rating of all reviews related to the film and updates the film average
        self.film.average_rating = self.film.reviews_films.aggregate(avg_rating=Avg('rating'))['avg_rating']
        self.film.save()