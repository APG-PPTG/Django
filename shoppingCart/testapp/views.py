from django.shortcuts import render
from testapp.forms import AddItemsForm
# Create your views here.
def index_view(request):
    return render(request, 'testapp/home.html')

def displayitems_view(request):
    return render(request, 'testapp/displayitems.html')


def additem_view(request):
    form = AddItemsForm()
    response = render(request, 'testapp/additems.html', {'form':form})
    if request.method=='POST':
        form = AddItemsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['itemname']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name, quantity,120)
    return response
