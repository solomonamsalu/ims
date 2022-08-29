

from django import forms

from sales.models import SalesOrder

class AddSalesOrderForm(forms.ModelForm):
    class Meta:
        model=SalesOrder
        fields = ['customer_name',  'sales_order_number',  'item', 'quantity', 'rate']

    def save(self, commit):
        return super().save(commit)