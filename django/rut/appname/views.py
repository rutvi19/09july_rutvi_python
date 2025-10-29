from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def modernart(request):
    return render(request, 'modernart.html')

def Gallery(request):
    return render(request, 'Gallery.html')

def design(request):
    return render(request, 'design.html')
