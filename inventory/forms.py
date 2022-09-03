from core.models import Company, Store
from django import forms

from inventory.models import Item, Supplier


class AddItemForm(forms.ModelForm):

    def __init__(self,  *args,  **kwargs):
        
        try:
            user = kwargs.pop('user') # Important to do this
        except:
            pass
        super(AddItemForm, self).__init__(*args, **kwargs)
        try:
            if user.company_owner:
                    self.fields['store'].queryset = user.company.store_set
                    self.fields['Preferred_supplier'].queryset = Supplier.objects.filter(company=user.company)

            else:
                self.fields['store'].initial = user.store
                self.fields['store'].queryset = Store.objects.filter(id=user.store.id)
                self.fields['Preferred_supplier'].queryset = Supplier.objects.filter(company=user.company)
        except:
            pass
    class Meta:
        model=Item
        fields = ['store', 'name', 'SKU_number', 'selling_price', 'cost_price', 'max_stock', 'on_hand_stock', 'reorder_point', 'Preferred_supplier']

    def save(self, commit):
        return super().save(commit)
        
class AddSupplierForm(forms.ModelForm):


    def __init__(self,  *args,  **kwargs):
        
        try:
            user = kwargs.pop('user') # Important to do this
        except:
            pass
        super(AddSupplierForm, self).__init__(*args, **kwargs)
        try:
            if user.company_owner:
                    self.fields['store'].queryset = user.company.store_set
            else:
                self.fields['store'].initial = user.store
                self.fields['store'].queryset = Store.objects.filter(id=user.store.id)
        except:
            pass
    class Meta:
        model=Supplier
        fields = ['first_name', 'last_name', 'company_name',  'email', 'phone', 'address']

    