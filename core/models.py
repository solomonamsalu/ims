from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
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
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    # password = models.

    def __str__(self) -> str:
        return 'Store: ' + self.store_number

    def get_absolute_url(self):
        return reverse('store-detail', kwargs={'pk': self.pk})
class User(AbstractUser):
    email = models.EmailField(null=True, blank=True)

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)