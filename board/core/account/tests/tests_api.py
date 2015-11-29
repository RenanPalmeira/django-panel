# -*- coding: utf-8 -*-

from django.test import TestCase
from rest_framework.test import APIRequestFactory

class AccountAPITestCase(TestCase):
	
	def setUp(self):
		self.factory = APIRequestFactory()

	def test_api_get(self):
		request = self.factory.get('/en/api/account/')