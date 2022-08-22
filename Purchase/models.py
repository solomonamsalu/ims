from tkinter import CASCADE
from django.db import models

class Supplier(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    company_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200,unique=True)
    phone=models.CharField(max_length=20,unique=True)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    Country=models.CharField(max_length=200)
    posta=models.CharField(max_lingn=200)
class PurchaseOrder(models.Model):
    supplier=models.ForeignKey(Supplier,on_delete=CASCADE):
    branch=models.CharField(max_length=200)
    deliver_to=models.CharField()
    purchase_order_number=models.IntegerField()
    date=models.DateField(auto_created=True)
    

    

