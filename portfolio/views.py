from django.shortcuts import render
from .models import Project


def portfolio(request):
    context = {
        "projects": Project.objects.filter(category=Project.Category.GENERAL),
    }
    return render(request, "portfolio/portfolio.html", context)


def dashboards(request):
    context = {
        "projects": Project.objects.filter(category=Project.Category.POWER_BI),
    }
    return render(request, "portfolio/dashboards.html", context)
