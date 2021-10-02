from django.contrib import admin
from . models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    icon_name = 'ballot'
    search_fields = ('name',)
