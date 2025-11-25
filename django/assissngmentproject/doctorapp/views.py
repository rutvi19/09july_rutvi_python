from django.shortcuts import render,redirect
from .models import Doctor
from .models import Patient

# Create your views here.
def index(request):
    return render(request, 'index.html')



def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

def add_doctor(request):
    if request.method == "POST":
        name = request.POST.get("name")
        specialization = request.POST.get("specialization")
        experience = request.POST.get("experience")
        bio = request.POST.get("bio")

        Doctor.objects.create(
            name=name,
            specialization=specialization,
            experience=experience,
            bio=bio
        )

        return redirect('doctor_list')

    return render(request, "add_doctor.html")

def register_patient(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        Patient.objects.create(
            name=name,
            age=age,
            email=email,
            phone=phone
        )
        return redirect('doctor_list')  # after saving go to next page

    return render(request, "register.html")

