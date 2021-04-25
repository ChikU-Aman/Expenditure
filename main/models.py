from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    amount = models.IntegerField()
    note = models.CharField(max_length=100)

