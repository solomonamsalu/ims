from django import forms

from inventory.models import Item, Supplier
class AddItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields= '__all__'
class AddSupplierForm(forms.ModelForm):
    class Meta:
        model=Supplier
        fields='__all__'