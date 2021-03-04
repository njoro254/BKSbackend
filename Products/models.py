from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=70)
    photo = models.CharField(max_length=64)
    price  = models.IntegerField(default=0)
    uniqid = models.CharField(max_length=12)
    description = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name}"
