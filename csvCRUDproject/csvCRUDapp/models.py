from django.db import models

# Create your models here.

class Student_data(models.Model):
    s_name=models.CharField(max_length=10)
    s_no=models.IntegerField()
