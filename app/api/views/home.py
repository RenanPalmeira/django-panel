# -*- coding: utf-8 -*-

from rest_framework import viewsets
from app.api.serializers import ApplicationSerializer, Application
from app.api.pagination import CustomPagination

class ApplicationViewSet(viewsets.ModelViewSet):
	model = Application
	serializer_class = ApplicationSerializer

	def get_queryset(self):
		queryset = Application.objects.all()
		loadtype = self.request.query_params.get('loadtype', None)
		if loadtype == 'results':
		    self.pagination_class = CustomPagination
		return queryset