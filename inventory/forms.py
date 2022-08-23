from django import forms

from inventory.models import Item
class AddItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields= '__all__'