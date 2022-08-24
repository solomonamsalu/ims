

from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from purchase.models import PurchaseOrder
from inventory.models import Item

@receiver(post_save, sender=PurchaseOrder)
def purchase_order_done(sender, instance, **kwargs):
    ''' Create sign off and send email to those who have to sign.'''
    purchase_order = instance
    item = purchase_order.item
    item.on_hand_stock += purchase_order.quantity
    post_save.disconnect(purchase_order_done, sender=sender)
    item.save()
    post_save.connect(purchase_order_done, sender=sender)