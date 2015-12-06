from __future__ import unicode_literals

from rest_framework import viewsets, exceptions, response, decorators
from board.api.pagination import CustomPagination

class ViewSet(viewsets.ModelViewSet):
	def get_queryset(self):
		queryset = self.model.objects.all()
		query = self.request.query_params.get('q', None)
		if query:
			try:
				queryset = [self.model.objects.get(slug=query)]
			except Exception, e:
				pass
		return queryset

	@decorators.detail_route(methods=['get',])
	def info(self, request, pk):
		data = {}
		return response.Response(data)