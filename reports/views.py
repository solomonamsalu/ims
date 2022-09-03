from django.views.generic import ListView
from django.shortcuts import render
from inventory.models import Item
from sales.models import SalesOrder
from purchase.models import PurchaseOrder
# Create your views here.

class ListSalesReportView(ListView):

    template_name = 'reports/sales_list.html'
    queryset = SalesOrder.objects.all()

class ListPurchaseReportView(ListView):

    template_name = 'reports/purchase_list.html'
    queryset = PurchaseOrder.objects.all()

class ListItemReportView(ListView):

    template_name = 'reports/item_list.html'
    queryset = Item.objects.all()

