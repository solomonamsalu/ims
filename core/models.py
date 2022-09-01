from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.utils.translation import gettext_lazy as _
from django.forms import ValidationError

class Company(models.Model):

    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('company-detail', kwargs={'pk': self.pk})

class Address(models.Model):

    city = models.CharField(max_length=255)
    state =models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.country+ ','+ self.city
class Store(models.Model):

    store_number = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    address = models.TextField()

    def __str__(self) -> str:
        return 'Store: ' + self.store_number

    def get_absolute_url(self):
        return reverse('store-detail', kwargs={'pk': self.pk})




class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, store, company, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, store, password, **other_fields)
    
    def create_user(self, email, user_name, first_name, store, company, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.store = store
        user.company = company
        user.save()
        return user

class User(AbstractUser):
    email = models.EmailField(null=True, blank=True)

    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, related_name='workers')
    company_owner = models.BooleanField(default=False)
    # objects = CustomAccountManager()

    # def clean(self):
    #     store = self.cleaned_data.get('store')
    #     company_owner = self.cleaned_data.get('company_owner')
    #     if not store and not company_owner:
    #         raise ValidationError('One of fields is required')
    #     return self.cleaned_data
    # def save(self, *args, **kwargs ):
    #     self.clean()
    #     return super().save(*args, **kwargs)