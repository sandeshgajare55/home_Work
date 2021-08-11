from django.db import models


# Create your models here.

class Person(models.Model):
    p_name=models.CharField(max_length=15)
    p_sal=models.FloatField()

