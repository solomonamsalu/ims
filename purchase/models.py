
from core.models import Address, Store
from django.core.exceptions import ValidationError
from django.db import models
from inventory.models import Item, Supplier
from django.urls import reverse

class PurchaseOrder(models.Model):
    # store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    deliver_to = models.TextField()
    purchase_order_number=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    item=models.ForeignKey(Item, on_delete= models.CASCADE)
    quantity = models.IntegerField()
    rate = models.FloatField()
    amount = models.FloatField(null=True, blank=True)
    received = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        self.amount = self.quantity*self.rate
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.purchase_order_number

    def clean(self):
        if self.item.on_hand_stock + self.quantity > self.item.max_stock:
            max_order = self.item.max_stock - self.item.on_hand_stock
            raise ValidationError({"quantity": f"You are trying to purchase beyond the maximum stock! The maximum you can order is {max_order}"})
        elif self.item.on_hand_stock + self.quantity < self.item.reorder_point:
            min_order = self.item.reorder_point - self.item.on_hand_stock
            raise ValidationError({"quantity": f"The stock will not go above the reorder point in this case! The minimum you can order is {min_order}"})

    def get_absolute_url(self):
        return reverse('purchaseorder-detail', kwargs={'pk': self.pk})