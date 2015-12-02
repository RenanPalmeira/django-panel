from __future__ import unicode_literals

from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns

from .application import views as application

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', application.home),
]