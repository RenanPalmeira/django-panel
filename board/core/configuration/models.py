from __future__ import unicode_literals
from django.db import models

from board.core.account.models import Account

class Configuration(models.Model):
	id_configuration = models.AutoField(primary_key=True)
	account = models.ForeignKey(Account)

	key = models.CharField(max_length=250)
	value = models.CharField(max_length=250)
	slug = models.SlugField()
	
	update_date = models.DateTimeField(auto_now=True)
	create_date = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	def __unicode__(self):
		return self.key

	def get_absolute_url(self):
		return 'app/'+self.slug

	class Meta:
		app_label = "configuration"
		db_table = "configuration"

class Permission(models.Model):
	id_permission = models.AutoField(primary_key=True)
	account = models.ForeignKey(Account)

	key = models.CharField(max_length=250)
	value = models.CharField(max_length=250)
	
	update_date = models.DateTimeField(auto_now=True)
	create_date = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	def __unicode__(self):
		return self.key

	class Meta:
		app_label = "configuration"
		db_table = "permission"