# -*- coding: utf-8 -*-

from rest_framework import viewsets, exceptions, response
from board.api.pagination import CustomPagination

class ViewSet(viewsets.ModelViewSet):
	def get_queryset(self):
		queryset = self.model.objects.all()
		loadtype = self.request.query_params.get('loadtype', None)
		if loadtype == 'results':
		    self.pagination_class = CustomPagination

		query = self.request.query_params.get('q', None)

		if query:
			try:
				queryset = [self.model.objects.get(slug=query)]
			except Exception, e:
				pass

		return queryset