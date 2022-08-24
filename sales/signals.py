



# import os
# from django.conf import settings
# from django.core.mail import send_mail
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from sales.models import SalesOrder
# from inventory.models import Item

# @receiver(post_save, sender=SalesOrder)
# def signoff(sender, instance, **kwargs):
#     ''' Create sign off and send email to those who have to sign.'''
#     sales_order = instance
    
#     items = sales_order.items.all()

#     for item in items:

#         item.on_hand_stock -= 