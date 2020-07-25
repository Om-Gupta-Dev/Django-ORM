from django.db import models

# Create your models here.

from django.db import models

# Creating Custom Model Manager 

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('eno')       # OverWrites default all() method to get all records from database
                                                            # Calling Parent Class Method by using super()
    def esal_range(self,esal1,esal2):
        return super().get_queryset().filter(esal__range=(esal1,esal2))
    
    def sort_Employee(self,sorter):
        return super().get_queryset().order_by(sorter)
                                                            
# Fixed Things in Defining Custom Managers Models.Manager, def get_queryset(self) self can be changed but not recommended, return super().get_queryset()
# Name of class can be changed and .order_by() or other filters can be used
# We can define only one manager Class at a time by default 
# To define costom manager just define a function in customManager class 

# Create your models here.

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField( max_length=100 )
    esal = models.FloatField()
    eaddr = models.CharField(max_length=128)
    objects = CustomManager()       # objects --> name of model.objects.all()  if we use other name here i.e xyz=CustomManager() 
                                    # then we have to use model.xyz.all() to retrieve records
    def __str__(self):
        return self.ename
    