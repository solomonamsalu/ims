
from authentication.models import Address
from django.core.exceptions import ValidationError
from django.db import models
from inventory.models import Item, Supplier
from sales.models import SalesOrder


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

    def __str__(self) -> str:
        return self.purchase_order_number

    def clean(self):
        if self.item.on_hand_stock + self.quantity > self.item.max_stock:
            raise ValidationError({"quantity": "You are trying to purchase beyond the maximum stock!"})
        elif self.item.on_hand_stock + self.quantity < self.item.reorder_point:
            raise ValidationError({"quantity": "The stock will not go above the reorder point in this case!"})

