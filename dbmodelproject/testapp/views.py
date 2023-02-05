from django.shortcuts import render
from testapp import models
from testapp.forms import JobApplicationForm
# Create your views here.

def homePageView(request):
    submitted = False
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            print("Form Validated printing data")
            print("Name:", form.cleaned_data['name'])
            print("Email:", form.cleaned_data['email'])
            print("Phone N:", form.cleaned_data['phNo'])
            submitted = True
    form = JobApplicationForm()
    return render(request, 'testapp/home.html', {'form':form, 'submitted':submitted})
