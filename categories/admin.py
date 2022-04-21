from simple_history.admin import SimpleHistoryAdmin
from django.contrib import admin
from . models import Category


@admin.register(Category)
class CategoryAdmin(SimpleHistoryAdmin):
    icon_name = 'ballot'
    search_fields = ('name',)
