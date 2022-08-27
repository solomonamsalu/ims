from django.shortcuts import render

from core.models import Company, Store
from django.views.generic import CreateView, DeleteView, DetailView
from django.http.response import HttpResponseRedirect
from django.urls import reverse

class CompanyCreateView(CreateView):
    model = Company
    # form_class = AddCompanyForm
    fields = '__all__'
    template_name = 'core/company_create.html'

    
class CompanyDetailView(DetailView):
      model = Company
      template_name = 'core/company_detail.html'

class StoreCreateView(CreateView):
    model = Store
    # form_class = AddStoreForm
    fields = '__all__'
    template_name = 'core/store_create.html'

    
class StoreDetailView(DetailView):
      model = Store
      template_name = 'core/store_detail.html'

