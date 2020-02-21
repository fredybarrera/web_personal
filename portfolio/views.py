from django.shortcuts import render
# Desde el archivo models.py (modelo), obtengo la clase Project
from .models import Project


# Create your views here.

def portafolio(request):
    projects = Project.objects.all();
    return render(request, "portfolio/portafolio.html", {'projects':projects})
