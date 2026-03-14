from django.contrib import admin
from .models import ServicePackage, Order


@admin.register(ServicePackage)
class ServicePackageAdmin(admin.ModelAdmin):
    """Admin configuration for ServicePackage model."""
    prepopulated_fields = {'slug': ('name',)}  # unique slug (human-readable) for URL
    list_display = ['name', 'price', 'is_active', 'order']
    list_editable = ['is_active', 'order']  # edit directly in list view


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin configuration for Order model."""
    list_display = ['name', 'email', 'package', 'created']
    readonly_fields = ['name', 'email', 'package', 'message', 'created']  # orders are read-only