from ampta.models import Project, Ticket, Status, Comment
from django.contrib import admin

admin.site.register(Project)
admin.site.register(Ticket)
admin.site.register(Status)
admin.site.register(Comment)