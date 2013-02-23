from django.shortcuts import render, redirect
from django.http import HttpResponse

# General views

def home_index(request):
    return render(request, 'home/index.html', None)
