from django.shortcuts import render
from testapp.forms import LoginForm
import datetime
# Create your views here.

def home_view(request):
    form = LoginForm()
    return render(request, 'testapp/home.html', {'form': form})

def date_time_view(request):
    # This is a get request hence we use GET and value associated with this GET we need to pass
    # 1st request there is no Cookie
    name = request.GET['name']
    response = render(request, 'testapp/datetime.html', {'name':name})
    response.set_cookie('name', name)
    return response


def results_view(request):
    name = request.COOKIES.get('name')
    date_time = datetime.datetime.now()
    return render(request, 'testapp/Results.html', {'name':name, 'date_time':datetime})
