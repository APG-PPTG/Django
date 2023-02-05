import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ormproject.settings')

import django
django.setup()

from testapp.models import Employee
from faker import Faker
from random import *
fake = Faker()

def populate(n):
    for i in range(n):
        feno = fake.random_int(min=1,max=999)
        fename =fake.name()
        fesal=randint(10000, 20000)
        faddress =fake.city()

#insertquery get_or_create (Django ORM related function)
# Models class variable = value from here
        emp_record = Employee.objects.get_or_create(eno=feno,
         ename=fename,
         esal=fesal,
         eaddr=faddress,
         )

n = int(input("Enter number of Records:"))
populate(n)
print(f'{n} Records Inserted Successfully')
