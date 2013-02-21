from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from ampta.models import Project, ProjectForm
import datetime
from django.http import HttpResponse

def index(request):
    projects = get_list_or_404(Project.objects.order_by('date_added'))
    return render(request, 'projects/index.html', { 'projects': projects })

def show(request, project_id=None):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/show.html', { 'project': project })

def new_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            form.instance.date_added = datetime.datetime.today()
            form.instance.date_updated = datetime.datetime.today()
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'projects/new.html', { 'form': form, 'submit': 'Create project' })

def edit_update(request, project_id=None):
    project = get_object_or_404(Project, id=project_id)
    if project.owned_by_user(request.user):
        if request.method == 'POST':
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                try:
                    form.instance.date_updated = datetime.datetime.today()
                    form.save()
                    return redirect("/projects/{0}".format(project_id))
                except:
                    return HttpResponseServerError()
        else:
            form = ProjectForm(instance=project)
    else:
        return HttpResponse("You don't have permissions to do that.")
    return render(request, 'projects/new.html', { 'form': form, 'submit': 'Update project' })



