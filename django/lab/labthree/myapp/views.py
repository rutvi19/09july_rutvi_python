from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def forms(request):
    return render(request, 'forms.html')
