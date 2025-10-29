from django.shortcuts import render
import random

# Create your views here.

def index(request):
    name="rutvi"
    num=random.randint(1,100)
    return render(request, 'index.html',{'name':name,'num':num})

def about(request):
    return render(request, 'about.html')

def info(request):
    return render(request, 'info.html')