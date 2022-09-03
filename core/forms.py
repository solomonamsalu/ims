

from core.models import Company, Store
from django import forms


class AddStoreForm(forms.ModelForm):

    class Meta:
        model=Store
        # fields = '__all__'
        fields = ['company', 'store_number', 'address']

    def __init__(self,  *args,  **kwargs):
        
        try:
            user = kwargs.pop('user') # Important to do this
        except:
            pass
        super(AddStoreForm, self).__init__(*args, **kwargs)
        
        try:
            self.fields['company'].queryset = Company.objects.filter(id=user.company.id)
        except:
            self.fields['company'].queryset = Company.objects.none()
