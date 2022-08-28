from django.contrib import admin
from django.urls import path
from purchase import views

urlpatterns = [
    path('purchasorders/', views.PurchaseOrderistView.as_view(), name='purchaseorder-list'),
    path('purchasorders/add/', views.PurchaseOrderCreateView.as_view(), name='purchaseorder-create'), 
    path('purchasorders/detail/<pk>/', views.PurchaseOrderDetailView.as_view() , name='purchaseorder-detail'),
    path('purchasorders/update/<pk>/', views.PurchaseOrderUpdateView.as_view() , name='purchaseorder-update'),
    path('purchasorders/delete/<pk>/', views.PurchaseOrderDeleteView.as_view() , name='purchaseorder-delete'),
]