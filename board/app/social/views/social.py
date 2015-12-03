# -*- coding: utf-8 -*-

from board.api.views import ViewSet
from board.app.social.serializers import SocialSerializer, ProviderSocial

class SocialViewSet(ViewSet):
	model = ProviderSocial
	serializer_class = SocialSerializer