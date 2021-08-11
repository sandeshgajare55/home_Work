from django.db import models

# Create your models here.
class Teacher(models.Model):
    t_name=models.CharField(max_length=20)
    t_experience=models.IntegerField()

    class meta:
        db_table:'Teacher'