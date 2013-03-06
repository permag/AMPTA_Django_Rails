from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from ampta.models import Project, Comment
from django.contrib.auth.models import User
from ampta.forms import ProjectForm, CommentForm
import datetime
from django.http import HttpResponse, Http404, HttpResponseServerError
from django.contrib.auth.decorators import login_required
from ampta.modules.decorators import get_project_if_member
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages


@login_required(login_url='/login')
def index(request):
    projects = get_list_or_404(Project.objects.order_by('-date_added'))
    paginator = Paginator(projects, 6)  # nr objects/page
    page = request.GET.get('p')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    return render(request, 'projects/index.html', 
                 {'projects': projects, 'projects_active': True})


@login_required(login_url='/login')
@get_project_if_member
def show(request, project_id=None, project=None):
    if not project:
        project = get_object_or_404(Project, id=project_id)
    comment_form = CommentForm()
    return render(request, 'projects/show.html', 
                 {'project': project, 'comment_form': comment_form})


@login_required(login_url='/login')
def new_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.user, request.POST)  # new form, exclude current user
        if form.is_valid():
            form.instance.owner = request.user
            form.instance.date_added = datetime.datetime.today()
            form.instance.date_updated = datetime.datetime.today()
            form.save()
            form.instance.users.add(request.user)  # add owner to project.users. after save.
            messages.success(request, 'Project was created')
            return redirect(form.instance)  # redirect to created project
    else:
        form = ProjectForm(request.user)  # exclude current user
    return render(request, 'projects/new.html', 
                 {'form': form, 'button': 'Create project', 'header': 'Create project',  
                  'create_projects_active': True})


@login_required(login_url='/login')
def edit_update(request, project_id=None):
    project = get_object_or_404(Project, id=project_id)
    if project.owned_by_user(request.user):
        if request.method == 'POST':
            form = ProjectForm(request.user, request.POST, instance=project)  # exclude current user
            if form.is_valid():
                try:
                    form.instance.date_updated = datetime.datetime.today()
                    form.save()
                    form.instance.users.add(request.user)  # add owner to project.users. after save.
                    messages.success(request, 'Project was updated')
                    return redirect(project)
                except:
                    return HttpResponseServerError()
        else:
            form = ProjectForm(request.user, instance=project)
    else:
        return render(request, 'shared/error.html', 
                     {'error_type': 'permission'})
    return render(request, 'projects/new.html', 
                 {'form': form, 'header': 'Edit project', 'button': 'Update project'})


@login_required(login_url='/login')
def delete(request, project_id=None):
    if request.method == 'POST':
        project = get_object_or_404(Project, id=project_id)
        if project.owned_by_user(request.user):
            project.delete()
            messages.success(request, 'Project "%s" was deleted' % project.name)
            return redirect('projects')
        else:
            return HttpResponse("You don't have permissions to do that.")
    else:
        raise Http404


@login_required(login_url='/login')
def create_comment(request, project_id=None):
    if request.method == 'POST':
        project = get_object_or_404(Project, id=project_id)
        if project.has_user(request.user):
            form = CommentForm(request.POST)
            if form.is_valid():
                form.instance.owner = request.user
                form.instance.project = project
                form.instance.comment_date = datetime.datetime.today()
                try:
                    form.save()
                    messages.success(request, 'Comment was created')
                    return redirect(project)
                except:
                    return HttpResponseServerError()
        else:
            return HttpResponse("You don't have permissions to do that.")
    else:
        raise Http404


@login_required(login_url='/login')
def delete_comment(request, project_id=None, comment_id=None):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=comment_id)
        project = comment.project
        if comment.owner == request.user:
            comment.delete()
            messages.success(request, 'Comment was deleted')
            return redirect(project)
        else:
            return HttpResponse("You don't have permissions to do that.")
    else:
        raise Http404

