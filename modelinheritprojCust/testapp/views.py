from django.shortcuts import render
from testapp.models import Employee
# Create your views here.
def display_view(request):
    employee_list = Employee.objects.get_emp_sal_range(19000,20000)
    return render(request, 'testapp/index.html', {'employee_list':employee_list})
