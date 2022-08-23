

from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    path('items/', views.ItemListView.as_view(), name='item-list'),
    path('items/add/', views.ItemCreateView.as_view(), name='item-create'), 
    path('items/detail/<pk>/', views.ItemDetailView.as_view() , name='item-detail'),
    path('items/update/<pk>/', views.ItemUpdateView.as_view() , name='item-update'),
    path('items/delete/<pk>/', views.ItemDeleteView.as_view() , name='item-delete'),

    # supplier
    path('suppliers/', views.SupplierListView.as_view(), name='supplier-list'),
    path('suppliers/add/', views.SupplierCreateView.as_view(), name='supplier-create'), 
    path('suppliers/detail/<pk>/', views.SupplierDetailView.as_view() , name='supplier-detail'),
    path('suppliers/update/<pk>/', views.SupplierUpdateView.as_view() , name='supplier-update'),
    path('suppliers/delete/<pk>/', views.SupplierDeleteView.as_view() , name='supplier-delete'),
]
