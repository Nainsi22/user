from django.contrib import admin
from user_management.user_management.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'role')
    list_filter = ('role', 'created_at')
