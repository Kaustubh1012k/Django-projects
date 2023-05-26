from django.db import models
from datetime import datetime

# Create your models here.
class SignUp(models.Model):
    username = models.CharField(max_length=225)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    date = models.DateField(default=datetime.now)
