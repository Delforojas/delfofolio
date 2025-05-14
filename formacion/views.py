from django.shortcuts import render
from .models import Formar , FormacionAcademica

# Create your views here.
def formacion(request):
    formars = Formar.objects.all()
    return render(request, "formacion/formacion.html", {'formars': formars})

def experiencia(request):
    formaciones = FormacionAcademica.objects.all()
    return render(request, "formacion/experiencia.html", {'formaciones': formaciones})