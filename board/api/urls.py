from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from board.app.project.views import ProjectViewSet
from board.app.social.views import SocialViewSet
from board.core.application.views import ApplicationViewSet
from board.core.account.views import AccountViewSet
from board.core.configuration.views import ConfigurationViewSet

router = DefaultRouter()
router.register(r'configuration', ConfigurationViewSet, 'Gear')
router.register(r'account', AccountViewSet, 'Account')
router.register(r'social', SocialViewSet, 'Social')
router.register(r'project', ProjectViewSet, 'Project')
router.register(r'application', ApplicationViewSet, 'Application')