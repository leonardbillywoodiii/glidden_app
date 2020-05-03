from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from cms import models
from django.utils.translation import gettext


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'last_name', 'first_name']
    fieldsets = (
        (None, {
            'fields': (
                'email', 'password',
            ),
        }),
        (gettext('Personal Info'), {
            'fields': (
                'first_name', 'last_name', 'birthday', 'sex',
            ),
        }),
        (gettext('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
            ),
        }),
        (gettext('Important Dates'), {
            'fields': (
                'last_login',
            ),
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': (
                'email', 'password',
            ),
        }),
        (gettext('Personal Info'), {
            'fields': (
                'first_name', 'last_name', 'birthday', 'sex',
            ),
        }),
    )


admin.site.register(models.UserProfile, UserAdmin)
