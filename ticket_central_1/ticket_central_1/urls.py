"""
Definition of urls for scaffold.
"""

from datetime import datetime
from app import views
from django.conf.urls import url
import django.contrib.auth.views
from django.conf import settings
from django.conf.urls.static import static

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^dashboard$', app.views.dashboard, name='dashboard'),
    url(r'^work_tickets$', app.views.work_tickets, name='work_tickets'),
    ##url(r'^work_detail/(?P<id>\d+)$', app.views.work_detail, name='work_detail'),
    url(r'^work_detail/(?P<id>\d+)$', app.views.tech_detail, name='work_detail'),
    url(r'^mytickets$', app.views.mytickets, name='mytickets'),
    url(r'^ticket$', app.views.add_model, name='add_model'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^password/$', app.views.change_password, name='change_password'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)