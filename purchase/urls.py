from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    path('purchasorders/', views.PuchaseOrderListView.as_view(), name='puchaseOrder-list'),
    path('purchasorders/add/', views.PuchaseOrderCreateView.as_view(), name='puchaseOrder-create'), 
    path('purchasorders/detail/<pk>/', views.PuchaseOrderDetailView.as_view() , name='puchaseOrder-detail'),
    path('purchasorders/update/<pk>/', views.PuchaseOrderUpdateView.as_view() , name='puchaseOrder-update'),
    path('purchasorders/delete/<pk>/', views.PuchaseOrderDeleteView.as_view() , name='puchaseOrder-delete'),
]