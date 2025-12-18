from django.shortcuts import render,redirect
from .models import *
from .forms import *
from artist.models import *

# Create your views here.
def cancel_booking(request):
    return render(request,"cancel_booking.html");

def book_artist(request):
    return render(request,"book_artist.html");

def feedback(request):
    user_id = request.session.get('user_id')
    if request.method == 'POST':
        form=feedback_form(request.POST)
        if form.is_valid():
            fb=form.save(commit=False)
            fb.user=user_register.objects.get(id=user_id)
            fb.save()
            print("feedback sent")
            return redirect('feedback')
        else:
            print(form.errors)
    return render(request,'feedback.html',{'form': feedback_form()});

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
    user_id=request.session.get('user_id')
    if request.method=='POST':
        form=manage_booking_form(request.POST)
        if form.is_valid():
            booking=form.save(commit=False)
            booking.user=user_register.objects.get(id=user_id)
            booking.save()
            print("booking done")
            return redirect('manage_booking')
        else:
            print(form.errors)
    return render(request,"manage_booking.html");

def manage_profile(request):
    user_id=request.session.get('user_id')
    if not user_id:
        return redirect('login')
    try:
        user=user_register.objects.get(id=user_id)
    except user_register.DoesNotExist:
        return redirect('login')    
    if request.method=='POST':
        update_profile=register_form(request.POST,instance=user)
        if update_profile.is_valid():
            update_profile.save()
            print("profile updated")
        else:
            print("errors")
    return render(request,"manage_profile.html",{'user':user});

def register(request):
    msg=""
    if request.method=='POST':
        email=request.POST.get('email')
        form = register_form(request.POST)
        if form.is_valid():
            user=form.save()
            request.session['user_id']=user.id
            print('registered')
            return redirect('login')
        else:
            print(form.errors)
    return render(request,"register.html");

def search_artist(request):
    artist=register_artist.objects.all()
    return render(request,"search_artist.html",{'artist':artist});