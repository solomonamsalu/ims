from django import forms

from inventory.models import Item, Supplier
class AddItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields = ['name', 'SKU_number', 'selling_price', 'cost_price', 'max_stock', 'on_hand_stock', 'reorder_point', 'Preferred_supplier']

    def save(self, commit):

        return super().save(commit)
class AddSupplierForm(forms.ModelForm):
    class Meta:
        model=Supplier
        fields='__all__'