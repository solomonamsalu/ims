
from django import forms
from inventory.models import Item

from purchase.models import PurchaseOrder

class AddPurchaseOrderForm(forms.ModelForm):

    # item = forms.ModelChoiceField(queryset = Item.objects.filter(store__))
    class Meta:
        model=PurchaseOrder
        fields = ['supplier', 'deliver_to', 'purchase_order_number',  'item', 'quantity', 'rate']

    def save(self, commit):
        return super().save(commit)