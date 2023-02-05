from django.shortcuts import render
from testapp.models import *
# Create your views here.

def dispaly_view(request):
    #employee_list = Employee.objects.all()
    employee_list = ProxyEmployee.objects.all()
    return render(request, 'testapp/index.html', {'employee_list':employee_list})
