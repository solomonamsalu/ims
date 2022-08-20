from django.contrib import admin


from .models import Stock

class StockAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'id', 'quantity', 'reorder_level', 'is_active']

admin.site.register(Stock, StockAdmin)