from __future__ import unicode_literals

from django.conf.urls import url, include
from .views import ApplicationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'apps', ApplicationViewSet, 'Application')