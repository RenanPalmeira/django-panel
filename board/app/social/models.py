from __future__ import unicode_literals
from django.db import models

from board.core.account.models import Account

class Social(models.Model):
	id_social = models.AutoField(primary_key=True)
	account = models.ForeignKey(Account)
	token = models.CharField(max_length=155)
	username = models.CharField(max_length=155)

	update_date = models.DateTimeField(auto_now=True)
	create_date = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return 'app/'+self.slug

	class Meta:
		db_table = "application"