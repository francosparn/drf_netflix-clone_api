from django.db import models


class Gender(models.Model):
    name = models.SlugField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.name
