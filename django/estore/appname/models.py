from django.db import models

# Create your models here.

class UserSignup(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname
   

class LoginForm(models.Model):
    Emailaddress=models.CharField(max_length=100)
    password=models.CharField(max_length=50)

def __str__(self):
    return self.Email