from django.db import models

# Create your models here.
class stdata(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    course=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
