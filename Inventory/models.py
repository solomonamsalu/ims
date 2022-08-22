from tkinter import CASCADE
from django.db import models

from authentication.models import Address
class Supplier(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    company_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200,unique=True)
    phone=models.CharField(max_length=20,unique=True)
    address=models.ForeignKey(Address, on_delete=models.CASCADE)
    
class Item(models.Model):
    name=models.CharField(max_length=100)
    SKU_number=models.IntegerField()
    seling_price=models.FloatField()
    cost_price=models.FloatField()
    on_hand_stock=models.IntegerField()
    reorder_point=models.IntegerField()
    Preferred_supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    
class Store(models.Model):

    store_number = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)



    