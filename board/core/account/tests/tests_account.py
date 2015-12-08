# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.auth import authenticate
from board.core.account.models import Account

class AccountTestCase(TestCase):
	
	def setUp(self):
		self.account = Account()

	def test_model(self):
		self.account.username = 'BigBoss'
		self.account.email = 'bigboss@forleven.com'
		self.account.set_password('bigboss')
		self.account.save()

	def test_authenticate(self):
		auth = authenticate(email=self.account.email, password='bigboss')