
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from purchase.models import PurchaseOrder

@method_decorator(login_required, name='dispatch')
class PurchaseOrderistView(ListView):
   
    # specify the model for list view
    model = PurchaseOrder

    template_name = 'purchase/list.html'
    # queryset = Item.objects.all()
    context_object_name = 'object_list'
    
    def get_queryset(self):
        return PurchaseOrder.objects.filter(store= self.request.user.store)

class PurchaseOrderCreateView(CreateView):
    model = PurchaseOrder
    fields = ['supplier', 'branch', 'deliver_to', 'purchase_order_number',  'item', 'quantity', 'rate']
    template_name = 'purchase/purchaseorder_create.html'

   
           
class PurchaseOrderDetailView(DetailView):
      model = PurchaseOrder
      template_name = 'purchase/purchaseorder_detail.html'

class PurchaseOrderUpdateView(UpdateView):
    model = PurchaseOrder
    fields = '__all__'
    template_name: str = 'purchase/item_create.html'

class PurchaseOrderDeleteView(DeleteView):
    model = PurchaseOrder
    success_url = reverse_lazy('PurchaseOrder-list')