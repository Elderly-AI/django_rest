from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import CustomUser


class AccountAdmin(BaseUserAdmin):

    list_display = ('email', 'username', 'is_staff',  'is_superuser', 'is_active', 'user_type')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'is_active', 'password', 'user_type')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'is_active', 'password', 'user_type')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(CustomUser, AccountAdmin)
