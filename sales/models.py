
from django.contrib import admin
from core.models import Address
from django.core.exceptions import ValidationError
from django.db import models
from inventory.models import Item, Store
from django.conf import settings

class Customer(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone=models.CharField(max_length=20,unique=True)
    address=models.TextField()
    
    def __str__(self) -> str:
        return self.user.first_name +','+self.user.last_name
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
class SalesOrder(models.Model):

    customer_name=models.ForeignKey(Customer,on_delete=models.CASCADE)
    branch=models.CharField(max_length=255)
    sales_order_number=models.CharField(max_length=100)
    sales_order_date=models.DateTimeField(auto_now_add=True)
    item=models.ForeignKey(Item, on_delete= models.CASCADE)
    quantity = models.IntegerField()
    rate = models.FloatField()
    amount = models.FloatField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.amount = self.quantity*self.rate
        return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.sales_order_number

    def clean(self):
        if self.item.on_hand_stock < self.quantity:

            raise ValidationError({"quantity": f"You are trying to sell beyond the available stock! Maximum you can order is {self.item.on_hand_stock}"})


