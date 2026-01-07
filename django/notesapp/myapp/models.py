from django.db import models

# Create your models here.
class note_cls(models.Model):
    query = models.CharField(max_length=100)
    file = models.FileField(upload_to='MyNotes')
    message =models.CharField(max_length=1000)

