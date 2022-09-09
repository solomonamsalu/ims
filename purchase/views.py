
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
class PurchaseReceiveListView(ListView):
   
    # specify the model for list view
    model = PurchaseOrder
    template_name = 'purchase/purchasereceive_list.html'
    # queryset = Item.objects.all()
    context_object_name = 'object_list'
    
    def get_queryset(self):
        if self.request.user.company_owner:
            return PurchaseOrder.objects.filter(item__store__company= self.request.user.company, status = 'RECEIVED')
        
        return PurchaseOrder.objects.filter(item__store = self.request.user.store,  status = 'RECEIVED')


@method_decorator(login_required, name='dispatch')
class PurchaseOrderListView(View):
   
    # specify the model for list view
    model = PurchaseOrder
    template_name = 'purchase/purchaseorder_list.html'
    # queryset = Item.objects.all()
    context_object_name = 'object_list'
    
    def get_queryset(self):
        if self.request.user.company_owner:
            return PurchaseOrder.objects.filter(item__store__company= self.request.user.company)
        
        return PurchaseOrder.objects.filter(item__store = self.request.user.store)

    form_class = AddPurchaseOrderForm
    template_name = 'purchase/purchaseorder_list.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        
        if self.request.user.company_owner:
            purchase_orders =  PurchaseOrder.objects.filter(item__store__company= self.request.user.company)
        
        else:
            purchase_orders = PurchaseOrder.objects.filter(item__store = self.request.user.store)
        return render(request, self.template_name, {'object_list': purchase_orders})

    def post(self, request, *args, **kwargs):
        status = request.POST['status']

        import json
        data = json.loads(status)['data']
        purchase_order = PurchaseOrder.objects.get(id = data[-1])
        status = data[0]
        if status == 'RECEIVED' and purchase_order.status == 'TRANSIT':
            purchase_order.status = data[0]
            purchase_order.save()
            # change on hand stock of item.
            item = purchase_order.item
            item.on_hand_stock += purchase_order.quantity
            item.save()
        if self.request.user.company_owner:
            purchase_orders =  PurchaseOrder.objects.filter(item__store__company= self.request.user.company)
        
        else:
            purchase_orders = PurchaseOrder.objects.filter(item__store = self.request.user.store)
        return render(request, self.template_name, {'object_list': purchase_orders})

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
    template_name: str = 'purchase/purchaseorder-update.html'

class PurchaseOrderDeleteView(DeleteView):
    model = PurchaseOrder
    success_url = reverse_lazy('PurchaseOrder-list')