from django.contrib import admin
from testapp.models import HydJob, PuneJob, BloreJob
# Register your models here.

class HydJobAdmin(admin.ModelAdmin):
    list_display = ['date', 'comp', 'title', 'elig', 'addr', 'email', 'phNo']

admin.site.register(HydJob, HydJobAdmin)

class PuneJobAdmin(admin.ModelAdmin):
    list_display = ['date', 'comp', 'title', 'elig', 'addr', 'email', 'phNo']

admin.site.register(PuneJob, PuneJobAdmin)

class BloreJobAdmin(admin.ModelAdmin):
    list_display = ['date', 'comp', 'title', 'elig', 'addr', 'email', 'phNo']

admin.site.register(BloreJob, BloreJobAdmin)
