from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from board.core.account.models import Account
from board.app.project.models import Project

class Article(models.Model):
	id_article = models.AutoField(primary_key=True)

	account = models.ForeignKey(Account)
	project = models.ForeignKey(Project)

	title = models.CharField(max_length=155)
	content = models.TextField()

	reference = models.CharField(max_length=155, null=True, verbose_name=_(u"Reference"))

	update_date = models.DateTimeField(auto_now=True)
	create_date = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	def __unicode__(self):
		return {}

	class Meta:
		app_label = "news"
		db_table = "article"

class ArticleConfiguration(models.Model):
	id_article_configuration = models.AutoField(primary_key=True)

	key = models.CharField(max_length=155)
	value = models.CharField(max_length=155)

	icon = models.CharField(max_length=155, null=True)

	update_date = models.DateTimeField(auto_now=True)
	create_date = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	class Meta:
		app_label = "news"
		db_table = "article_configuration"