from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .serializers import GeneralSerializers, HomesSerializers, HomestedSerializers
from .models import General

# Create your views here.

class GeneralView(viewsets.ModelViewSet):
    queryset = General.objects.all()
    serializer_class = GeneralSerializers

class HomeView(viewsets.ModelViewSet):
    queryset = General.objects.all()
    serializer_class = GeneralSerializers


def home(request):
    everybody = General.objects.all()
    return render(request, 'temps/home.html', {'everybody':everybody})

# def geom(requests):
#     data = {'data': None}
#     poly = 
