

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
        if user.company_owner:
            self.fields['item'].queryset = Item.objects.filter(store__company=user.company)
        else:
            self.fields['item'].queryset = Item.objects.filter(store=user.store)

    class Meta:
        model=SalesOrder
        fields = ['customer_name',  'sales_order_number',  'item', 'quantity', 'rate']

    def save(self, commit):
        return super().save(commit)

class AddCustomerForm(forms.ModelForm):
    
    

    class Meta:
        model=Customer
        # fields = '__all__'
        fields = [ 'first_name', 'last_name', 'phone', 'address']

    def save(self, commit):
        return super().save(commit)