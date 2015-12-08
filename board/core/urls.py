from __future__ import unicode_literals

from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns

from .account import views as account
from .configuration import views as configuration

urlpatterns = [
    url(r'^account/$', account.home),
    url(r'^configuration/$', configuration.home),
]