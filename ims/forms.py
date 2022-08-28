

from email.policy import default
from allauth.account.forms import LoginForm, SignupForm
from django.shortcuts import redirect
from requests import request
from core.models import Store
from django import forms
from django.http.response import HttpResponse


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    store_number = forms.ModelChoiceField(queryset=Store.objects.all())
    company_owner = forms.BooleanField(initial=False)
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.store = self.cleaned_data['store']
        user.save()
        return user

class CustomLoginForm(LoginForm):
    
    store_number = forms.CharField(max_length=100)
    fields = ['user_name', 'store', 'password']


    def login(self, *args, **kwargs):
        form = CustomLoginForm(self.request.POST)
        store_number = CustomLoginForm(self.request.POST).data['store_number']
        
        if self.user.store.store_number != store_number and self.user.company_owner == False:
            return redirect('account_login')
        # Add your own processing here.

        # You must return the original result.
        return super(CustomLoginForm, self).login(*args, **kwargs)


    