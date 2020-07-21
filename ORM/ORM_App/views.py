from django.shortcuts import render

from ORM_App.models import Employee
# Create your views here.


def display_view(request):
    # Selecting All Employees Data 
    employees = Employee.objects.all()
    
    # To see sql query in the backend use str(employees.query)

    # Filtering Employees on Different Filters
    # Syntax --> Model.objects.filter(FieldName__Filter=Vlaue) 
    # Filter 
    # __lt For Less Than
    # __lte For Less Than Equal to
    # __gt For Greater Than 
    # __gte For Greater Than Equal to
    # Ex Employee.objects.filter(esal__gt=1234567)

    # Filtering Employees on Exact Filters
    # Syntax --> Model.objects.get(FieldName__exact=Vlaue) if value is str Case matters Case sensitive
    # Syntax --> Model.objects.get(FieldName__iexact=Vlaue) if value is str Don't Case matters Case insensitive
    
    # Filtering data on the base of field values
    # Syntax --> Model.objects.filter(FieldName__contains=Vlaue) if value is str Case matters Case sensitive
    # Syntax --> Model.objects.filter(FieldName__icontains=Vlaue) if value is str Don't Case matters Case insensitive
    
    # Sql IN selector 
    # Syntax --> Model.objects.filter(FieldName__in=[values]) if value is str Case matters Case sensitive
    # Note There is no __inn for case insensitive 
    
    # StartsWith selector 
    # Syntax --> Model.objects.filter(FieldName__startswith=value) if value is str Case matters Case sensitive
    # Syntax --> Model.objects.filter(FieldName__istartswith=value) if value is str Don't Case matters Case insensitive
    
    # EndssWith selector 
    # Syntax --> Model.objects.filter(FieldName__endswith=value) if value is str Case matters Case sensitive
    # Syntax --> Model.objects.filter(FieldName__iendswith=value) if value is str Don't Case matters Case insensitive
    
    # Range Selector 
    # Syntax --> Model.objects.filter(FieldName__range=(start , end))
    
    # Using Multiple Conditions to filter -------------------------------
    # Using OR condition 
    # Method 1
    # queryset_1|queryset_2
    # Ex employees = Employee.objects.filter(esal__gt = 123456789 )|Employee.objects.filter(ename__startswith="J")
    
    # Method 2
    # from django.db.models import Q
    # Q(Condition1)|Q(condition2)
    # Ex employees = Employee.objects.filter(Q(esal__gt = 123456789 )|Q(ename__startswith="J"))
    
    # Using AND condition 
    # Method 1
    # model.objects.filter(condition1 , condition2)
    
    # Method 2
    # queryset_1&queryset_2
    # Ex employees = Employee.objects.filter(esal__gt = 123456789 )&Employee.objects.filter(ename__startswith="J")
    
    # Method 2
    # from django.db.models import Q
    # Q(Condition1)&Q(condition2)
    # Ex employees = Employee.objects.filter(Q(esal__gt = 123456789 )&Q(ename__startswith="J"))
    
    # How to Implement NOT queries 
    # Method 1
    # model.objects.exclude(condition) Exclude all values satisfying the given condition 
    # Method 2
    # from django.db.models import Q 
    # model.objects.filter(~Q(condition))

    employees = Employee.objects.filter(ename__in =['derrick Donovan', 'Joel Howard'])


    my_dict = {'employees':employees}
    return render(request , 'ORM_App/index.html' , my_dict)