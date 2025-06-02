from django.shortcuts import render
from .models import Dataset

def dataset(request):
    datasets = Dataset.objects.all()
    return render(request, "dataset/dataset.html", {'datasets': datasets})