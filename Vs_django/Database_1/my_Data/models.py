from django.db import models

class Item(models.Model):
    item_Name=models.CharField(max_length=20)
    item_Cost=models.FloatField()

