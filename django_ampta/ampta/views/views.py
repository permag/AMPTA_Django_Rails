from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseServerError
from ampta.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# General views

@login_required(login_url='/login')
def home_index(request):
    return render(request, 'general/home.html', {'home_active': True})


def login_user(request):
    message = ''
    if request.user.is_authenticated():
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_to_try = form.cleaned_data['username']
            password_to_try = form.cleaned_data['password']
            user = authenticate(username=username_to_try, password=password_to_try)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.info(request, 'Welcome back, %s!' % user.first_name)
                    return redirect('home')
                else:
                    return HttpResponse('<h1>Your account is disabled</h1>')
            else:
                message = 'Wrong username or password'
    else:
        form = LoginForm()
    return render(request, 'general/login.html', {'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('login')


def create_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(username=username, email=email, 
                                            password=password)
            user.first_name = first_name
            user.last_name = last_name
            try:
                user.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.info(request, 'Thanks for registering. You are now logged in.')
                return redirect('home')
            except:
                return HttpResponseServerError()
    else:
        form = RegisterForm()
    return render(request, 'general/register.html', {'form': form})


@login_required(login_url='/login')
def user_index(request, page=None):
    users = get_list_or_404(User.objects.order_by('last_name', 'first_name'))
    paginator = Paginator(users, 20)  # nr objects/page
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'users/index.html', 
                 {'users': users, 'all_users_active': True})


@login_required(login_url='/login')
def user_show(request, user_id=None):
    the_user = get_object_or_404(User, id=user_id)
    return render(request, 'users/show.html', {'the_user': the_user})

