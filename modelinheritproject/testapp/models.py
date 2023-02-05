from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length=20)
    email= models.EmailField()
    address= models.CharField(max_length=20)
    class Meta:
        abstract = True

class Student(ContactInfo):
    rollNo= models.IntegerField()
    marks = models.IntegerField()

class Teacher(ContactInfo):
    subject= models.CharField(max_length=20)
    salary= models.FloatField()

class ContactInfo1(models.Model):
    name = models.CharField(max_length=20)
    email= models.EmailField()
    address= models.CharField(max_length=20)


class Student1(ContactInfo):
    rollNo= models.IntegerField()
    marks = models.IntegerField()

class Teacher1(ContactInfo):
    subject= models.CharField(max_length=20)
    salary= models.FloatField()


# Multi Level inheritance
class Person(models.Model):
    name = models.CharField(max_length=20)
    age  = models.IntegerField()


class Employee(Person):
    eno = models.IntegerField()
    esal = models.FloatField()


class Manager(Employee):
    exp = models.IntegerField()
    team_size = models.IntegerField()


# Multiple inheritance
class Parent1(models.Model):
    f1 = models.CharField(max_length=22)
    f2 = models.CharField(max_length=22)

class Parent2(models.Model):
    f3 = models.CharField(max_length=22, primary_key=True)
    f4 = models.CharField(max_length=22)

class Child(Parent1, Parent2):
    f5 = models.CharField(max_length=22)
    f6 = models.CharField(max_length=22)
