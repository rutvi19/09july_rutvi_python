from django.shortcuts import render,redirect
from .forms import *
# Create your views here.
def artist_home(request):
    return render(request,"artist_home.html");

def artist_login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=register_artist.objects.filter(email = email,password = password).first()
        if user:
            request.session['user_id']=user.id
            return redirect(artist_home)
        else:
            print('lodin fail')
    return render(request,"artist_login.html");

def artist_manage_profile(request):
    return render(request,"artist_manage_profile.html");

def artist_cancel_booking(request):
    return render(request,"artist_cancel_booking.html");

def artist_register(request):
    if request.method=="POST":
        email=request.POST.get('email')
        form=artist_form(request.POST)
        if form.is_valid():
            user=form.save()
            print("resistered")
            return redirect('artist_login')
        else:
            print(form.errors)
    return render(request,"artist_register.html");

def artist_upload_media(request):
    return render(request,"artist_upload_media.html");

def artist_view_booking(request):
    return render(request,"artist_view_booking.html");

def artist_feedback(request):
    return render(request,"artist_feedback.html");


