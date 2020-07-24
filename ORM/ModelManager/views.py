from django.shortcuts import render

from ModelManager.models import Employee
# Create your views here.

def index(request):
    Employees = Employee.objects.all()
    return render(request , 'ModelManager/home.html' , {'employees':Employees})

# Model Manager is the Medium to communicate to the database 
# The Default Model Manager Provided by Django is objects
# i.e model.objects .objects is the Model Manager 
# We can confirm the same by checking the type of model.objects
# Go to python shell and import ModelClass from App.Model 
# and type : type(ModelClass.objects) it will return <class 'django.db.models.manager.Manager'>


# How to Define Our Own Custom Model Manager  
#  Default all() method 
# the all() method internally calls get_queryset function to get all models Records 
# we can Change all() method by OverWriting get_queryset function in models.py