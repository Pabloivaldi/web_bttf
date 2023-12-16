from django.shortcuts import render
from .models import Project

# Create your views here.

def eshop(request):
    projects = Project.objects.all()
    return render(request, "eshop/eshop.html", {'projects':projects})
    