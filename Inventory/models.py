from tkinter import CASCADE
from django.db import models
from Purchase.models import Supplier

from authentication.models import Address

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


