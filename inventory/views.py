from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.list import ListView

from inventory.forms import AddItemForm, AddSupplierForm
from inventory.models import Item, Supplier

@method_decorator(login_required, name='dispatch')
class ItemListView(ListView):
   
    # specify the model for list view
    model = Item
    template_name = 'inventory/list.html'
    # queryset = Item.objects.all()
    context_object_name = 'object_list'
    
    def get_queryset(self):
            
        if self.request.user.company_owner:                
            if self.request.user.company:
                return Item.objects.filter(store__company = self.request.user.company)
            else:
                return Item.objects.none()
        elif self.request.user.store == None:
            return Item.objects.filter(store= self.request.user.store)
        return Item.objects.filter(store= self.request.user.store)

class ItemCreateView(CreateView):
    model = Item
    form_class = AddItemForm
    template_name = 'inventory/item_create.html'

    def post(self,request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            success_url = reverse('item-detail', kwargs={'pk': obj.id})
            return HttpResponseRedirect(success_url)
            
        return self.form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ItemDetailView(DetailView):
      model = Item
      template_name = 'inventory/item_detail.html'

class ItemUpdateView(UpdateView):
    model = Item
    fields = '__all__'
    template_name: str = 'inventory/item_update.html'

class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('item-list')

# supplier

class SupplierListView(ListView):
   
    # specify the model for list view
    model = Supplier
    # template_name = 'inventory/supplier_list.html'
    # context_object_name = 'object_list'
    def get_queryset(self):
            
        if self.request.user.company_owner:
            return Supplier.objects.filter(company = self.request.user.company)
        elif self.request.user.store == None:
            return Supplier.objects.none()
        return Item.objects.filter(store= self.request.user.store)

class SupplierCreateView(CreateView):
    model = Supplier
    fields = '__all__'
    template_name = 'inventory/supplier_create.html'

   
class SupplierDetailView(DeleteView):
      model = Supplier
      template_name = 'inventory/supplier_detail.html'
      context_object_name = 'object'

class SupplierUpdateView(UpdateView):
    model = Supplier
    fields = '__all__'
    template_name: str = 'inventory/supplier_update.html'

class SupplierDeleteView(DeleteView):
    model = Supplier
    success_url = reverse_lazy('supplier-list')


class SupplierCreateView(CreateView):
    model = Supplier
    form_class = AddSupplierForm
    template_name = 'inventory/supplier_create.html'

    def post(self,request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            # if self.request.user.company_owner:
            #     return HttpResponse("You can't create an Supplier.")
            obj = form.save(commit=False)
            obj.company = self.request.user.company
            obj.save()
            success_url = reverse('supplier-detail', kwargs={'pk': obj.id})
            return HttpResponseRedirect(success_url)
            
        return self.form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
