# -*- coding: utf-8 -*-

from board.api.views import ViewSet
from board.core.account.serializers import AccountSerializer, Account

class AccountViewSet(ViewSet):
	model = Account
	serializer_class = AccountSerializer