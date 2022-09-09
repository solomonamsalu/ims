from django.contrib import admin
from django.urls import path
from purchase import views

urlpatterns = [
    path('purchaseorders/', views.PurchaseOrderListView.as_view(), name='purchaseorder-list'),
    path('purchasereceives/', views.PurchaseReceiveListView.as_view(), name='purchasereceive-list'),
    path('purchaseorders/add/', views.PurchaseOrderCreateView.as_view(), name='purchaseorder-create'), 
    path('purchaseorders/detail/<pk>/', views.PurchaseOrderDetailView.as_view() , name='purchaseorder-detail'),
    path('purchaseorders/update/<pk>/', views.PurchaseOrderUpdateView.as_view() , name='purchaseorder-update'),
    path('purchaseorders/delete/<pk>/', views.PurchaseOrderDeleteView.as_view() , name='purchaseorder-delete'),
]