from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_ampta.views.home', name='home'),
    # url(r'^django_ampta/', include('django_ampta.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# General views
urlpatterns += patterns('ampta.views.views',
    # root
    url(r'^$', 'home_index', name='root'),
    # home
    url(r'home/$', 'home_index', name='home'),
    # login
    url(r'^login/$', 'login_user', name='login'),
    # logout
    url(r'^logout/$', 'logout_user', name='logout'),
    # register
    url(r'^register/$', 'create_user', name="create_user"),
)

# Project viewss
urlpatterns += patterns('ampta.views.project_views',
    # projects
    url(r'^projects/$', 'index', name='projects'),
    # projects/1
    url(r'^projects/(?P<project_id>\d+)/$', 'show', name='project'),
    # projects/new
    url(r'^projects/new/$', 'new_create', name='new_project'),
    # projects/1/edit
    url(r'^projects/(?P<project_id>\d+)/edit/$', 'edit_update', name='edit_project'),
    # projects/1/delete
    url(r'^projects/(?P<project_id>\d+)/delete/$', 'delete', name='delete_project'),
)

# Ticket views
urlpatterns += patterns('ampta.views.ticket_views',
    # tickets
    url(r'^tickets/$', 'index', name='tickets'),
    # tickets.json|xml
    url(r'^tickets\.(?P<extension>(json)|(xml))$', 'index', name='tickets'),
    # tickets/1
    url(r'^tickets/(?P<ticket_id>\d+)/$', 'show', name="ticket"),
    # projects/1/tickets
    url(r'^projects/(?P<project_id>\d+)/tickets/$', 'index', name='project_tickets'),
    # projects/1/tickets/1
    url(r'^projects/(?P<project_id>\d+)/tickets/(?P<ticket_id>\d+)/$', 'show', name='project_ticket'),
    # projects/1/tickets/new
    url(r'^projects/(?P<project_id>\d+)/tickets/new/$', 'new_create', name='new_project_ticket'),
    # projects/1/tickets/1/edit
    url(r'^projects/(?P<project_id>\d+)/tickets/(?P<ticket_id>\d+)/edit/$', 'edit_update', name='edit_project_ticket'),
    # projects/1/tickets/1/delete
    url(r'^projects/(?P<project_id>\d+)/tickets/(?P<ticket_id>\d+)/delete/$', 'delete', name='delete_project_ticket'),

)

