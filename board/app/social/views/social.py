# -*- coding: utf-8 -*-

from board.api.views import ViewSet
from board.app.social.serializers import SocialSerializer, Social

class SocialViewSet(ViewSet):
	model = Social
	serializer_class = SocialSerializer