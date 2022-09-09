

from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from purchase.models import PurchaseOrder
from inventory.models import Item

@receiver(post_save, sender=PurchaseOrder)
def purchase_order_done(sender, instance, **kwargs):
    pass