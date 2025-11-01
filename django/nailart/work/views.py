from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cateye(request):
    return render(request, 'cateye.html')

