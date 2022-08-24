


from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from inventory.models import Item

@receiver(post_save, sender=Item)
def purchase_order_done(sender, instance, **kwargs):
    ''' Create sign off and send email to those who have to sign.'''
    item = instance
    if item.on_hand_stock < item.reorder_point:
        item.enough = False
    else:
        item.enough = True

    post_save.disconnect(purchase_order_done, sender=sender)
    item.save()
    post_save.connect(purchase_order_done, sender=sender)