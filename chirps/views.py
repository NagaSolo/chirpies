from django.shortcuts import render

def home(request):
    return render(request, 'chirps/home.html')

def about(request):
    return render(request, 'chirps/about.html', {'title': 'About'})