from django.contrib import admin
from purchase.models import PurchaseOrder,PurchaseOrderedItem
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display=[field.name for field in PurchaseOrder._meta.fields]
class PurchaseOrderedItemAdmin(admin.ModelAdmin):
    list_display=[field.name for field in PurchaseOrderedItem._meta.fields]
admin.site.register(PurchaseOrder,PurchaseOrderAdmin)
admin.site.register(PurchaseOrderedItem,PurchaseOrderedItemAdmin)

