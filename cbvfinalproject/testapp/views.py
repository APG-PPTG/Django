from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from testapp.models import Beer
# Create your views here.
class BeerListView(ListView):
    model = Beer
    #Default template file : beer_list.html
    #Default context obj name: beer_list

class BeerDetailView(DetailView):
    model = Beer
    # template file : beer_detail.html
    # context object name : beer or object

class BeerCreateView(CreateView):
    model = Beer
    fields = '__all__'
    # template file : beer_form.html

class BeerUpdateView(UpdateView):
    model = Beer
    fields = '__all__'
    # template file : beer_form.html

from django.urls import reverse_lazy
class BeerDeleteView(DeleteView):
    model = Beer
    success_url = reverse_lazy('list')
