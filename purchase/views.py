
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.list import ListView
from purchase.forms import AddPurchaseOrderForm
from purchase.models import PurchaseOrder

@method_decorator(login_required, name='dispatch')
class PurchaseOrderistView(ListView):
   
    # specify the model for list view
    model = PurchaseOrder
    template_name = 'purchase/list.html'
    # queryset = Item.objects.all()
    context_object_name = 'object_list'
    
    def get_queryset(self):
        if self.request.user.company_owner:
            return PurchaseOrder.objects.filter(item__store__company= self.request.user.company)
        
        return PurchaseOrder.objects.filter()

class PurchaseOrderCreateView(FormView):
    model = PurchaseOrder
    template_name = 'purchase/purchaseorder_create.html'
    form_class = AddPurchaseOrderForm    
    
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
            success_url = reverse('purchaseorder-detail', kwargs={'pk': obj.id})
            return HttpResponseRedirect(success_url)
            
        return super().post(request, *args, **kwargs)
        

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