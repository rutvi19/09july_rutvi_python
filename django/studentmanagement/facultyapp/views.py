from django.shortcuts import render,redirect
from .forms import *
from .models import *
from studentapp.models import *

# Create your views here.

def fa_login(request):
    if request.method == 'POST':
        f_email =  request.POST.get('email')
        f_password =  request.POST.get('password')
        faculty = fa_data.objects.filter(email=f_email, password=f_password).first()
        if faculty:
            request.session['faculty_id'] = faculty.id                    
            print('login successfully!!')
            return redirect('fa_dashboard')
        else:
            print('Login failed!!')
    return render(request,'fa_login.html')

def fa_register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if fa_data.objects.filter(email=email).exists():
            return render(request,'fa_register.html')
        form = faform(request.POST)
        if form.is_valid():
            form.save()
            print("register successfully!!")
            return redirect('fa_login')
        else:
            print(form.errors)
    return render(request,'fa_register.html')

def fa_dashboard(request):

    students  = stdata.objects.all() 
    notes = notes_cls.objects.all()
    course = std_course.objects.all()

    total_n = len(notes)
    total_u = len(students)
    context = {
        'students': students, 
        'total_u': total_u,
        'total_n': total_n,
        'course' : course,
        

    }
    return render(request,'fa_dashboard.html',context)

def delete_student(request, id):
    stdata.objects.get(id=id).delete()
    return redirect('fa_dashboard')
