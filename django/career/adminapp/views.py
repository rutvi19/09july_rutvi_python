from django.shortcuts import render,redirect
from django.contrib.auth import logout
from customer.models import *
from artist.models import *


# Create your views here.

def admin_dashboard(request):
    u=user_register.objects.all()
    a=register_artist.objects.all()

    total_u=len(u)
    total_a=len(a)
    return render(request,'admin_dashboard.html',{'total_u':total_u,'total_a':total_a});

def admin_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username=="admin" and password=="123":
            request.session['admin_login']=True
            print("login successfully")
            return redirect('admin_dashboard')
        else:
            print('login fail')
    return render(request,'admin_login.html');

def approve_artist(request):
    return render(request,'approve_artist.html');

def manage_users(request):
    return render(request,'manage_users.html');

def view_bookings(request):
    return render(request,'view_bookings.html');

def view_feedbacks(request):
    
    return render(request,'view_feedbacks.html');

def view_reviews(request):
    return render(request,'view_reviews.html');

def admin_logout(request):
    logout(request)
    return redirect('admin_login')