from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def notes(request):
    if request.method=='POST':
        mynote=notesform(request.POST,request.FILES)
        if mynote.is_valid():
            mynote.save()
            print("your notes has been uploaded!!")
        else:
            print(mynote.errors)
    return render(request,'notes.html')