from __future__ import unicode_literals

from board.api.views import ViewSet
from board.core.configuration.serializers import ConfigurationSerializer, Configuration

class ConfigurationViewSet(ViewSet):
	model = Configuration
	serializer_class = ConfigurationSerializer