#coding: utf8 
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from ampta.models import Project, Ticket
from ampta.forms import TicketForm
import datetime
from django.http import HttpResponse, HttpResponseServerError, Http404
from django.contrib.auth.decorators import login_required
from ampta.modules.decorators import get_project_if_member, get_ticket_if_member
from django.core import serializers


@login_required(login_url='/login')
def index(request, project_id=None, extension=None):
    if project_id:
        project = get_object_or_404(Project, id=project_id)
        if project.has_user(request.user) or project.owned_by_user(request.user):
            tickets = get_list_or_404(project.tickets.order_by('-date_added'))
        else:
            raise Http404
    else:
        tickets = request.user.tickets.order_by('-date_added')
    if extension == 'json':
        data = serializers.serialize('json', tickets)
        return HttpResponse(data, mimetype='application/json')
    return render(request, 'tickets/index.html', {'tickets': tickets})


@login_required(login_url='/login')
@get_ticket_if_member
def show(request, project_id=None, ticket_id=None, ticket=None ):
    if not ticket:
        ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'tickets/show.html', {'ticket': ticket})


@login_required(login_url='/login')
@get_project_if_member
def new_create(request, project_id=None, project=None):
    if request.method == 'POST':
        #project = get_object_or_404(Project, id=project_id)
        form = TicketForm(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            form.instance.project = project
            form.instance.date_added = datetime.datetime.today()
            form.instance.date_updated = datetime.datetime.today()
            try:
                form.save()
                return redirect(project)
            except:
                HttpResponseServerError()
    else:
        form = TicketForm()
    return render(request, 'tickets/new.html', 
                 {'form': form, 'title': 'Create ticket'})


@login_required(login_url='/login')
def edit_update(request, project_id=None, ticket_id=None):
    project = get_object_or_404(Project, id=project_id)
    ticket = get_object_or_404(project.tickets, id=ticket_id)
    user = request.user
    if project.owned_by_user(user) or ticket.owned_by_user(user):
        if request.method == 'POST':
            form = TicketForm(request.POST, instance=ticket)
            if form.is_valid():
                try:
                    form.instance.date_updated = datetime.datetime.today()
                    form.save()
                    return redirect(ticket)
                except:
                    return HttpResponseServerError()
        else:
            form = TicketForm(instance=ticket)
    else:
        return render(request, 'shared/error.html', {'error_type': 'permission'})
    return render(request, 'tickets/new.html', {'form': form, 'title': 'Update ticket'})


@login_required(login_url='/login')
def delete(request, project_id=None, ticket_id=None):
    if request.method == 'POST':
        ticket = get_object_or_404(Ticket, id=ticket_id)
        project = ticket.project
        user = request.user
        if project.owned_by_user(user) or ticket.owned_by_user(user):
            try:
                ticket.delete()
                return redirect(project)
            except:
                return HttpResponseServerError()
        else:
            return HttpResponse("You don't have permissions to do that.")
    else:
        raise Http404

