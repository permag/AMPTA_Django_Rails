from django.shortcuts import render, redirect
from django.http import HttpResponse
from ampta.forms import LoginForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required


# General views

@login_required(login_url='/login')
def home_index(request):
    return render(request, 'general/home.html', {'home_active': True})


def user_login(request):
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_to_try = form.cleaned_data['username']
            password_to_try = form.cleaned_data['password']
            user = authenticate(username=username_to_try, password=password_to_try)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse("<h1>Your account is disabled</h1>")
            else:
                message = "Wrong username or password"
    else:
        form = LoginForm()
    return render(request, 'general/login.html', {'form': form, 'message': message})


def user_logout(request):
    logout(request)
    return redirect('login')