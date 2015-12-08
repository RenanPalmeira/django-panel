# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory, APIClient

class AccountAPITestCase(TestCase):
	fixtures = ['account.json', ]
	def setUp(self):
		self.factory = APIRequestFactory()
		self.client = APIClient()

	def test_api_get(self):
		self.client.login(username='bigboss', password='bigboss')
		request = self.client.get('/en/api/account/')