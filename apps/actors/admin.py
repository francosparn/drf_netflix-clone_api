from django.contrib import admin

from apps.actors.models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    list_display_links = ['full_name']
    list_per_page = 10
    # Order alphabetically
    ordering = ('full_name',)

