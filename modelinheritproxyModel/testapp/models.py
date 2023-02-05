from django.db import models

# Create your models here.

class CustomManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__gte=15000)

class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__lte=15000)


class Employee(models.Model):
    eno = models.IntegerField()
    ename= models.CharField(max_length=30)
    esal= models.FloatField()
    eaddr= models.CharField(max_length=30)
    objects=CustomManager1()

class ProxyEmployee(Employee):
    objects=CustomManager2()
    class Meta:
        proxy=True
