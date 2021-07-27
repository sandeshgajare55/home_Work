from django.db import models

class book_Demo(models.Model):
    b_Name=models.CharField(max_length=20)
    b_Cost=models.IntegerField()
    b_Author=models.CharField(max_length=20)
