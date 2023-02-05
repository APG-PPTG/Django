from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("<h1> This response is from class Based View </h1>")

class TemplateCBV(TemplateView):
    template_name = 'testapp/results.html'

# how to pass context parameters
class TemplateCBV2(TemplateView):
    template_name = 'testapp/results2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Durga'
        context['marks'] = 100
        context['subject'] = 'Django'
        return context
