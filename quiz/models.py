from django.db import models

# Create your models here.

class Questions(models.Model):
    question=models.CharField(max_length=250)
    optiona=models.CharField(max_length=250)
    optionb=models.CharField(max_length=250)
    optionc=models.CharField(max_length=250)
    optiond=models.CharField(max_length=250)
    answer=models.CharField(max_length=250)
    
