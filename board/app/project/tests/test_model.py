from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth import authenticate
from board.app.project.models import Project

class AccountTestCase(TestCase):
	
	def setUp(self):
		self.project = Project()

	def test_model(self):
		self.project.name = 'BigBoss'
		self.project.site = 'forleven.com'
		self.project.slug = 'bigboss'
		self.project.save()