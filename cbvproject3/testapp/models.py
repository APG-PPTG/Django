from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=28)
    location = models.CharField(max_length=20)
    ceo = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})
