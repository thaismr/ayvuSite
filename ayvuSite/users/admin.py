from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile, ProxyUser

User = get_user_model()


class UserProfileInline(admin.TabularInline):
    model = UserProfile
    can_delete = False


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (("User", {"fields": ("is_premium",)}),) + tuple(
        BaseUserAdmin.fieldsets
    )
    list_display = BaseUserAdmin.list_display + ("is_premium",)


@admin.register(ProxyUser)
class ProxyUserAdmin(admin.ModelAdmin):
    icon_name = 'person'
    fields = (
        ('username', 'is_active',),
        ('first_name', 'last_name', 'email', 'is_premium'),
    )
    list_display = BaseUserAdmin.list_display + ("is_premium",)
    list_filter = ('is_staff', 'is_active', 'is_premium')
    readonly_fields = ('is_premium',)
    inlines = (UserProfileInline,)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    icon_name = 'person'
    autocomplete_fields = ('user',)
    list_display = ('user', 'bio', 'website',)
    list_filter = ('user__is_active', 'user__is_premium')
