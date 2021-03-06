from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})


def detail(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'projects/detail.html', {'project': project})