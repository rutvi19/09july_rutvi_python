from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
import random
from django.contrib.auth import logout
from finalproject import settings
from .models import *

# Create your views here.
def index(request):
    user=request.session.get("email")
    return render(request,'index.html',{'user':user})

def login(request):
    if request.method == "POST":
        u_email = request.POST.get("email")
        u_password = request.POST.get("password")

        # Use filter() instead of get() to avoid MultipleObjectsReturned
        user = userdata.objects.filter(email=u_email, password=u_password).first()

        if user:
            print("Login Successfully!")
            request.session["email"] = u_email
            request.session["userid"] = user.id
            return redirect("/")
        else:
            print("Error! Login Failed..")
            return render(request, 'login.html', {"error": "Invalid Email or Password"})

    return render(request, 'login.html') 


def signup(request):
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            form.save()
            #OTP Email Sending
            global otp
            otp=random.randint(11111,99999)
            sub="Your OTP for Verification"
            mail_msg=f"Dear User\n\nThanks for registration with us!\nYour Email Verification code is {otp}.\nPlease verify your account and enjoy our services!\n\nThank & Regards\nNotesApp Team\n+91 9429190565 | rutvimandaliya@gmail.com"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['email']]
            send_mail(subject=sub,message=mail_msg,from_email=from_ID,recipient_list=to_ID)
            return redirect('otp')
        else:
            print(form.errors)
    return render(request,'signup.html')

def userlogout(request):
    request.session.flush()   # clear all session data
    return redirect("/")


def otp(request):
    global otp
    msg=""
    if request.method=='POST':
        if otp==int(request.POST["otp"]):
            print("OTP verified successfully!")
            return redirect('login')
        else:
            msg="Invalid OTP! Please try again."
    return render(request,'otp.html',{'msg':msg})

def profile(request):
    userid = request.session.get("userid")

    if userid is None:
        return redirect("login")   
    try:
        user = userdata.objects.get(id=userid)
    except userdata.DoesNotExist:
        return redirect('login.html')  

    if request.method == 'POST':
        form = signupform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            print("Profile Updated!")
            return redirect("profile")
        else:
            print(form.errors)

    return render(request, 'profile.html', {'user': user})
       
        
def update_profile(request,id):
    user=userdata.objects.get(id=id)

    if request.method=='POST':
        update_user=signupform(request.POST,instance=user)
        if update_user.is_valid():
            update_user.save()
            return redirect('/')
        else:
            print(update_user.errors)
    return render(request,'update_profile.html',{'user':user}) 


def about(request):
    return render(request,'about.html');