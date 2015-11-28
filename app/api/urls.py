from __future__ import unicode_literals

from django.conf.urls import url, include
from app.core.application.views import AppViewSet
from app.core.configuration.views import ConfigurationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'app', AppViewSet, 'App')
router.register(r'configuration/(?P<id>\d+)', ConfigurationViewSet, 'Gear')