from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    users = models.ManyToManyField(User, related_name='projects')
    owner = models.ForeignKey(User, related_name='projects_owned_by_user')
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()
    def __unicode__(self):
        return self.name
    def owned_by_user(self, user):
        return self.owner == user
    def has_user(self, user):
        return user in self.users.all()
    def get_absolute_url(self):
        return reverse('project', args=[str(self.id)])

class Status(models.Model):
    status_name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.status_name
    class Meta:
        verbose_name_plural = 'Statuses'

class Ticket(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    start_date = models.DateField();
    end_date = models.DateField();
    status = models.ForeignKey(Status, related_name='tickets')
    project = models.ForeignKey(Project, related_name='tickets')
    owner = models.ForeignKey(User, related_name='tickets')
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()
    def __unicode__(self):
        return self.name
    def owned_by_user(self, user):
        return self.owner == user
    def get_absolute_url(self):
        return reverse('project_ticket', args=[str(self.project.id), str(self.id)])