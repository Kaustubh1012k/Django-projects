from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=225)
    email=models.EmailField(max_length=100)
    option1=models.CharField(max_length=2)
    option2=models.CharField(max_length=2)
    enquiry=models.TextField(max_length=300)

