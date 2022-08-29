
from django import forms

from purchase.models import PurchaseOrder

class AddPurchaseOrderForm(forms.ModelForm):
    class Meta:
        model=PurchaseOrder
        fields = ['supplier', 'deliver_to', 'purchase_order_number',  'item', 'quantity', 'rate']

    def save(self, commit):
        self.clean()

        return super().save(commit)