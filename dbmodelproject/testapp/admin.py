from django.contrib import admin
from testapp.models import HydJobs, PuneJobs, BloreJobs
# Register your models here.

class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligib', 'address', 'email', 'phNo']

admin.site.register(HydJobs, HydJobsAdmin)

class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligib', 'address', 'email', 'phNo']

admin.site.register(PuneJobs, PuneJobsAdmin)

class BloreJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligib', 'address', 'email', 'phNo']

admin.site.register(BloreJobs, BloreJobsAdmin)
