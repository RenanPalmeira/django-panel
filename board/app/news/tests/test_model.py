from __future__ import unicode_literals

from django.test import TestCase

from board.core.account.models import Account
from board.app.news.models import Article
from board.app.project.models import Project

from board.app.news.tasks import send_link

class ArticleTestCase(TestCase):
	fixtures = ['account.json', ]
	def setUp(self):
		self.article = Article()
		self.account = Account.objects.first()
		self.project = Project(name='Django-panel', site='github.com/RenanPalmeira/django-panel')
		self.project.save()
	
	def test_model(self):
		self.article.account = self.account
		self.article.project = self.project
		self.article.reference = 'https://www.python.org'

		self.article.title = 'Hello world'
		self.article.content = '...'
		self.article.save()

	def test_tasks(self):
		result= send_link.delay('https://www.python.org')