from django.shortcuts import render
from inventory.models import Item, Supplier
from django.http import HttpResponse
from inventory.forms import AddItemForm,AddSupplierForm
from django.views import View
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

class ItemListView(ListView):
   
    # specify the model for list view
    model = Item
    template_name = 'inventory/list.html'
    queryset = Item.objects.all()
    context_object_name = 'object_list'
    

class ItemCreateView(CreateView):
    model = Item
    fields = '__all__'
    template_name = 'inventory/item_create.html'

   
class ItemDetailView(DeleteView):
      model = Item
      template_name = 'inventory/item_detail.html'

class ItemUpdateView(UpdateView):
    model = Item
    fields = '__all__'
    template_name: str = 'inventory/item_create.html'

class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('item-list')

# supplier

class SupplierListView(ListView):
   
    # specify the model for list view
    model = Supplier
    # template_name = 'inventory/supplier_list.html'
    queryset = Supplier.objects.all()
    # context_object_name = 'object_list'
    

class SupplierCreateView(CreateView):
    model = Supplier
    fields = '__all__'
    template_name = 'inventory/supplier_create.html'

   
class SupplierDetailView(DeleteView):
      model = Supplier
      template_name = 'inventory/supplier_detail.html'

class SupplierUpdateView(UpdateView):
    model = Supplier
    fields = '__all__'
    template_name: str = 'inventory/supplier_create.html'

class SupplierDeleteView(DeleteView):
    model = Supplier
    success_url = reverse_lazy('supplier-list')



