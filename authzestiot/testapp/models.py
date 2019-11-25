from django.db import models

# Create your models here.
class employees(models.Model):
    name=models.CharField(max_length=256)
    phno=models.IntegerField()
    email=models.EmailField()