from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import logout

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def stddashboard(request):
    std=request.session.get("std")
    return render(request,'stddashboard.html',{'std':std})

def register(request):
    if request.method=='POST':
        form=data(request.POST)
        if form.is_valid():
            form.save()
            print('registered successfully!')
            return redirect('login')
        else:
            print(form.errors)
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        s_course = request.POST.get('course')
        s_email = request.POST.get('email')
        s_password = request.POST.get('password')
        std = stdata.objects.filter(course=s_course, email=s_email, password=s_password)
        if std.exists():                     
            stdid = std.first()              
            print(stdid.id)
            print('login successful')
            request.session['std'] = s_email
            request.session['stdid'] = stdid.id
            return redirect('stddashboard')
        else:
            print('Login failed')
    return render(request, 'login.html')

def userlogout(request):
    logout(request)
    return redirect("/")

