from django.http import HttpResponse
from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now()
    print("test function is called from view")
    # return HttpResponse("<h1>Hello this is index page</h1>" + str(date))
    return render(request, template_name='home.html', context={})


def about(request):
    return render(request, template_name='about.html',context= {})


def services(request):
    return render(request, template_name='services.html', context={})
