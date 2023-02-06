from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def course(request):
    return HttpResponse('Welcome to Django for web & AI')

def Data_Science(request):
    return HttpResponse('Welcome to Data_Science course')

def Big_Data(request):
    return HttpResponse('Welcome to Big_Data course')

def Data_Analysis(request):
    return HttpResponse('Welcome to Data_Analysis course')

def Deep_Learning(request):
    return HttpResponse('Welcome to Deep_Learning course')

