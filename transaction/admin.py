from django.contrib import admin


from .models import PurchaseOrder

class PurchaseOrderAdmin(admin.ModelAdmin):
    
    list_display = [field.name for field in PurchaseOrder._meta.fields]
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)