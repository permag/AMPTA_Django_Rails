from django import template
from django.template import Library, Node

register = template.Library()


@register.filter(name='user_projects')  # "name", if other name than function
def user_projects(user):
    """ Get all projects for a user.
    Used in the left menu navigation.

    """
    projects = user.projects.order_by('-date_added')
    return projects


@register.filter
def project_owned_by_user(project, user):
    """ Check if project is owned my user.
    Return true if so.

    """
    return project.owned_by_user(user)


@register.filter
def ticket_owned_by_user(ticket, user):
    """ Check if ticket is owned by user.

    """
    return ticket.owned_by_user(user)


@register.filter
def project_or_ticket_owned_by_user(ticket, user):
    """ Check if project or ticket is owned by user.

    """
    return ticket.owned_by_user(user) or ticket.project.owned_by_user(user)


@register.filter
def user_is_project_member_or_owner(project, user):
    """ Check if user is member or owner of project.

    """
    return project.owned_by_user(user) or project.has_user(user)


@register.filter
def date_has_passed(date):
    """ Check if given date is older than todays date.
    If date is older, return true.

    """
    import datetime

    return date > datetime.date.today()


@register.filter
def get_hurry_tickets(user):
    """ Get tickets for which the end date will pass within a few days

    """
    import datetime
    from datetime import date, timedelta

    date_from = datetime.date.today()
    date_to = datetime.date.today() + timedelta(days=3)  # days to add
    return user.tickets.filter(end_date__range=(date_from, date_to))

