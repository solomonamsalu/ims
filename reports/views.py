from django.db.models.aggregates import Sum
from django.shortcuts import render
from django.views.generic import ListView
from inventory.models import Item
from purchase.models import PurchaseOrder
from sales.models import SalesOrder

# Create your views here.

class ListSalesByCustomerReportView(ListView):

    template_name = 'reports/sales_by_customer_list.html'
    def get_queryset(self):
        sales_by_customer = SalesOrder.objects.all().values(total_inventory=Sum('quantity'), total_price = Sum('rate'))
        return sales_by_customer
class ListSalesByItemReportView(ListView):

    template_name = 'reports/sales_by_item_list.html'
    queryset = SalesOrder.objects.all()

class ListPurchaseReportView(ListView):

    template_name = 'reports/purchase_list.html'
    queryset = PurchaseOrder.objects.all()

class ListItemReportView(ListView):

    template_name = 'reports/item_list.html'
    queryset = Item.objects.all()

