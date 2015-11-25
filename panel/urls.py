"""panel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns

from axes.decorators import watch_login
from app.desk import views as desk
from app.configuration import views as configuration

from app.api.urls import router as api

urlpatterns = [
    url(r'^logout/$', desk.logout),
    url(r'^desk$', desk.home),
]

urlpatterns += i18n_patterns(
    url(r'^app/gear', configuration.form, name='app'),
    url(r'^api/', include(api.urls)),
    url(r'^login/$', watch_login(desk.login)),
    url(r'^locked/$', desk.login, name='recaptcha'),
)