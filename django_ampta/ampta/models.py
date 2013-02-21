from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(User, related_name='projects')
    users = models.ManyToManyField(User)
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()
    def __unicode__(self):
        return self.name

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
    project = models.ForeignKey(Project, related_name='tickets')
    status = models.ForeignKey(Status, related_name='tickets')
    owner = models.ForeignKey(User, related_name='tickets')
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()
    def __unicode__(self):
        return self.name

