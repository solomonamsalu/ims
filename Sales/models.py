from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200,unique=True)
    phone=models.CharField(max_length=20,unique=True)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    postal=models.CharField(max_length==200)
    
