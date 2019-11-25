from django.db import models
from django.shortcuts import redirect
from django.urls import reverse

# Create your models here.
class employee(models.Model):
    ename=models.CharField(max_length=256)
    eno=models.IntegerField()
    email=models.EmailField()


    def get_absolute_url(self):
        return reverse('home')