from django.db import models

# Create your models here.
class register_artist(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=120)
    category=models.CharField(max_length=15)

    def __str__(self):
        return self.fullname
