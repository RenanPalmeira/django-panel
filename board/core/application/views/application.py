from __future__ import unicode_literals

from board.api.views import ViewSet
from board.core.application.serializers import ApplicationSerializer, Application

class ApplicationViewSet(ViewSet):
	model = Application
	serializer_class = ApplicationSerializer
	lookup_field = 'slug'