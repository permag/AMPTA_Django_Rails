from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from ampta.models import Project, Ticket
from django.http import HttpResponse

def index(request, project_id=None):
	if project_id:
		project = get_object_or_404(Project, id=project_id)
		tickets = get_list_or_404(project.tickets.order_by('-date_added'))
	else:
		tickets = get_list_or_404(Ticket.objects.order_by('-date_added'))
	return render(request, 'tickets/index.html', { 'tickets': tickets })

def show(request, project_id=None, ticket_id=None):
	if project_id and ticket_id:
		project = get_object_or_404(Project, id=project_id)
		ticket = get_object_or_404(project.tickets.get(id=ticket_id))
	elif ticket_id:
		ticket = get_object_or_404(Ticket, id=ticket_id)
	return render(request, 'tickets/show.html', { 'ticket': ticket })