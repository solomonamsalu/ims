from django.contrib import admin

from core.models import Company, Address


class CompanyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Company._meta.fields]
class AddressAdmin(admin.ModelAdmin):
    list_display=[field.name for field in  Address._meta.fields]
    
admin.site.register(Company,CompanyAdmin)
admin.site.register(Address,AddressAdmin)
