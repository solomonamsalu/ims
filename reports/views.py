from django.contrib.auth.decorators import login_required
from django.db.models import OuterRef, Subquery
from django.db.models.aggregates import Sum
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from inventory.models import Item
from purchase.models import PurchaseOrder
from sales.models import SalesOrder


# Create your views here.
@method_decorator(login_required, name='dispatch')
class ListSalesByCustomerReportView(ListView):

    template_name = 'reports/sales_by_customer_list.html'
    def get_queryset(self):
        sales_by_customer = SalesOrder.objects.values('customer__first_name', 'customer__last_name').annotate(total_inventory=Sum('quantity'), total_price = Sum('amount'))
        object_list = sales_by_customer
        return object_list
@method_decorator(login_required, name='dispatch')
class ListSalesByItemReportView(ListView):

    template_name = 'reports/sales_by_item_list.html'
    def get_queryset(self):
        sales_by_customer = SalesOrder.objects.values('item__name', 'item__SKU_number').annotate(total_inventory=Sum('quantity'), total_price = Sum('amount'))
        object_list = sales_by_customer
        return object_list

@method_decorator(login_required, name='dispatch')
class InventorySummaryReportView(ListView):

    template_name = 'reports/inventory_summary.html'
    def get_queryset(self):
        newest = PurchaseOrder.objects.filter(item=OuterRef('pk')).order_by('-date')
        sales_by_customer = Item.objects.filter().annotate(quantity_in= Subquery(newest.values('quantity'))) # todo finish this.
            # .order_by('date').first().quantity), quantity_out = Sum('rate'))
        object_list = sales_by_customer
        return object_list
    # def get_context_data(self, **kwargs):

    #     data = super().get_context_data(**kwargs)
    #     data['page_title'] = 'Authors'
    #     return data


@method_decorator(login_required, name='dispatch')
class ListPurchaseReportView(ListView):

    template_name = 'reports/purchase_list.html'
    queryset = PurchaseOrder.objects.all()

@method_decorator(login_required, name='dispatch')
class ListItemReportView(ListView):

    template_name = 'reports/item_list.html'
    queryset = Item.objects.all()

@method_decorator(login_required, name='dispatch')
class ListPurchaseByItemReportView(ListView):

    template_name = 'reports/purchase_by_item_list.html'
    def get_queryset(self):
        purchase_by_item = PurchaseOrder.objects.values('item__name', 'item__SKU_number').annotate(total_inventory=Sum('quantity'), total_price = Sum('amount'))
        object_list = purchase_by_item
        return object_list
