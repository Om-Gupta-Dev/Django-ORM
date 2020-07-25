import os
from faker import Faker
import numpy as np
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'ORM.settings')
import django
django.setup()

from ModelManager.models import *

from ModelInheritence.models import *

fake = Faker()

def populate(n):
    for i in range(n):
        fname = fake.name()
        fsal = int(str(np.random.randint(60000,99999))+str(np.random.randint(60000,99999)))
        feno = fake.numerify()
        fadd = fake.address()
        Employee.objects.get_or_create(ename = fname , 
                                esal = fsal , 
                                eno = feno ,
                                eaddr = fadd )
    
# populate(10)

def populate(n):
    for i in range(n):
        fname = fake.name()
        fRoll = int(str(np.random.randint(10,99))+str(np.random.randint(0,9)))
        fMarks = int(str(np.random.randint(10,99))+str(np.random.randint(0,9)))
        femail = fake.email()
        fadd = fake.address()
        ContactInfo.objects.get_or_create(Name = fname , 
                                Marks = fMarks , 
                                Address = fadd ,
                                Email = femail , 
                                RollNo = fRoll , 
                                )
    
# populate(10)