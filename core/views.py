from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, DetailView, ListView,UpdateView
from requests import request

from core.models import Company, Store
from inventory.models import Item


@login_required(login_url="/accounts/login/")
def home(request):

    return render(request, 'layouts/base.html')

def profile(request):
    
    return render(request, 'home/profile.html')


@method_decorator(login_required, name='dispatch')
class CompanyListView(ListView):
   
    # specify the model for list view
    model = Company
    template_name = 'core/company_list.html'
    context_object_name = 'object'
    
    def get_queryset(self):
        
        company = self.request.user.company
        if company:
            return company
        else:
            return None

class CompanyCreateView(CreateView):
    model = Company
    # form_class = AddCompanyForm
    fields = '__all__'
    template_name = 'core/company_create.html'

    
class CompanyDetailView(DetailView):
      model = Company
      template_name = 'core/company_detail.html'
class CompanyUpdateView(UpdateView):
    model = Company
    fields = '__all__'
    template_name = 'core/company_create.html'

class StoreCreateView(CreateView):
    model = Store
    # form_class = AddStoreForm
    fields = '__all__'
    template_name = 'core/store_create.html'

    
class StoreDetailView(DetailView):
      model = Store
      template_name = 'core/store_detail.html'
class StoreListView(ListView):
   
    # specify the model for list view
    model = Store
    template_name = 'core/store_list.html'
    # queryset = Item.objects.all()
    context_object_name = 'object_list'
    
    def get_queryset(self):
        return Store.objects.filter() # ODO filter the companies
class StoreUpdateView(UpdateView):
    model =Store
    fields = '__all__'
    template_name = 'core/store_create.html'



