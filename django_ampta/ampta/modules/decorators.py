from django.shortcuts import get_object_or_404, render
from ampta.models import Project, Ticket

# Get project object and return it to view method IF user is member of project.
def get_project_if_member(function):
    def wrapper(request, project_id=None, *args, **kwargs):
        user = request.user
        project = get_object_or_404(Project, id=project_id)
        if not project.has_user(user) and not project.owned_by_user(user):
            return render(request, 'shared/error.html', { 'error_type': 'private' })
        return function(request, project_id, project, *args, **kwargs)
    return wrapper

# Get ticket object and return it to view method IF user is member of project.
def get_ticket_if_member(function):
    def wrapper(request, project_id=None, ticket_id=None, *args, **kwargs):
        user = request.user
        if project_id and ticket_id:
            project = get_object_or_404(Project, id=project_id)
            ticket = get_object_or_404(project.tickets, id=ticket_id)
        else:
            ticket = get_object_or_404(Ticket, id=ticket_id)
            project = ticket.project
        if not project.has_user(user) and not project.owned_by_user(user) and not ticket.owned_by_user(user):
            return render(request, 'shared/error.html', { 'error_type': 'private' })
        return function(request, project_id, ticket_id, ticket, *args, **kwargs)
    return wrapper