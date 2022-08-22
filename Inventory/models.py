from tkinter import CASCADE
from django.db import models
from Purchase import Supplier
class Item(models.Model):
    name=models.CharField(max_length=100)
    SKU_price=models.IntegerField()
    seling_price=models.DecimalField()
    cost_price=models.DecimalField()
    on_hand_stock=models.IntegerField()
    reorder_point=models.IntegerField()
    Preferred_supplier=models.ForeignKey(Supplier,on_delete=CASCADE)
    
