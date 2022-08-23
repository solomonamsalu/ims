

from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    path('items/', views.ItemListView.as_view(), name='item-list'),
    path('items/add/', views.ItemCreateView.as_view(), name='item-create'), 
    path('items/detail/<pk>/', views.ItemDetailView.as_view() , name='item-detail'),
    path('items/update/<pk>/', views.ItemUpdateView.as_view() , name='item-update'),
    path('items/delete/<pk>/', views.ItemDeleteView.as_view() , name='item-delete'),
]
