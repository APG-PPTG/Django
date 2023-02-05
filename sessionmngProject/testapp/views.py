from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request, 'testapp/home.html')

def age_view(request):
    name = request.GET['name']
    response = render(request, 'testapp/age.html', {'name':name})
    response.set_cookie('name', name)
    return response

def gf_view(request):
    name = request.COOKIES.get('name')
    Age = request.GET['age']
    response = render(request, 'testapp/gf.html', {'Age':Age}) 
    response.set_cookie('Age', Age)
    return response

def results_view(request):
    name = request.COOKIES.get('name')
    Age = request.COOKIES.get('Age')
    GFName= request.GET['gfName']
    response = render(request, 'testapp/results.html', {'name':name, 'Age':Age, 'GFName':GFName})
    return response
