from django.db import models

from inventory.models import Stock

class PurchaseOrder(models.Model):

    stock=models.ForeignKey(Stock,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    order_date=models.DateTimeField(auto_now_add=True)
    vendor=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
