from django.views.generic import ListView
from django.shortcuts import render

# Create your views here.

class ListSalesReportView(ListView):

    template_name = 'reports/sales_list.html'
    