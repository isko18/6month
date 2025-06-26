from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.users.models import CustomUser
from django.utils.translation import gettext_lazy as _


@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('email', 'full_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    ordering = ('email',)
    search_fields = ('email', 'full_name')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Личная информация'), {'fields': ('full_name',)}),
        (_('Права доступа'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Важные даты'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )
