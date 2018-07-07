from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'temps/home.html')

def maincensus(request):
    return render(request,'temps/main.html')