from django import template
from django.template import Library, Node

register = template.Library()

@register.filter(name='user_projects')
def user_projects(user):
    projects = user.projects.order_by('-date_added')
    return projects

@register.filter(name='project_owned_by_user')
def project_owned_by_user(project, user):
    return project.owned_by_user(user)

@register.filter(name='project_or_ticket_owned_by_user')
def project_or_ticket_owned_by_user(ticket, user):
	return ticket.owned_by_user(user) or ticket.project.owned_by_user(user)