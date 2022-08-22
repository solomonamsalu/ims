from tkinter import CASCADE
from django.db import models
from Purchase import Supplier
class Item(models.Model):
    name=models.CharField(max_length=100)
    SKU_number=models.IntegerField()
    seling_price=models.FloatField()
    cost_price=models.FloatField()
    on_hand_stock=models.IntegerField()
    reorder_point=models.IntegerField()
    Preferred_supplier=models.ForeignKey(Supplier,on_delete=CASCADE)
    
