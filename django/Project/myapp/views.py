from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
        if request.method=='POST':
            form=UserForm(request.POST)
            if form.is_valid():
                form.save()
                print("Record Inserted!")
            else:
                print(form.errors)
        return render(request,'index.html')

def showdata(request):
    data=Userdata.objects.all()
    return render(request,'showdata.html',{'data':data})