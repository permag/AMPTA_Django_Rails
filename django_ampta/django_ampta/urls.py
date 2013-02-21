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

# Home view
urlpatterns += patterns('ampta.views.home_views',
    # root
    url(r'^$', 'index', name='root'),
    # home
    url(r'home/$', 'index', name='home'),
)

# Project views
urlpatterns += patterns('ampta.views.project_views',
    # projects
    url(r'^projects/$', 'index', name='projects'),
    # projects/1
    url(r'^projects/(?P<project_id>\d+)/$', 'show', name='project'),

)

# Ticket views
urlpatterns += patterns('ampta.views.ticket_views',

)