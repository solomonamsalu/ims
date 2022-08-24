from django.contrib import admin

# Register your models here.
from .models import Address
class AddressAdmin(admin.ModelAdmin):
    list_display=[field.name for field in  Address._meta.fields]
admin.site.register(Address,AddressAdmin)