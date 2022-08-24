from django.contrib import admin
from purchase.models import PurchaseOrder
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display=[field.name for field in PurchaseOrder._meta.fields]

admin.site.register(PurchaseOrder,PurchaseOrderAdmin)

