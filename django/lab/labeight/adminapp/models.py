from django.db import models

class Specialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE
    )
    hospital = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
