from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(null=True, blank=True)
class Company(models.Model):

    name = models.CharField(max_length=100)
    

    def __str__(self) -> str:
        return self.name

class Address(models.Model):

    city = models.CharField(max_length=255)
    state =models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.country+ ','+ self.city
