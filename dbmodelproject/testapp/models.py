from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date    = models.DateField()
    company = models.CharField(max_length = 20)
    title   = models.CharField(max_length = 20)
    eligib  = models.CharField(max_length = 20)
    address = models.TextField()
    email   = models.EmailField()
    phNo    = models.BigIntegerField()

class PuneJobs(models.Model):
    date    = models.DateField()
    company = models.CharField(max_length = 20)
    title   = models.CharField(max_length = 20)
    eligib  = models.CharField(max_length = 20)
    address = models.TextField()
    email   = models.EmailField()
    phNo    = models.BigIntegerField()

class BloreJobs(models.Model):
    date    = models.DateField()
    company = models.CharField(max_length = 20)
    title   = models.CharField(max_length = 20)
    eligib  = models.CharField(max_length = 20)
    address = models.TextField()
    email   = models.EmailField()
    phNo    = models.BigIntegerField()
