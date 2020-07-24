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
    
    