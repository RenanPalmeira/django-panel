from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns

from axes.decorators import watch_login
from board.app.desk import views as desk
from board.api.urls import router as api

urlpatterns = [
    url(r'^logout/$', desk.logout),
    url(r'^desk$', desk.home),
]

urlpatterns += i18n_patterns(
    url(r'^api/', include(api.urls)),
    url(r'^login/$', watch_login(desk.login)),
    url(r'^locked/$', desk.login, name='recaptcha'),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += [
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^website/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),  
    # url(r'^.*$', website.home),
]