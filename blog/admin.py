from django.contrib import admin
from . models import PostCategory, BlogPost


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'date_created', 'is_published')
    list_display_links = ('id', 'title')
    list_editable = ('category', 'is_published')
    list_filter = ('category', 'date_created', 'is_published')
    list_per_page = 30
    search_fields = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_per_page = 30
    search_fields = ('name',)


# Register your models here.
admin.site.register(PostCategory, CategoryAdmin)
admin.site.register(BlogPost, PostAdmin)

