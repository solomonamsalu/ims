

from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    path('items/', views.ListItemView.as_view(), name='add_item'),
    path('items/add/', views.ItemView.as_view()), 
]
