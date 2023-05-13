from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=225)
    email=models.EmailField(max_length=100)
    place=models.CharField(max_length=200,default='N/A')
    address=models.CharField(max_length=250,null=True)
    enquiry=models.TextField(blank=True)
    date=models.DateField()
