from django.shortcuts import render
from inventory.models import Item, Supplier
from django.http import HttpResponse
from inventory.forms import AddItemForm,AddSupplierForm
from django.views import View
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse
class ItemListView(ListView):
   
    # specify the model for list view
    model = Item
    template_name = 'inventory/list.html'
    # queryset = Item.objects.all()
    context_object_name = 'object_list'
    
    def get_queryset(self):
        return Item.objects.filter(store= self.request.user.store)

class ItemCreateView(CreateView):
    model = Item
    form_class = AddItemForm
    template_name = 'inventory/item_create.html'

    def post(self,request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.store = self.request.user.store
            obj.save()
            success_url = reverse('item-detail', kwargs={'pk': obj.id})
            return HttpResponseRedirect(success_url)
            
        return self.form_invalid(form)
           
class ItemDetailView(DetailView):
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



def home(request):

    return render(request, 'layouts/base.html')