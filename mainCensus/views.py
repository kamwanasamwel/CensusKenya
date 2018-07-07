from django.shortcuts import render, get_object_or_404

# Create your views here.

def home(request):
    everybody = General.objects.all()
    return render(request, 'home.html', {'everybody':everybody})
