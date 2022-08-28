from django.contrib import admin
from django.urls import path
from sales import views

urlpatterns = [
    path('salesorders/', views.SalesOrderListView.as_view(), name='salesorder-list'),
    path('salesorders/add/', views.SalesOrderCreateView.as_view(), name='salesorder-create'), 
    path('salesorders/detail/<pk>/', views.SalesOrderDetailView.as_view() , name='salesorder-detail'),
    path('salesorders/update/<pk>/', views.SalesOrderUpdateView.as_view() , name='salesorder-update'),
    path('salesorders/delete/<pk>/', views.SalesOrderDeleteView.as_view() , name='salesorder-delete'),
]