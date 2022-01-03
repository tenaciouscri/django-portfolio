from django.shortcuts import render
from projects.models import Project

def project_index(request, pk):
    projects = Project.objects.all(pk=pk)
    context = {
        "projects": projects
    }
    return render(request, "project_index.html", context)