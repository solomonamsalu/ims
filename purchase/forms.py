
from django import forms
from inventory.models import Item

from purchase.models import PurchaseOrder
from core.models import User


class AddPurchaseOrderForm(forms.ModelForm):
  
    def __init__(self,  *args,  **kwargs):
        
        try:
            user = kwargs.pop('user') # Important to do this
        except:
            pass
        super(AddPurchaseOrderForm, self).__init__(*args, **kwargs)
        try:
            if user.company_owner:
                self.fields['item'].queryset = Item.objects.filter(store__company=user.company)
            else:
                self.fields['item'].queryset = Item.objects.filter(store=user.store)
                self.fields['deliver_to'].initial = user.store.address
        except:
            pass

    class Meta:
        model=PurchaseOrder
        fields = ['supplier', 'deliver_to', 'purchase_order_number',  'item', 'quantity', 'rate']

    def save(self, commit):
        return super().save(commit)