from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .serializers import GeneralSerializers, HomesSerializers, HomestedSerializers
from .models import General, Homested
from django.core.serializers import serialize
# Create your views here.

class GeneralView(viewsets.ModelViewSet):
    queryset = General.objects.all()
    serializer_class = GeneralSerializers

class HomeView(viewsets.ModelViewSet):
    queryset = General.objects.all()
    serializer_class = GeneralSerializers


def home(request):
    everybody = General.objects.all()
    j_son = serialize('geojson', Homested.objects.all(), fields=('location', 'hs_code'))
    return render(request, 'temps/main.html', {'everybody':everybody, 'j_son': j_son })

# def geom(requests):
#     data = {'data': None}
#     poly = 
