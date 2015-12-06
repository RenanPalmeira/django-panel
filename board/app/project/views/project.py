from __future__ import unicode_literals

from board.api.views import ViewSet
from board.app.project.serializers import ProjectSerializer, Project

class ProjectViewSet(ViewSet):
	model = Project
	serializer_class = ProjectSerializer