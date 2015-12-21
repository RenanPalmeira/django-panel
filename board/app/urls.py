from __future__ import unicode_literals

from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns

from .news import views as news
from .social import views as social

urlpatterns = [
    url(r'^social/$', social.home),
    url(r'^twitter/$', social.twitter),
    url(r'^news/$', news.home),
    url(r'^news/list/$', news.listing),
]