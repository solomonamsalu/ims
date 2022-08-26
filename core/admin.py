from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import Company, Address, User

class UserAdmin(BaseUserAdmin):
    pass
class CompanyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Company._meta.fields]
class AddressAdmin(admin.ModelAdmin):
    list_display=[field.name for field in  Address._meta.fields]
    
admin.site.register(Company,CompanyAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(User, UserAdmin)