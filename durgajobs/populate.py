import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'durgajobs.settings')

import django
django.setup()

from testapp import models
from faker import Faker

from random import *
fake_gen = Faker()



def phonenumbergen():
    d1 = randint(6, 9)
    num = str(d1)
    for i in range(9):
        num = num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate = fake_gen.date()
        fcompany = fake_gen.company()
        ftitle = fake_gen.random_element(elements= ('Project Manager', 'Team Lead', 'Software Engineer', 'Associate Engineer'))
        feligibility = fake_gen.random_element(elements=('B.Tech', 'M.Tech', 'MCA', 'Phd'))
        faddress = fake_gen.address()
        femail = fake_gen.email()
        fphonenumber = phonenumbergen()
        hyd_jobs_record = models.BloreJob.objects.get_or_create(date=fdate, comp =fcompany , title=ftitle, elig=feligibility, addr=faddress, email = femail, phNo=fphonenumber)



#nsertquery get_or_create (Django ORM related function)
# Models class variable = value from here



n = int(input("Enter number of records:"))
populate(n)
print(f'(n) Records Inserted Successfully')
