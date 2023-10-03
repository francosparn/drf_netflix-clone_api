from django.contrib import admin
from apps.genders.models import Gender


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    ordering = ('name',) 
