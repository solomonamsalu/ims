

from core.models import Store
from django import forms
from inventory.models import Item

from sales.models import Customer, SalesOrder


class AddSalesOrderForm(forms.ModelForm):
    
    def __init__(self,  *args,  **kwargs):
        
        try:
            user = kwargs.pop('user') # Important to do this
        except:
            pass
        super(AddSalesOrderForm, self).__init__(*args, **kwargs)
        try:
            if user.company_owner:
                self.fields['item'].queryset = Item.objects.filter(store__company=user.company)
                self.fields['customer'].queryset = Customer.objects.filter(store__company=user.company)
            else:
                self.fields['item'].queryset = Item.objects.filter(store=user.store)
                self.fields['customer'].queryset = Customer.objects.filter(store=user.store)
        except:
            pass
    class Meta:
        model=SalesOrder
        fields = ['customer',  'sales_order_number',  'item', 'quantity', 'rate']

    def save(self, commit):
        return super().save(commit)

class AddCustomerForm(forms.ModelForm):
    
    def __init__(self,  *args,  **kwargs):
        
        try:
            user = kwargs.pop('user') # Important to do this
        except:
            pass
        super(AddCustomerForm, self).__init__(*args, **kwargs)
        try:
            if user.company_owner:
                    self.fields['store'].queryset = user.company.store_set

            else:
                self.fields['store'].queryset = Store.objects.filter(id=user.store.id)
        except:
            pass
    
    class Meta:
        model=Customer
        # fields = '__all__'
        fields = [ 'first_name', 'last_name','store', 'phone', 'address']

    def save(self, commit):
        return super().save(commit)
