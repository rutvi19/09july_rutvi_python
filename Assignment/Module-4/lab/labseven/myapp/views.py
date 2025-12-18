from django.shortcuts import render
from datetime import date

def home(request):
    context = {
        'username': 'Rutvi',
        'today': date.today()
    }
    return render(request, 'home.html', context)
