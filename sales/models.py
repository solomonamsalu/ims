
from django.db import models
from inventory.models import Item, Store
from authentication.models import Address


class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200,unique=True)
    phone=models.CharField(max_length=20,unique=True)
    address=models.ForeignKey(Address, on_delete=models.CASCADE)
   
class SalesOrder(models.Model):

    customer_name=models.ForeignKey(Customer,on_delete=models.CASCADE)
    branch=models.ForeignKey(Store,on_delete=models.CASCADE)
    sales_order_number=models.CharField(max_length=100)
    sales_order_date=models.DateTimeField(auto_now_add=True)
    item=models.ForeignKey(Item, on_delete= models.CASCADE)
    quantity = models.IntegerField()
    rate = models.FloatField()
    amount = models.FloatField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.amount = self.quantity*self.rate
        return super().save(*args, **kwargs)




