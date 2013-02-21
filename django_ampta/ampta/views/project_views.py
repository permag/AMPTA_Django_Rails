from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from ampta.models import Project
from django.http import HttpResponse

def index(request):
    projects = Project.objects.order_by('date_added')
    return render(request, 'projects/index.html', { 'projects': projects })

def show(request, project_id=None):
    return HttpResponse("project#show")