from django import forms

from inventory.models import Item
class AddItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields= '__all__'
    

    
    # name=forms.CharField(max_length=100)
    # SKU_number=forms.CharField(max_length=100)
    # seling_price=forms.FloatField()
    # cost_price=forms.FloatField()
    # max_stock=forms.IntegerField()
    # on_hand_stock=forms.IntegerField()
    # reorder_point=forms.IntegerField()
    # # Preferred_supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    