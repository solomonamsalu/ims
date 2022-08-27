
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from inventory.models import Item

from sales.models import SalesOrder


@receiver(post_save, sender=SalesOrder)
def sales_order_done(sender, instance, **kwargs):
    ''' Create sign off and send email to those who have to sign.'''
    sales_order = instance
    item = sales_order.item
    item.on_hand_stock -= sales_order.quantity
    post_save.disconnect(sales_order_done, sender=sender)
    item.save()
    post_save.connect(sales_order_done, sender=sender)

# @receiver(post_save, sender=Item)
# def item_create(sender, instance, **kwargs):
#     ''' Create sign off and send email to those who have to sign.'''
#     item = instance
#     item.store = request.user.store
#     post_save.disconnect(item_create, sender=sender)
#     item.save()
#     post_save.connect(item_create, sender=sender)

