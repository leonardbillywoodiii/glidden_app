from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from cms import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'last_name', 'first_name']


admin.site.register(models.UserProfile, UserAdmin)
