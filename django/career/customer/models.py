from django.db import models

# Create your models here.
class user_register(models.Model):
    Fullname=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=120)
    mobile=models.CharField(max_length=15)

    def __str__(self):
        return self.full_name

    

