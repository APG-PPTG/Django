from django.db import models

# Create your models here.
class HydJob(models.Model):
    date = models.DateField()
    comp = models.CharField(max_length = 20)
    title= models.CharField(max_length = 20)
    elig = models.CharField(max_length = 20)
    addr = models.TextField()
    email= models.EmailField()
    phNo = models.BigIntegerField()


class PuneJob(models.Model):
    date = models.DateField()
    comp = models.CharField(max_length = 20)
    title= models.CharField(max_length = 20)
    elig = models.CharField(max_length = 20)
    addr = models.TextField()
    email= models.EmailField()
    phNo = models.BigIntegerField()

class BloreJob(models.Model):
    date = models.DateField()
    comp = models.CharField(max_length = 20)
    title= models.CharField(max_length = 20)
    elig = models.CharField(max_length = 20)
    addr = models.TextField()
    email= models.EmailField()
    phNo = models.BigIntegerField()
