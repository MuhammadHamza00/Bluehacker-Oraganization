from email import message
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30, null=True, blank=True)
    email=models.EmailField(max_length=254,null=True,blank=True)
    message=models.CharField(max_length=30, null=True, blank=True)

class newsletter(models.Model):
    email=models.EmailField(max_length=254,null=True,blank=True)

class pricing_class(models.Model):
    plan=models.CharField(max_length=254,null=True,blank=True)   
    price=models.CharField(max_length=254,null=True,blank=True)   
    period=models.CharField(max_length=254,null=True,blank=True)   
    
# class Signup(models.Model):
#     username=models.EmailField(max_length=254,null=True,blank=True)
#     email=models.EmailField(max_length=254,null=True,blank=True)
#     password=models.EmailField(max_length=254,null=True,blank=True)
    