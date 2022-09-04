

"""ims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from reports import views

urlpatterns = [
  path('sales/by_customer/', views.ListSalesByCustomerReportView.as_view(), name='sales_by_customer-report'),
  path('sales/by_item/', views.ListSalesByItemReportView.as_view(), name='sales_by_item-report'),
  path('sales/by_item/', views.ListPurchaseByItemReportView.as_view(), name='purchase_by_item-report'),
  path('inventory_summary/', views.InventorySummaryReportView.as_view(), name='inventory_summary-report'),
  path('purchase/', views.ListPurchaseReportView.as_view(), name='purchase-report'),
  path('items/', views.ListItemReportView.as_view(), name='item-report'),

]
