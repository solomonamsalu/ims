

from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    # path('items/', views.ItemListView.as_view(), name='item-list'),
    path('company/add/', views.CompanyCreateView.as_view(), name='company-create'), 
    path('companys/detail/<pk>/', views.CompanyDetailView.as_view() , name='company-detail'),
    # path('companys/update/<pk>/', views.companyUpdateView.as_view() , name='company-update'),
    # path('companys/delete/<pk>/', views.companyDeleteView.as_view() , name='company-delete'),

    # supplier
    # path('suppliers/', views.SupplierListView.as_view(), name='supplier-list'),
    path('store/add/', views.StoreCreateView.as_view(), name='store-create'), 
    path('store/detail/<pk>/', views.StoreDetailView.as_view() , name='store-detail'),
    # path('suppliers/update/<pk>/', views.SupplierUpdateView.as_view() , name='supplier-update'),
    # path('suppliers/delete/<pk>/', views.SupplierDeleteView.as_view() , name='supplier-delete'),
]
