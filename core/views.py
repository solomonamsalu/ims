from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.db.models.aggregates import Sum
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from inventory.models import Item
from requests import request

from core.forms import AddStoreForm
from core.models import Company, Store
from purchase.models import PurchaseOrder


@login_required(login_url="/accounts/login/")
def home(request):

    if request.method == 'GET':
        if request.user.company_owner:
            low_stock_items = Item.objects.filter(store__company=request.user.company).filter(on_hand_stock = F('reorder_point')).count()
            all_items = Item.objects.filter(store__company=request.user.company).count()
            quantity_in_hand = Item.objects.filter(store__company=request.user.company).aggregate(quantity_in_hand=Sum('on_hand_stock'))
            quantity_to_be_received = PurchaseOrder.objects.filter(item__store__company=request.user.company, status = 'TRANSIT').aggregate(quantity_to_be_received = Sum('quantity'))
        else:
            low_stock_items = Item.objects.filter(store=request.user.store).filter(on_hand_stock = F('reorder_point')).count()
            all_items = Item.objects.filter(store=request.user.store).count()
            quantity_in_hand = Item.objects.filter(store=request.user.store).aggregate(quantity_in_hand=Sum('on_hand_stock'))
            quantity_to_be_received =PurchaseOrder.objects.filter(item__store = request.user.store, status = 'TRANSIT').aggregate(quantity_to_be_received = Sum('quantity'))
        context = {
            'low_stock_items': low_stock_items,
            'all_items': all_items,
            'quantity_in_hand': quantity_in_hand,
            'quantity_to_be_received': quantity_to_be_received
        }
        return render(request, 'home/index.html', context=context)

@method_decorator(login_required, name='dispatch')
def profile(request):
    return render(request, 'home/profile.html')


@method_decorator(login_required, name='dispatch')
class CompanyListView(ListView):
   
    # specify the model for list view
    model = Company
    template_name = 'core/company_list.html'
    context_object_name = 'object'
    
    def get_queryset(self):
        
        try:
            company = self.request.user.store.company
        except:
            company = self.request.user.company

        if company:
            return company
        else:
            return Company.objects.none()

class CompanyCreateView(CreateView):
    model = Company
    # form_class = AddCompanyForm
    fields = '__all__'
    template_name = 'core/company_create.html'

    def post(self,request, *args, **kwargs):

        form = self.get_form_class()(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            # make the comany the company of the current user
            request.user.company = obj
            request.user.company_owner=True
            request.user.save()
            success_url = reverse('company-detail', kwargs={'pk': obj.id})
            return HttpResponseRedirect(success_url)
            
        return super().post(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class CompanyDetailView(DetailView):
      model = Company
      template_name = 'core/company_detail.html'
class CompanyUpdateView(UpdateView):
    model = Company
    fields = '__all__'
    template_name = 'core/company_update.html'

class StoreCreateView(CreateView):
    model = Store
    form_class = AddStoreForm
    template_name = 'core/store_create.html'

    def post(self,request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            # store_number = f.store_number
            obj = form.save(commit=False)
            # make the comany the company of the current Store
            if self.request.user.company:
                obj.company = self.request.user.company
                obj.save()
            else:
                obj.delete()
            success_url = reverse('store-detail', kwargs={'pk': obj.id})
            return HttpResponseRedirect(success_url)
            
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
        
@method_decorator(login_required, name='dispatch')    
class StoreDetailView(DetailView):
      model = Store
      template_name = 'core/store_detail.html'

@method_decorator(login_required, name='dispatch')
class StoreListView(ListView):
   
    # specify the model for list view
    model = Store
    # template_name = 'core/store_list.html'
    # queryset = Item.objects.all()
    context_object_name = 'object_list'
    
    def get_context_object_name(self, object_list):

        if self.request.user.company_owner:
            return 'object_list'
        return 'object'
    def get_template_names(self):
        if self.request.user.company_owner or self.request.user.store == None:
            return ['core/store_list.html',]
        return ['core/store_detail.html',]
        # return if self.requsuper().get_template_names()

    def get_queryset(self):
        if self.request.user.company_owner:
            try:
                return self.request.user.company.store_set.all()
            except:
                return Store.objects.none()
        return self.request.user.store
class StoreUpdateView(UpdateView):
    model =Store
    fields = '__all__'
    template_name = 'core/store_update.html'



