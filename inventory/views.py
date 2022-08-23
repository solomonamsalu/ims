from django.shortcuts import render
from inventory.models import Item
from django.http import HttpResponse
from inventory.forms import AddItemForm,AddSupplierForm
from django.views import View
from django.views.generic.list import ListView
class ItemView(View):
    form_class=AddItemForm
    # initial={'key','value'}
    template_name='add_item.html' 
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # <process form cleaned data>
            return HttpResponse('/success/')

        return render(request, self.template_name, {'form': form})




   
class ListItemView(ListView):
   
    # specify the model for list view
    model = Item
    template_name = 'list.html'
    queryset = Item.objects.all()
class SupplierView(View):
    form_class=AddSupplierForm
    template_name='add_supplier.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # <process form cleaned data>
            return HttpResponse('suplier is add successfully')


   
   