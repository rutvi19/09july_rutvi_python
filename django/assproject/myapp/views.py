from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def client_register(request):
    if request.method == 'POST':
        Patient.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            email=request.POST['email'],
            phone=request.POST['phone']
        )
        return redirect('success')

    return render(request, 'register.html')