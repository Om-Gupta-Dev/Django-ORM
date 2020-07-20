from django.shortcuts import render

from ORM_App.models import Employee
# Create your views here.


def display_view(request):
    employees = Employee.objects.all()
    my_dict = {'employees':employees}
    return render(request , 'ORM_App/index.html' , my_dict)