from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
import datetime

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

####
### FORMS
##

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput)

class ProjectForm(ModelForm):
    start_date = forms.DateField(initial=datetime.date.today)
    # define multi choice form field manually to customize help_text
    users = forms.ModelMultipleChoiceField(User.objects.all(), 
            help_text='Select many by holding down ctrl or cmd key.')
    class Meta:
        model = Project
        exclude = ('owner', 'date_added', 'date_updated')

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = ('project', 'owner', 'date_added', 'date_updated')



