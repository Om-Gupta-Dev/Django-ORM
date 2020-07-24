from django.shortcuts import render

# Create your views here.


# There are Basically 4 Types of Model Inheritence
# 1. Abstract Based Class Model Inheritence
# 2. Multi Table Inheritence 
# 3. Proxy Table Inheritence 
# 4. and 5. more or less are the part of 2. Multi Table Inheritence
# 4. Multiple Inheritence 
# 5. MultiLevel Inheritence
# NOTE: 1,2,3 are mainly used and important

def home(request):
    return render(request , 'ModelInheritence/home.html')