from django.db import models

# Create your models here.
class Lion(models.Model):
    #we're defining the columns and constraints on the rows for each 
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=250)
    age = models.IntegerField()
    