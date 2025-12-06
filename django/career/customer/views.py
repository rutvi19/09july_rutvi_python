from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def cancel_booking(request):
    return render(request,"cancel_booking.html");

def book_artist(request):
    return render(request,"book_artist.html");

def feedback(request):
    return render(request,"feedback.html");

def home(request):
    return render(request,"home.html");

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=user_register.objects.filter(email = email,password = password).first()
        if user:
            request.session['user_id'] = user.id
            return redirect('home')
        else:
            print("login fail")
    return render(request,"login.html");

def manage_booking(request):
    return render(request,"manage_booking.html");

def manage_profile(request):
    return render(request,"manage_profile.html");

def register(request):
    msg=" "
    if request.method=='POST':
        email=request.POST.get('email')
        form = register_form(request.POST)
        if form.is_valid():
            user=form.save()
            print('registered')
            return redirect('login')
        else:
            print(form.errors)
    return render(request,"register.html");

def search_artist(request):
    return render(request,"search_artist.html");