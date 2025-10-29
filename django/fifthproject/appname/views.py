from django.shortcuts import render
import random

# Create your views here.
n=1
def index(request):
    name="rutvi"
    num=random.randint(1,100)
    global n
    n=n+1
    return render(request, 'index.html', {'name': name, 'num': num,'n': n})