from __future__ import unicode_literals
from django.db import models

from board.core.account.models import Account

class ProviderSocial(models.Model):
	id_provider_social = models.AutoField(primary_key=True)

	name = models.CharField(max_length=155)

	update_date = models.DateTimeField(auto_now=True)
	create_date = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	class Meta:
		app_label = "social"
		db_table = "social_provider"

class Social(models.Model):
	id_social = models.AutoField(primary_key=True)
	account = models.ForeignKey(Account)
	
	token = models.CharField(max_length=155)
	username = models.CharField(max_length=155)

	update_date = models.DateTimeField(auto_now=True)
	create_date = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	def __unicode__(self):
		return self.username

	def get_absolute_url(self):
		return 'app/'+self.slug

	class Meta:
		app_label = "social"
		db_table = "social"