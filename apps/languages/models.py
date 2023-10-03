from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.name