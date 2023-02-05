from django.shortcuts import render
from testapp import models
# Create your views here.
def homepage_view(request):
    return render(request, 'testapp/HomePage.html')

def hydJobs_view(request):
    job_list = models.HydJob.objects.all()
    my_dict = {'job_list':job_list}
    return render(request, 'testapp/HydJobs.html', my_dict)

def puneJobs_view(request):
    job_list = models.PuneJob.objects.all()
    my_dict = {'job_list':job_list}
    return render(request, 'testapp/puneJobs.html', my_dict)

def bloreJobs_view(request):
    job_list = models.BloreJob.objects.all()
    my_dict = {'job_list': job_list}
    print(my_dict)
    return render(request, 'testapp/bloreJobs.html', my_dict)
