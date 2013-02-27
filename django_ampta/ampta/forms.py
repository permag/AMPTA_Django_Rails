from django.forms import ModelForm
from django import forms
import datetime
from django.contrib.auth.models import User
from ampta.models import Project, Ticket


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=40, 
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput())
    password = forms.CharField(max_length=40, widget=forms.PasswordInput())
    email = forms.EmailField(max_length=75, widget=forms.TextInput())
    first_name = forms.CharField(max_length=30, widget=forms.TextInput())
    last_name = forms.CharField(max_length=30, widget=forms.TextInput())


class ProjectForm(ModelForm):
    start_date = forms.DateField(initial=datetime.date.today)  # define manually to set initial value
    users = forms.ModelMultipleChoiceField(User.objects.all(), # define manually to customize help_text
            help_text='Select many by holding down ctrl or cmd key.')
    error_css_class = 'validationError'  # add css class to form field with error

    class Meta:
        model = Project
        exclude = ('owner', 'date_added', 'date_updated')


class TicketForm(ModelForm):
    start_date = forms.DateField(initial=datetime.date.today)
    error_css_class = 'validationError'

    class Meta:
        model = Ticket
        exclude = ('project', 'owner', 'date_added', 'date_updated')

