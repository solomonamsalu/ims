from django.contrib import admin

from .models import Item, Store, Supplier

class ItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Item._meta.fields]
class SupplierAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Supplier._meta.fields]

class StoreAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Store._meta.fields]
admin.site.register(Item, ItemAdmin)
admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Store,StoreAdmin)