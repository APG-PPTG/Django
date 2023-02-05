import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelproject5.settings')

import django
django.setup()

from testapp import models
from faker import Faker

from random import *
fakegen = Faker()

def phonenumbergen():
    d1 = randint(6, 9)
    num = str(d1)
    for i in range(9):
        num = num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        frollno = fakegen.random_int(min=1, max=999)
        fname =fakegen.name()
        fdob = fakegen.date()
        fmarks=fakegen.random_int(min=1, max=100)
        femail=fakegen.email()
        fphonenumber=phonenumbergen()
        faddress =fakegen.address()
        #insertquery get_or_create (Django ORM related function)
        #Models class variable = value from here
        student_record = models.hydJobs.objects.get_or_create(rollNo=frollno, stuName=fname , dob=fdob, marks=fmarks, email=femail, phno=fphonenumber, address=faddress)

populate(5)
