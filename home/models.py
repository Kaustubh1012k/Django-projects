from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=100)
    place = models.TextField()
    address = models.TextField()
    enquiry = models.TextField()
    date = models.DateField(default=datetime.now)
