from django import forms
from core.models import Store

from inventory.models import Item, Supplier
class AddItemForm(forms.ModelForm):

    def __init__(self,  *args,  **kwargs):
        
        try:
            user = kwargs.pop('user') # Important to do this
        except:
            pass
        super(AddItemForm, self).__init__(*args, **kwargs)
        if user.company_owner:
                self.fields['store'].queryset = user.company.store_set
        else:
            self.fields['store'].initial = user.store
            self.fields['store'].queryset = Store.objects.filter(id=user.store.id)
    class Meta:
        model=Item
        fields = ['store', 'name', 'SKU_number', 'selling_price', 'cost_price', 'max_stock', 'on_hand_stock', 'reorder_point', 'Preferred_supplier']

    def save(self, commit):
        return super().save(commit)
        
class AddSupplierForm(forms.ModelForm):
    class Meta:
        model=Supplier
        fields='__all__'