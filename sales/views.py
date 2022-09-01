
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from sales.forms import AddCustomerForm, AddSalesOrderForm
from sales.models import Customer, SalesOrder

@method_decorator(login_required, name='dispatch')
class SalesOrderListView(ListView):
   
    # specify the model for list view
    model = SalesOrder
    template_name = 'sales/sales_order_list.html'
    # queryset = Item.objects.all()
    context_object_name = 'object_list'
    
    def get_queryset(self):
        if self.request.user.company_owner:
            return SalesOrder.objects.filter(item__store__company= self.request.user.company)
        
        return SalesOrder.objects.filter()

class SalesOrderCreateView(CreateView):
    model = SalesOrder
    template_name = 'sales/sales_order_create.html'
    form_class = AddSalesOrderForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
        
    def post(self,request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.store = self.request.user.store
            obj.save()
            success_url = reverse('sales/sales_order-detail', kwargs={'pk': obj.id})
            return HttpResponseRedirect(success_url)
            
        return super().post(request, *args, **kwargs)
           
class SalesOrderDetailView(DetailView):
      model = SalesOrder
      template_name = 'sales/sales_order_detail.html'

class SalesOrderUpdateView(UpdateView):
    model = SalesOrder
    fields = '__all__'
    template_name: str = 'sales/sales_order_create.html'

class SalesOrderDeleteView(DeleteView):
    model = SalesOrder
    success_url = reverse_lazy('salesOrder-list')


# customer

@method_decorator(login_required, name='dispatch')
class CustomerListView(ListView):
   
    # specify the model for list view
    model = Customer
    template_name = 'sales/customer_list.html'
    # queryset = Item.objects.all()
    context_object_name = 'object_list'
    
    def get_queryset(self):
        if self.request.user.company_owner:
            return Customer.objects.filter(store= self.request.user.store)
        
        return Customer.objects.filter()

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'sales/customer_create.html'
    form_class = AddCustomerForm

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs
        
    def post(self,request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.store = self.request.user.store
            obj.save()
            success_url = reverse('customer-detail', kwargs={'pk': obj.id})
            return HttpResponseRedirect(success_url)
            
        return super().post(request, *args, **kwargs)
           
class CustomerDetailView(DetailView):
      model = Customer
      template_name = 'customer_detail.html'

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = '__all__'
    template_name: str = 'sales/customer_create.html'

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer-list')