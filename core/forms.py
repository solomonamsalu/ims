

from django import forms

from core.models import Company, Store


class AddStoreForm(forms.ModelForm):

    def __init__(self,  *args,  **kwargs):
            try:
                user = kwargs.pop('user') # Important to do this
            except:
                pass
            super(AddStoreForm, self).__init__(*args, **kwargs)
            try:
                if user.company_owner:
                    self.fields['company'].queryset = Company.objects.filter(id=user.company.id)
                else:
                    self.fields['company'].queryset = Company.objects.filter(id=user.company.id)
            except:
                pass
    class Meta:
        model=Store
        # fields = '__all__'
        fields = ['company', 'store_number', 'address']

    def save(self, commit):
        return super().save(commit)
