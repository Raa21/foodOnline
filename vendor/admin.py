from django.contrib import admin
from .models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'vendor_name', 'is_approved', 'created_at')
    list_display_links = ('vendor_name','user')
    ordering = ('-created_at',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.
admin.site.register(Vendor, VendorAdmin)