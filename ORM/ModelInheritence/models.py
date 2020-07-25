from django.db import models

# Create your models here.

# 1. Abstract Based Class Model Inheritence
# Creating Base Code to Call in other Models 
class ContactInfo(models.Model):
    Name = models.CharField(max_length=64)
    Email = models.EmailField()
    Address = models.CharField(max_length=264)
    
    class Meta:
        abstract = True         #Using this don't seperate model at database level And use Class Just at python code level to inherit
        

class Student(ContactInfo):
    RollNo = models.IntegerField()
    Marks = models.IntegerField()
    
class Teacher(ContactInfo):
    Subject = models.CharField(max_length=64)
    Salary = models.FloatField()
    
    
# 2. Multi Table Inheritence 
# In This Inheritence There Are Multiple table Created at Database Level which are connected by primary key refrence  
# In This Ex. 3 tables are created and 
# table ContactInfo1 contain 4 Fields i.e one extra ID field 
# table Student1 contain 3 Fields i.e one extra Primary Key  field Original Name of Table --> contactinfo1_ptr_id
# table Teacher1 contain 3 Fields i.e one extra Primary Key field Original Name of Table --> contactinfo1_ptr_id

class ContactInfo1(models.Model):
    Name = models.CharField(max_length=64)
    Email = models.EmailField()
    Address = models.CharField(max_length=264)

class Student1(ContactInfo1):
    RollNo = models.IntegerField()
    Marks = models.IntegerField()
    
class Teacher1(ContactInfo1):
    Subject = models.CharField(max_length=64)
    Salary = models.FloatField()
    

# 3. Proxy Model Inheritence 
# Proxy --> Duplicate View For The same(Existing) Table/Model 
# In this inheritence we define different view for the same table using Custom Model Managers

class CustomManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('Name')       # OverWrites default all() method to get all records from database
                                                            # Calling Parent Class Method by using super()
class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('RollNo')       # OverWrites default all() method to get all records from database
                                                            # Calling Parent Class Method by using super()
        

class ContactInfo(models.Model):
    Name = models.CharField(max_length=64)
    Email = models.EmailField()
    Address = models.CharField(max_length=264)
    RollNo = models.IntegerField()
    Marks = models.IntegerField()
    objects = CustomManager1()

# We Can Create any Numbers of Proxy Models
class ProxyContactInfo(ContactInfo):
    objects = CustomManager2()
    
    class Meta:
        proxy = True
    

# 4. Multiple Inheritence 
# This is same as 2. Multiple Table Inheritence BUT Here multiple parents are used 
# NOTE: here we will get error as same id field in parent tables 
# To Solve this error make any one primary key own defined fields   

class Parent1(models.Model):
    Name = models.CharField(max_length=64)
    Email = models.EmailField(primary_key=True)
    Address = models.CharField(max_length=264)

class Parent2(models.Model):
    RollNo = models.IntegerField(primary_key=True)
    Marks = models.IntegerField()
    
class Child1(Parent1,Parent2):
    CodeName = models.CharField(max_length=64)
    Salary = models.FloatField()
    
    
# 5. MultiLevel Inheritence
# In This type of Inheritence There is a series inheritence Parent->Child->SubChild

class Parent(models.Model):
    Name = models.CharField(max_length=64)
    Email = models.EmailField(primary_key=True)
    Address = models.CharField(max_length=264)

class Child(Parent):
    RollNo = models.IntegerField(primary_key=True)
    Marks = models.IntegerField()
    
class SubChild(Child):
    CodeName = models.CharField(max_length=64)
    Salary = models.FloatField()
    
