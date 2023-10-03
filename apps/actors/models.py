from django.db import models


class Actor(models.Model):
    full_name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=120, unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.full_name
