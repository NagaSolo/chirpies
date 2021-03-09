from django.shortcuts import render
from .models import Chirp

def home(request):
    context = {
        'chirps': Chirp.objects.all()
    }
    return render(request, 'chirps/home.html', context)

def about(request):
    return render(request, 'chirps/about.html', {'title': 'About'})