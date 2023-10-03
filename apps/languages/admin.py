from django.contrib import admin

from apps.languages.models import Language

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    ordering = ('name',)

