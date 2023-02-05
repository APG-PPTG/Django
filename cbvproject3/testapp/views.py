from django.shortcuts import render
from testapp.models import Company
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
class CompanyListView(ListView):
    model = Company
    # default template file : company_list.html
    # default context object : company_list

class CompanyDetailView(DetailView):
    model = Company
    # default template file : company_detail.htnl
    # default context object : company or object

class CompanyCreateView(CreateView):
    model = Company
    #fields = ('name', 'location', 'ceo')
    fields = '__all__'
    # default template file : company_form.htnl


class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('location', 'ceo')
    # default template file : company_form.htnl

class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('list')
