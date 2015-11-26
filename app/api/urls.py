from __future__ import unicode_literals

from django.conf.urls import url, include
from app.core.views import AppViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'app', AppViewSet, 'App')