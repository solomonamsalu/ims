from django.contrib.auth.decorators import login_required
from django.db.models import OuterRef, Subquery
from django.db.models.aggregates import Sum
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from inventory.models import Item
from purchase.models import PurchaseOrder
from sales.models import SalesOrder
from django.db.models import F, Func


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
        newest_purchases = PurchaseOrder.objects.filter(item=OuterRef('pk')).order_by('-date')
        newest_sales = SalesOrder.objects.filter(item=OuterRef('pk')).order_by('-date')
        if self.request.user.company_owner:
            
            sales_by_customer = Item.objects.filter(store__company = self.request.user.company).annotate(quantity_in= Subquery(newest_purchases.values('quantity')),\
                                                            quantity_out= Subquery(newest_sales.values('quantity'))) # TODO finish this.
        else:
            try:
                sales_by_customer = Item.objects.filter(store = self.request.user.store).annotate(quantity_in= Subquery(newest_purchases.values('quantity')),\
                                                            quantity_out= Subquery(newest_sales.values('quantity'))) # TODO finish this.
            except:
                sales_by_customer = Item.objects.none()
        object_list = sales_by_customer
        return object_list
    # def get_context_data(self, **kwargs):

    #     data = super().get_context_data(**kwargs)
    #     data['page_title'] = 'Authors'
    #     return data


@method_decorator(login_required, name='dispatch')
class ProductSalesOrderView(ListView):

    template_name = 'reports/product_sales_order.html'
    queryset = Item.objects.all()
    def get_queryset(self):
        if self.request.user.company_owner:
            sales_orders = SalesOrder.objects.filter(item=OuterRef('pk')).order_by().values('quantity').annotate(sum=Func(F('id'), function='Sum')).values('sum')
            # sales_price = SalesOrder.objects.filter(item=OuterRef('pk')).order_by().annotate(count=Func(F('id'), function='Count')).values('count')
            sales_by_item = Item.objects.filter(store__company = self.request.user.company).annotate(quantity_sold=Subquery(sales_orders))
        else:
            sales_orders = SalesOrder.objects.filter(item=OuterRef('pk')).order_by().annotate(count=Func(F('id'), function='Count')).values('count')
            sales_by_item = Item.objects.filter(store = self.request.user.store).annotate(quantity_sold=Subquery(sales_orders))

        
        object_list = sales_by_item
        return object_list

@method_decorator(login_required, name='dispatch')
class ListPurchaseByItemReportView(ListView):

    template_name = 'reports/purchase_by_item_list.html'
    def get_queryset(self):

        if self.request.user.company_owner:

            purchase_by_item = PurchaseOrder.objects.filter(item__store__company = self.request.user.company).values('item__name', 'item__SKU_number').annotate(total_inventory=Sum('quantity'), total_price = Sum('amount'))
        else:
            purchase_by_item = PurchaseOrder.objects.filter(item__store = self.request.user.store).values('item__name', 'item__SKU_number').annotate(total_inventory=Sum('quantity'), total_price = Sum('amount'))
        
        object_list = purchase_by_item
        return object_list
