from django.contrib import admin

from ORM_App.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno' , 'ename' , 'esal' , 'eaddr']
    
    
# Register your models here.


admin.site.register(Employee , EmployeeAdmin)