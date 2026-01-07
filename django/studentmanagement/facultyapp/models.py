from django.db import models

# Create your models here
class fa_data(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    confirmpassword = models.CharField(max_length=15)
