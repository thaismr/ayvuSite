from django.contrib import admin
from . models import Language


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    search_fields = ('name',)
