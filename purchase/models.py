
from django.db import models
from inventory.models import Item
from sales.models import SalesOrder
from authentication.models import Address
from inventory.models import Supplier

class PurchaseOrder(models.Model):
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    branch=models.CharField(max_length=200) # FIXME fix to foreignkey
    deliver_to = models.ForeignKey(Address, on_delete=models.CASCADE)
    purchase_order_number=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    item=models.ForeignKey(Item, on_delete= models.CASCADE)
    quantity = models.IntegerField()
    rate = models.FloatField()
    amount = models.FloatField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.amount = self.quantity*self.rate
        return super().save(*args, **kwargs)


