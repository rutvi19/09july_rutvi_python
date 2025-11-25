from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def login(request):
      if request.method=='POST':
        em=request.POST['email']
        pa=request.POST['password']
        
        user=UserSignup.objects.filter(email=em,password=pa)
        if user:
            print("Login Successfully!")
            request.session['user']=em
            return redirect('home')
        else:
            print("Error!Login faild...")
        
        return render(request,'index.html')