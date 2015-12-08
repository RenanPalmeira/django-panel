from __future__ import unicode_literals

from django.test import TestCase

from board.core.application.models import Application

class AccountTestCase(TestCase):
	fixtures = ['application.json', ]

	def setUp(self):
		self.model = Application()

	def test_model(self):
		self.model.name = "ApplicationTest"
		self.model.slug = "application_test"
		self.model.icon = "octicon octicon-beaker"
		self.model.color = "#00bfff"
		self.model.order = 42
		self.model.save()

	
