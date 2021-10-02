from django.contrib import admin
from . models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    icon_name = 'description'
    list_display = ('title', 'category', 'date_created', 'published_status')
    list_editable = ('category', 'published_status')
    list_filter = ('category', 'date_created', 'published_status')
    search_fields = ('title',)
    autocomplete_fields = ('author', 'translated_from', 'language', 'category',)
