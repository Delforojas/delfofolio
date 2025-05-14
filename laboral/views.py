from django.shortcuts import render
from .models import ExperienciaLaboral

def experiencia_laboral(request):
    laborales = ExperienciaLaboral.objects.all()
    return render(request, "laboral/laboral.html", {'laborales': laborales})