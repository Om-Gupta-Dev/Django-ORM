from django.shortcuts import render

from django.db.models.functions import Lower

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
    
    # Range Selector ----------NOTE: for int fields provide small value first then large value to select in range 
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
    
    # How to Implement UNION Operation for Querysets
    # UNION Operation is like OR Operation But Very Helpful when working with multiple tables 
    # Also Here is a Twist in The Case and that is For performing UNION Operation to different Querysets 
    # Both Querysets Should contain Same Columns and Same Number of Columns Otherwise Error
    # But we can select particular fields and perform Operations using .values_list(fieldnames)
    # QuerySet3 = QuerySet1.Union(QuerySet2)
    
    # Selecting Particular Fields From QuerySet
    # Method 1  Using values_list()
    # Syntax --> model.objects.all().values_list('fieldname1' , 'fieldname2', ....)
    # The values_list() method returns a QuerySet containing tuples:
    # <QuerySet [(1,), (2,)]>
    
    # Method 2  Using values()
    # Syntax --> model.objects.all().values('fieldname1' , 'fieldname2', ....)
    # NOTE: The values() method returns a QuerySet containing dictionaries:
    # <QuerySet [{'comment_id': 1}, {'comment_id': 2}]>

    # Method 3  Using only()
    # Syntax --> model.objects.all().values_list('id' , 'fieldname1' , 'fieldname2', ....) Gives ID Also By Default
    
    # Adding Record to Database
    # Syntax --> object = model(field1='value' , field2=value, ....)
    # Object.save()
    
    # Creating Multiple Record at once 
    # object1 = model(field1='value' , field2=value, ....)
    # object2 = model(field1='value' , field2=value, ....)
    # object3 = model(field1='value' , field2=value, ....)
    # object4 = model(field1='value' , field2=value, ....)
    # model.objects.bulk_create([object1,object2,object3,object4])
    
    # Deleting Record from Database NOTE: Here NO Rollback is there So Take Care Before Deleting
    # 1. get Object  2. Delete Object From Database  
    # 1. object = model.objects.get(field=Value)  Any One Field To Extract 
    # 2. object.delete()
    
    # Deleting Multiple Records From Database
    # 1. get Object  2. Delete Object From Database  
    # 1. object = model.objects.filter(condition)  Any One Field To Extract 
    # Ex. object = Employee.objects.filter(esal__gt=15000)
    # 2. object.delete()
    
    # Deleting All Records From Database also called TRUNCATE Operation
    # 1. get All Object  2. Delete All Objects From Database  
    # 1. object = model.objects.all()
    # Ex. object = Employee.objects.all()
    # 2. object.delete()
    # OR Directly model.bojects.all().delete()
    
    # How to Update Record
    # 1. Get Object  2. Update Record  3. Save Changes
    # 1. object = model.objects.get(field=Value)  Any One Field To Extract 
    # 2. object.FieldName = NewValue
    # 3. object.save()
    
    # How To Sort QuerySet --------------NOTE: QuerySet is Always List Type
    # objects = model.objects.all().order_by('FieldName') By Default Ascending Order FieldName
    # objects = model.objects.all().order_by('-FieldName') Sort By Descending Order FieldName
    
    # objects = model.objects.all().order_by('-FieldName')[0] Highest FieldName Only 
    # objects = model.objects.all().order_by('FieldName')[0] Lowest FieldName Only 
    
    # objects = model.objects.all().order_by('-FieldName')[0:3] Top Three FieldName Only Using Slice Operator
    # objects = model.objects.all().order_by('FieldName')[0:3] Last Three FieldName Only Using Slice Operator
    
    # NOTE: If We apply on Order by Alphabetical field then the ordering will be done on the basis of UNICode Values
    # That is UNOCodes like A-->65, B-->66 BUT a-->97, b-->98
    # Thats Why a(Small Characters(Starting)) comes After Capital Alphabets(Starting)
     
    # To Fix This We Can use Lower Function from django.db.models.functions
    # from django.db.models.functions import Lower
    # objects = model.objects.all().order_by(Lower('FieldName'))

    employees = Employee.objects.all().order_by(Lower('ename'))

    my_dict = {'employees':employees}
    return render(request , 'ORM_App/index.html' , my_dict)