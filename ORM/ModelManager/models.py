from django.db import models

# Create your models here.

from django.db import models

# Creating Custom Model Manager 

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('eno')       #OverWrites default all() method to get all records from database

# Create your models here.

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField( max_length=100 )
    esal = models.FloatField()
    eaddr = models.CharField(max_length=128)
    objects = CustomManager()
    
    def __str__(self):
        return self.ename
    