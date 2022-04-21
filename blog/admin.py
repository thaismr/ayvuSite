from simple_history.admin import SimpleHistoryAdmin
from django.contrib import admin
from . models import BlogPost


# @admin.register(BlogPost)
class BlogPostAdmin(SimpleHistoryAdmin):
    icon_name = 'description'
    history_list_display = ['status']

    list_display = ('title', 'category', 'created_date', 'published_status')
    list_editable = ('category', 'published_status')
    list_filter = ('category', 'created_date', 'published_status')
    search_fields = ('title',)
    autocomplete_fields = ('author', 'translated_from', 'language', 'category',)


admin.site.register(BlogPost, BlogPostAdmin)
