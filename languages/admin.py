from django.contrib import admin
from . models import Language


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    icon_name = 'language'
    search_fields = ('name',)
