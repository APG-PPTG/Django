from django.shortcuts import render, redirect
from testapp.models import Employee
from django.db.models import Q
# Create your views here.

def retrieve_view(request):
    #emp_list = Employee.objects.all()
    #emp_list = Employee.objects.filter(esal__gt=18000)
    #emp_list = Employee.objects.filter(ename__startswith='D') | Employee.objects.filter(esal__lt=11000)
    #emp_list = Employee.objects.filter(Q(ename__startswith='D') | Q(esal__lt=11000))
    #emp_list = Employee.objects.filter(ename__startswith='D') & Employee.objects.filter(esal__lt=11000)
    #emp_list = Employee.objects.filter(Q(ename__startswith='D') & (Q(esal__lt=11000)))
    #emp_list = Employee.objects.filter(ename__startswith='D',  esal__lt=11000)
    #emp_list = Employee.objects.exclude(ename__startswith='J')
    #emp_list = Employee.objects.filter(~Q(ename__startswith='D'))
    #emp_list = Employee.objects.all().values_list('ename', 'esal')
    #emp_list = Employee.objects.all().values('ename', 'esal', 'eaddr')
    emp_list = Employee.objects.all().only('ename', 'esal', 'eaddr')
    return render(request, 'testapp/specific.html', {'emp_list':emp_list})

from django.db.models import Avg, Sum, Min,Max, Count
def aggregate_view(request):
    avg = Employee.objects.all().aggregate(Avg('esal'))
    max = Employee.objects.all().aggregate(Max('esal'))
    min = Employee.objects.all().aggregate(Min('esal'))
    sum = Employee.objects.all().aggregate(Sum('esal'))
    count = Employee.objects.all().aggregate(Count('esal'))

    my_dict = {'avg':avg['esal__avg'], 'max':max['esal__max'], 'min':min['esal__min'], 'sum':sum['esal__sum'], 'count':count['esal__count']}
    return render(request, 'testapp/aggregate.html', my_dict)
