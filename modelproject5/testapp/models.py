from django.db import models

# Create your models here.
class Student(models.Model):
    rollNo = models.IntegerField()
    stuName= models.CharField(max_length=30)
    dob = models.DateField()
    marks = models.IntegerField()
    email = models.EmailField()
    phno = models.BigIntegerField()
    address = models.TextField()
