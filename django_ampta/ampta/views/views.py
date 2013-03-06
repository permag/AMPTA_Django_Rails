from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseServerError
from ampta.forms import LoginForm, RegisterForm, ChangeUserPasswordForm
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


@login_required(login_url='/login')
def user_index(request):
    sort_letter = request.GET.get('s')
    if sort_letter:
        users = (User.objects.filter(last_name__startswith=sort_letter)
                             .order_by('last_name', 'first_name'))
    else:
        users = get_list_or_404(User.objects.order_by('last_name', 'first_name'))
    page = request.GET.get('p')
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


def new_create_user(request):
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
                messages.success(request, """Thanks %s, for registering. 
                                          You are now logged in.""" % first_name)
                return redirect('home')
            except:
                return HttpResponseServerError()
    else:
        form = RegisterForm()
    return render(request, 'users/new.html', {'form': form})


@login_required(login_url='/login')
def edit_update_user(request):
    user = request.user
    if request.method == 'POST':
        form = ChangeUserPasswordForm(request.POST)
        if form.is_valid():
            password_current = form.cleaned_data['password_current']
            user.set_password(form.cleaned_data['password'])
            password2 = form.cleaned_data['password2']
            user_auth = authenticate(username=user.username, password=password_current)
            if  user_auth is not None:
                try:
                    user.save()
                    messages.success(request, 'Your password was updated')
                    return redirect('/users/%i' % user.id)
                except:
                    return HttpResponseServerError()
            else:
                messages.error(request, 'Current password is wrong. Try again.')
                return redirect('edit_user')
    else:
        form = ChangeUserPasswordForm()
    return render(request, 'users/edit_password.html', {'form': form})

