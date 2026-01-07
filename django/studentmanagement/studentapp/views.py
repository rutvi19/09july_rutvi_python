from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import logout
from django.conf import settings
from django.core.mail import send_mail
import random

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def stddashboard(request):
    user_id = request.session.get("user_id")

    if not user_id:
        return redirect('login')

    user = stdata.objects.get(id=user_id)
    return render(request,'stddashboard.html',{'user':user})

def register(request):
    if request.method=='POST':
        email=request.POST.get('email')
        # if stdata.objects.filter(email=email).exists():
        #     return render(request,'register.html')
        form=stdform(request.POST)
        if form.is_valid():
            form.save()
            # request.session['user_id'] = user.id
            global otp
            otp = random.randint(11111, 99999)
            subject = "Your OTP for Verification"
            mail_msg=f"Dear User\n\nThanks for registration with us!\nYour Email Verification code is {otp}.\nPlease verify your account and enjoy our services!\n\nThank & Regards\nNotesApp Team\n+91 9724799469 | rutvimandaliya19@gmail.com"
            from_email=settings.EMAIL_HOST_USER
            to_email = [email]

            send_mail(subject=subject,message=mail_msg,from_email=from_email,recipient_list=to_email)

            print("Registered successfully, OTP sent!")
            return redirect('otpverify')
        else:
            print(form.errors)
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        s_email = request.POST.get('email')
        s_password = request.POST.get('password')
        user= stdata.objects.filter(email=s_email, password=s_password).first()
        if user:
            request.session['user_id'] = user.id                    
            print('login successfully!!')
            return redirect('stddashboard')
        else:
            print('Login failed')
    return render(request, 'login.html')

def userlogout(request):
    logout(request)
    return redirect("/")

def profile(request):
    user_id = request.session.get("user_id")
    user=stdata.objects.get(id=user_id)
    if request.method == 'POST':
        ureq=stdform(request.POST,instance=user)
        if ureq.is_valid():
            ureq.save()
            print("Profile updateddd!!!")
            return redirect("stddashboard")
        else:
            print(ureq.errors)
    return render(request,'profile.html',{'user':user})

def course(request):
    user_id = request.session.get('user_id')
    # user not logged in
    if not user_id:
        return redirect('login')
    user = stdata.objects.get(id=user_id)
    if request.method == "POST":
        course_name = request.POST.get('course')
        # prevent duplicate enrollment (optional but recommended)
        if not std_course.objects.filter(user=user, course=course_name).exists():
            std_course.objects.create(
                course=course_name,
                user=user
            )
        return redirect('stddashboard')
    # GET request → show page
    courses = std_course.objects.filter(user=user)
    return render(request, 'course.html', {
        'user': user,
        'courses': courses
    })


def otpverify(request):
    global otp
    msg=""
    if request.method=='POST':
        if otp == int(request.POST["otp"]):
            print("Verification Successfull")
            
            return redirect("login")
        else:
            msg="Sorry!Verfication faild....Try again!"
    return render(request,'otpverify.html',{'msg':msg})


def notes(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect(login)
    user = stdata.objects.get(id=user_id)
    
    if request.method == 'POST':
        form = notesform(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = user         
            obj.save()
            print("notes submitted!!!")
            form = notesform()
        else:
            print(form.errors)
    else:
        form = notesform()

    return render(request, 'notes.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = contactform(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)

            obj.user = stdata.objects.first()

            obj.save()
            print("form saved")
            return render(request, 'contact.html', {'form': contactform()})
        else:
            print(form.errors)
    else:
        form = contactform()

    return render(request, 'contact.html', {'form': form})

def aboutus(request):
    return render(request,'aboutus.html')