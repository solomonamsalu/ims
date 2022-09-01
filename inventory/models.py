from tkinter import CASCADE

from django.db import models
from django.urls import reverse
from core.models import Company, Store


class Supplier(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    company_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200,unique=True)
    phone=models.CharField(max_length=20,unique=True)
    address=models.TextField()

    def __str__(self) -> str:
        return self.first_name + ' '+ self.last_name
    
    def get_absolute_url(self):
        return reverse('supplier-detail', kwargs={'pk': self.pk})
class Item(models.Model):
    name=models.CharField(max_length=100)
    store = models.ForeignKey(Store, on_delete=models.CASCADE,null=True,blank=True)
    SKU_number=models.CharField(max_length=100)
    selling_price=models.FloatField()
    cost_price=models.FloatField()
    max_stock=models.IntegerField()
    on_hand_stock=models.IntegerField()
    reorder_point=models.IntegerField()
    Preferred_supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    enough = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk': self.pk})
    
    
