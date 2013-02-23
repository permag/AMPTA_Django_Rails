from django.forms import ModelForm
from django import forms
import datetime
from django.contrib.auth.models import User
from ampta.models import Project, Ticket

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput)

class ProjectForm(ModelForm):
    start_date = forms.DateField(initial=datetime.date.today)
    # define multi choice form field manually to customize help_text
    users = forms.ModelMultipleChoiceField(User.objects.all(), 
            help_text='Select many by holding down ctrl or cmd key.')
    # add css clas to form field with error
    error_css_class = 'validationError'
    class Meta:
        model = Project
        exclude = ('owner', 'date_added', 'date_updated')

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = ('project', 'owner', 'date_added', 'date_updated')

