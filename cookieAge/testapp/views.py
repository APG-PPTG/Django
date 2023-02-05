from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request, 'testapp/home.html')

def age_view(request):
    name = request.GET['name']
    print(name)
    response = render(request, 'testapp/age.html', {'name':name})
    response.set_cookie('name', name, 10)
    return response

def gf_view(request):
    age = request.GET['age']
    print(age)
    name = request.COOKIES.get('name')
    response = render(request, 'testapp/gf.html', {'name':name, 'age':age})
    response.set_cookie('age',age, 10)
    return response

def results_view(request):
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')
    gf  = request.GET['gf']
    response = render(request, 'testapp/results.html', {'name':name, 'age':age, 'gf':gf})
    response.set_cookie('gf', gf, 10)
    return response
