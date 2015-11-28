# -*- coding: utf-8 -*-

from rest_framework import viewsets, exceptions, response
from app.api.pagination import CustomPagination
from app.core.configuration.serializers import ConfigurationSerializer, Configuration

class ConfigurationViewSet(viewsets.ModelViewSet):
	model = Configuration
	serializer_class = ConfigurationSerializer

	def get_queryset(self):
		queryset = Configuration.objects.all()
		loadtype = self.request.query_params.get('loadtype', None)
		if loadtype == 'results':
		    self.pagination_class = CustomPagination

		query = self.request.query_params.get('q', None)

		if query:
			try:
				queryset = [Configuration.objects.get(slug=query)]
			except Exception, e:
				pass

		return queryset