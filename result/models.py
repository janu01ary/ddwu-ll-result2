from django.db import models

# Create your models here.

class Result(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    pf = models.BooleanField(default=True)
    dateTime = models.CharField(max_length=100)

    def __str__(self):
        return self.name