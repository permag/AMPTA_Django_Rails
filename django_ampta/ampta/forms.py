from django.forms import ModelForm
from django import forms
import datetime
from django.contrib.auth.models import User
from ampta.models import Project, Ticket, Comment


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

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError('This username is already registered')
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('This e-mail is already registered')
        return data


class ChangeUserPasswordForm(forms.Form):
    password_current = forms.CharField(max_length=40, 
                                       widget=forms.PasswordInput(attrs={'placeholder': 'Current password'}))
    password = forms.CharField(max_length=40, 
                               widget=forms.PasswordInput(attrs={'placeholder': 'New password'}))
    password2 = forms.CharField(max_length=40, 
                                widget=forms.PasswordInput(attrs={'placeholder': 'New password again'}))

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if not password == password2:
            raise forms.ValidationError('Field did not match new password')


class ProjectForm(ModelForm):
    start_date = forms.DateField(initial=datetime.date.today)  # define manually to set initial value
    users = forms.ModelMultipleChoiceField(User.objects.all(), # define manually to customize help_text
                                           help_text='Select many by holding down ctrl or cmd key.',
                                           required=False)
    error_css_class = 'validationError'  # add css class to form field with error

    def __init__(self, current_user, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)  # exclude current user from users MultipleChoiceField
        self.fields['users'].queryset = self.fields['users'].queryset.exclude(id=current_user.id)

    class Meta:
        model = Project
        exclude = ('owner', 'date_added', 'date_updated')

    def clean_end_date(self):
        data = self.cleaned_data['end_date']
        if data <= self.cleaned_data['start_date']:
            raise forms.ValidationError('End date must be later than start date')
        return data


class TicketForm(ModelForm):
    start_date = forms.DateField(initial=datetime.date.today)
    error_css_class = 'validationError'

    class Meta:
        model = Ticket
        exclude = ('project', 'owner', 'date_added', 'date_updated')

    def clean_end_date(self):
        data = self.cleaned_data['end_date']
        if data <= self.cleaned_data['start_date']:
            raise forms.ValidationError('End date must be later than start date')
        return data


class CommentForm(ModelForm):
    comment = forms.CharField(max_length=999, widget=forms.Textarea(attrs={'placeholder': 'Comment ...'}))

    class Meta:
        model = Comment
        exclude = ('comment_date', 'owner', 'project')


