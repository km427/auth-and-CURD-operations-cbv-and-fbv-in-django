from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField()
    phno=models.IntegerField()