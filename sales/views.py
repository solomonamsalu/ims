
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from sales.models import SalesOrder

@method_decorator(login_required, name='dispatch')
class SalesOrderListView(ListView):
   
    # specify the model for list view
    model = SalesOrder
    template_name = 'sales_order_list.html'
    # queryset = Item.objects.all()
    context_object_name = 'object_list'
    
    # def get_queryset(self):
    #     return SalesOrder.objects.filter(store= self.request.user.store)

class SalesOrderCreateView(CreateView):
    model = SalesOrder
    fields = '__all__'
    template_name = 'sales_order_create.html'

   
           
class SalesOrderDetailView(DetailView):
      model = SalesOrder
      template_name = 'sales_order_detail.html'

class SalesOrderUpdateView(UpdateView):
    model = SalesOrder
    fields = '__all__'
    template_name: str = 'sales_order_create.html'

class SalesOrderDeleteView(DeleteView):
    model = SalesOrder
    success_url = reverse_lazy('SalesOrder-list')

