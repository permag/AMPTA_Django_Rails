from django import template
from django.template import Library, Node
from django.shortcuts import get_list_or_404
from ampta.models import Project, Ticket

register = template.Library()

@register.filter(name='user_projects')
def user_projects(user):
    projects = user.projects.order_by('-date_added')
    return projects

@register.filter(name='owned_by_user')
def owned_by_user(project, user):
    return project.owned_by_user(user)
