from django.contrib import admin
from sales.models import Customer,SalesOrder
class CustomerAdmin(admin.ModelAdmin):
    
    # list_display=['first_name', 'last_name', 'address', 'phone' ]
    list_display=[field.name for field in Customer._meta.fields]

    
class SalesOrderAdmin(admin.ModelAdmin):
    list_display=[field.name for field in SalesOrder._meta.fields]
admin.site.register(Customer,CustomerAdmin)
admin.site.register(SalesOrder,SalesOrderAdmin)