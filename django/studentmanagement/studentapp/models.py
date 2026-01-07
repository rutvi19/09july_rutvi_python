from django.db import models

# Create your models here.
class stdata(models.Model):
    fullname=models.CharField(max_length=100)   
    email=models.EmailField()
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=15)
    role=models.CharField(max_length=15)

class std_course(models.Model):
  user = models.ForeignKey(stdata, on_delete=models.CASCADE)
  course = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.course

class contact_std_cls(models.Model):
   user = models.ForeignKey(stdata,on_delete=models.CASCADE)
   message = models.CharField(max_length=100)
   image = models.ImageField()


class notes_cls(models.Model):
    user = models.ForeignKey(stdata, on_delete=models.CASCADE) 
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title