

from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    path('items/', views.list_items), 
    path('items/add/', views.add_item, name='add_item'),
]
