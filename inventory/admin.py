from django.contrib import admin

from .models import Item, Supplier

class ItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Item._meta.fields]
class SupplierAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Supplier._meta.fields]

admin.site.register(Item, ItemAdmin)
admin.site.register(Supplier,SupplierAdmin)