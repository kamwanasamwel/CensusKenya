from django.shortcuts import render, get_object_or_404
from .models import General

# Create your views here.

def home(request):
    everybody = General.objects.all()
    return render(request, 'temps/home.html', {'everybody':everybody})

# def geom(requests):
#     data = {'data': None}
#     poly = 
