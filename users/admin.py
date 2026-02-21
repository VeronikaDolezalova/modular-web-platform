from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile # user profile model


class ProfileInline(admin.StackedInline):
    """Profile displayed inline with User in admin."""
    model = Profile
    can_delete = False


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin configuration for Profile model."""
    list_display = ['user', 'gender', 'date_of_birth']


# Re-register User with Profile inline
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site._registry[User].inlines = [ProfileInline]