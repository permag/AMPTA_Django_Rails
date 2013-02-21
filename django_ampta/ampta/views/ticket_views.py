from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from ampta.models import Project, Ticket
from django.http import HttpResponse