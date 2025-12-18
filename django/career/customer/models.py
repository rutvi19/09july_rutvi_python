from django.db import models
import datetime

# Create your models here.
class user_register(models.Model):
    Fullname=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=120)
    mobile=models.CharField(max_length=15)

    def __str__(self):
        return self.Fullname
    
class manage_booking_cls(models.Model):
    user=models.ForeignKey(user_register,on_delete=models.CASCADE)
    artist_name=models.CharField(max_length=100)
    booking_date=models.DateField(auto_now=True)    

class feedback_cls(models.Model):
    user=models.ForeignKey(user_register,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    feedback=models.CharField(max_length=500)